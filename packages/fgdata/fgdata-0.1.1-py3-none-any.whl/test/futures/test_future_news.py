# -*- coding: utf-8 -*-
# test/fgdata/futures/test_future_news.py

import unittest
# from fgdata.futures.future_news import futures_news_sina
import fgdata as fg
import pandas as pd


futures_code = 'CU'
df = fg.futures_news_sina(futures_code)
print(df.head())
print(df[['期货品种','新闻标题','发布日期']])