# FGdata

A data toolkit for the Chinese futures market.

一个中国期货市场的数据工具包。

## Installation
```bash
pip install fgdata
```
## Usage Examples

```python
import fgdata as fg
import pandas as pd


futures_code = 'CU'
df = fg.futures_news_sina(futures_code)
print(df.head())
```