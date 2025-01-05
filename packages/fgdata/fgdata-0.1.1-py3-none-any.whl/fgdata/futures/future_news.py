# -*- coding: utf-8 -*-
import requests
from lxml import html
import pandas as pd

def futures_news_sina(futures_code):
    # 根据期货品种代码构建URL
    url = f'https://finance.sina.com.cn/money/future/{futures_code}/'
    
    # 发送HTTP请求
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the webpage for futures code {futures_code}. Status code: {response.status_code}")
    
    # 解析HTML
    tree = html.fromstring(response.content)
    
    xpath_base = '/html/body/div/div[4]/div[1]/div[2]/div[2]/ul/li'
    li_elements = tree.xpath(xpath_base)
    
    # 初始化列表来存储数据
    data = []
    
    for li in li_elements:
        # 期货品种
        futures_type = li.xpath('span/text()')[0].strip('[]')
        
        # 新闻标题和链接
        a_element = li.xpath('a')[0]
        title = a_element.xpath('text()')[0].strip()
        link = a_element.xpath('@href')[0]
        
        # 发布日期
        date_str = li.xpath('text()')[-1].strip('()')
        
        # 将数据添加到列表中
        data.append({
            '期货品种': futures_type,
            '新闻标题': title,
            '发布日期': date_str, 
            '链接': link
        })
    
    
    df = pd.DataFrame(data)
    return df

# futures_code = 'CU'
# df = futures_news_sina(futures_code)
# print(df.head())
# print(df[['期货品种','新闻标题','发布日期']])