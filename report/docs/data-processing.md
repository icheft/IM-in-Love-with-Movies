
# 資料處理


```python
# import required packages, though not all of them are actually used
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator
import matplotlib.mlab as mlab
import matplotlib.dates as mpl_dates
%matplotlib inline

import mplfinance as mpf 
from mplfinance.original_flavor import candlestick_ohlc
# set fig size; bigger DPI results in bigger fig
plt.rcParams["figure.dpi"] = 100

import seaborn as sns
import pandas as pd
import numpy as np
import sympy as sp
import math
import scipy.stats as stats
from scipy.stats import norm
from scipy.optimize import curve_fit
import statsmodels.api as sm
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as smm
import statsmodels.stats.outliers_influence as sso
from statsmodels.stats.stattools import durbin_watson as sdw
import statsmodels.stats.libqsturng
import plotly.express as px
from datetime import datetime

import stemgraphic as stem

# from ete3 import Tree, faces, AttrFace, TreeStyle, TextFace

# from mgt2001 import *

import mgt2001
from mgt2001.hyp.ind import two_population, two_population_proportion
import mgt2001.hyp.anova as anova
import mgt2001.hyp.chi2 as chi2
import mgt2001.hyp.non as non

import random
import itertools
import math

plt.style.use('ggplot') # refined style

import warnings
warnings.filterwarnings("ignore")

mgt2001.__version__ # show version of mgt2001
```




    '0.4.1.4'




```python
movie_df = pd.read_excel('../data/sorted_all_movie.xlsx', index_col=0)
covid_date = datetime(2020, 3, 1)
movie_df['has_collection'] = movie_df['belongs_to_collection'].isna().replace({True: 0, False: 1})
movie_df['pre_covid'] = (movie_df['release_date'] < covid_date).replace({True: 1, False: 0})
movie_df['post_covid'] = (movie_df['release_date'] >= covid_date).replace({True: 1, False: 0})
movie_df['release_year'] = movie_df['release_date'].apply(lambda x: x.year)
movie_df['release_month'] = movie_df['release_date'].apply(lambda x: x.month)

display(movie_df.head())
display(movie_df.tail())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
      <th>budget</th>
      <th>genres</th>
      <th>original_language</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>TW_release_date</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>...</th>
      <th>rating</th>
      <th>rotten_aud_score</th>
      <th>zh_title</th>
      <th>belongs_to_collection</th>
      <th>has_homepage</th>
      <th>has_collection</th>
      <th>pre_covid</th>
      <th>post_covid</th>
      <th>release_year</th>
      <th>release_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4234</td>
      <td>Scream 3</td>
      <td>40000000</td>
      <td>['Horror', 'Mystery']</td>
      <td>en</td>
      <td>['Craven-Maddalena Films', 'Dimension Films', ...</td>
      <td>2000-02-03</td>
      <td>NaN</td>
      <td>161834276</td>
      <td>116</td>
      <td>...</td>
      <td>R</td>
      <td>37.0</td>
      <td>驚聲尖叫3：終結篇</td>
      <td>Scream Collection</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1907</td>
      <td>The Beach</td>
      <td>40000000</td>
      <td>['Drama', 'Adventure', 'Romance', 'Thriller']</td>
      <td>en</td>
      <td>['Figment Films']</td>
      <td>2000-02-03</td>
      <td>NaN</td>
      <td>144056873</td>
      <td>119</td>
      <td>...</td>
      <td>R</td>
      <td>57.0</td>
      <td>海灘</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15655</td>
      <td>The Tigger Movie</td>
      <td>30000000</td>
      <td>['Family', 'Animation', 'Comedy']</td>
      <td>en</td>
      <td>['Disney Television Animation', 'DisneyToon St...</td>
      <td>2000-02-11</td>
      <td>NaN</td>
      <td>45554533</td>
      <td>77</td>
      <td>...</td>
      <td>G</td>
      <td>62.0</td>
      <td>跳跳虎歷險記</td>
      <td>NaN</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14181</td>
      <td>Boiler Room</td>
      <td>7000000</td>
      <td>['Crime', 'Drama', 'Thriller']</td>
      <td>en</td>
      <td>['New Line Cinema']</td>
      <td>2000-02-18</td>
      <td>NaN</td>
      <td>28780255</td>
      <td>118</td>
      <td>...</td>
      <td>R</td>
      <td>78.0</td>
      <td>搶錢大作戰</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2069</td>
      <td>The Whole Nine Yards</td>
      <td>41300000</td>
      <td>['Comedy', 'Crime']</td>
      <td>en</td>
      <td>['Franchise Pictures', 'Morgan Creek Productio...</td>
      <td>2000-02-18</td>
      <td>NaN</td>
      <td>106371651</td>
      <td>98</td>
      <td>...</td>
      <td>R</td>
      <td>64.0</td>
      <td>殺手不眨眼</td>
      <td>The Whole Nine/Ten Yards Collection</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>2000</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 33 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>title</th>
      <th>budget</th>
      <th>genres</th>
      <th>original_language</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>TW_release_date</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>...</th>
      <th>rating</th>
      <th>rotten_aud_score</th>
      <th>zh_title</th>
      <th>belongs_to_collection</th>
      <th>has_homepage</th>
      <th>has_collection</th>
      <th>pre_covid</th>
      <th>post_covid</th>
      <th>release_year</th>
      <th>release_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3167</th>
      <td>460465</td>
      <td>Mortal Kombat</td>
      <td>20000000</td>
      <td>['Action', 'Fantasy', 'Adventure']</td>
      <td>en</td>
      <td>['Atomic Monster', 'Broken Road Productions', ...</td>
      <td>2021-04-07</td>
      <td>NaN</td>
      <td>76706000</td>
      <td>110</td>
      <td>...</td>
      <td>R</td>
      <td>86.0</td>
      <td>真人快打</td>
      <td>NaN</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2021</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3168</th>
      <td>637649</td>
      <td>Wrath of Man</td>
      <td>40000000</td>
      <td>['Action', 'Crime']</td>
      <td>en</td>
      <td>['Miramax', 'Metro-Goldwyn-Mayer', 'Toff Guy F...</td>
      <td>2021-04-22</td>
      <td>2021-04-29T00:00:00.000Z</td>
      <td>80648577</td>
      <td>119</td>
      <td>...</td>
      <td>R</td>
      <td>91.0</td>
      <td>玩命鈔劫</td>
      <td>NaN</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2021</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3169</th>
      <td>520663</td>
      <td>The Woman in the Window</td>
      <td>4000000</td>
      <td>['Crime', 'Mystery', 'Thriller']</td>
      <td>en</td>
      <td>['Fox 2000 Pictures', 'Scott Rudin Productions...</td>
      <td>2021-05-14</td>
      <td>NaN</td>
      <td>0</td>
      <td>102</td>
      <td>...</td>
      <td>R</td>
      <td>36.0</td>
      <td>窺探</td>
      <td>NaN</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2021</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3170</th>
      <td>503736</td>
      <td>Army of the Dead</td>
      <td>90000000</td>
      <td>['Action', 'Horror', 'Thriller']</td>
      <td>en</td>
      <td>['The Stone Quarry']</td>
      <td>2021-05-14</td>
      <td>NaN</td>
      <td>780000</td>
      <td>148</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>活屍大軍</td>
      <td>Army of the Dead Collection</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2021</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3171</th>
      <td>337404</td>
      <td>Cruella</td>
      <td>200000000</td>
      <td>['Comedy', 'Crime']</td>
      <td>en</td>
      <td>['Walt Disney Pictures']</td>
      <td>2021-05-26</td>
      <td>NaN</td>
      <td>46586903</td>
      <td>134</td>
      <td>...</td>
      <td>PG-13</td>
      <td>97.0</td>
      <td>時尚惡女：庫伊拉</td>
      <td>Cruella Collection</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2021</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 33 columns</p>
</div>



```python
movie_df.hist(figsize=(15, 15))
plt.show()
```


![png](output_7_0.png)


可以看出裡面有需多 outliers，這些 data points 很可能影響到整體結果，所以我們將不考慮這些電影的計算。

在這邊，我們也可以看到 "revenue"、"budget"、"ROI" 這三個重點項目都不是常態分佈，要做分析的話會有點困難。這時候，我們可以採用 `np.log1p()` 來做 data transformation。如要要做預測的話，則是用 `np.exp1p()` 來還原。這部分，會在去除玩異質之後統一處理。


```python
# Plot
fig = plt.figure(figsize=(9, 3))
row, col = 1, 3
fig.subplots_adjust(hspace=0.2, wspace=.5)
ax = fig.add_subplot(row, col, 1)
ax = sns.boxplot(y=movie_df['revenue']) # orient='h' results in horizontal boxplot
plt.title('Revenue')
ax.grid(True)
ax = fig.add_subplot(row, col, 2)
ax = sns.boxplot(y=movie_df['ROI']) # orient='h' results in horizontal boxplot
plt.title('ROI')
ax.grid(True)

ax = fig.add_subplot(row, col, 3)
ax = sns.boxplot(y=movie_df['budget']) # orient='h' results in horizontal boxplot
plt.title('budget')
ax.grid(True)


plt.show()
```


![png](output_9_0.png)


<div class="alert alert-block alert-info">
<b>🍿 你知道嗎？</b><br> 票房最高的電影是 2019 年上映的復仇者聯盟：終局之戰。</div>


```python
movie_df.sort_values(by='revenue', ascending=False).head(20)[['release_date', 'zh_title', 'revenue', 'director']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_date</th>
      <th>zh_title</th>
      <th>revenue</th>
      <th>director</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3005</th>
      <td>2019-04-24</td>
      <td>復仇者聯盟：終局之戰</td>
      <td>2797800564</td>
      <td>Anthony Russo</td>
    </tr>
    <tr>
      <th>1339</th>
      <td>2009-12-10</td>
      <td>阿凡達</td>
      <td>2787965087</td>
      <td>James Cameron</td>
    </tr>
    <tr>
      <th>2418</th>
      <td>2015-12-15</td>
      <td>STAR WARS：原力覺醒</td>
      <td>2068223624</td>
      <td>J.J. Abrams</td>
    </tr>
    <tr>
      <th>2850</th>
      <td>2018-04-25</td>
      <td>復仇者聯盟3：無限之戰</td>
      <td>2046239637</td>
      <td>Anthony Russo</td>
    </tr>
    <tr>
      <th>2315</th>
      <td>2015-06-06</td>
      <td>侏羅紀世界</td>
      <td>1671713208</td>
      <td>Colin Trevorrow</td>
    </tr>
    <tr>
      <th>3032</th>
      <td>2019-07-12</td>
      <td>獅子王</td>
      <td>1656943394</td>
      <td>Jon Favreau</td>
    </tr>
    <tr>
      <th>1756</th>
      <td>2012-04-25</td>
      <td>復仇者聯盟</td>
      <td>1518815515</td>
      <td>Joss Whedon</td>
    </tr>
    <tr>
      <th>2287</th>
      <td>2015-04-01</td>
      <td>玩命關頭7</td>
      <td>1515047671</td>
      <td>James Wan</td>
    </tr>
    <tr>
      <th>3086</th>
      <td>2019-11-20</td>
      <td>冰雪奇緣2</td>
      <td>1450026933</td>
      <td>Chris Buck</td>
    </tr>
    <tr>
      <th>2298</th>
      <td>2015-04-22</td>
      <td>復仇者聯盟2：奧創紀元</td>
      <td>1405403694</td>
      <td>Joss Whedon</td>
    </tr>
    <tr>
      <th>2822</th>
      <td>2018-02-13</td>
      <td>黑豹</td>
      <td>1346739107</td>
      <td>Ryan Coogler</td>
    </tr>
    <tr>
      <th>1600</th>
      <td>2011-07-07</td>
      <td>哈利波特：死神的聖物 II</td>
      <td>1341511219</td>
      <td>David Yates</td>
    </tr>
    <tr>
      <th>2795</th>
      <td>2017-12-13</td>
      <td>STAR WARS：最後的絕地武士</td>
      <td>1332539889</td>
      <td>Rian Johnson</td>
    </tr>
    <tr>
      <th>2866</th>
      <td>2018-06-06</td>
      <td>侏羅紀世界：殞落國度</td>
      <td>1303459585</td>
      <td>J. A. Bayona</td>
    </tr>
    <tr>
      <th>2035</th>
      <td>2013-11-20</td>
      <td>冰雪奇緣</td>
      <td>1274219009</td>
      <td>Chris Buck</td>
    </tr>
    <tr>
      <th>2669</th>
      <td>2017-03-16</td>
      <td>美女與野獸</td>
      <td>1263521126</td>
      <td>Bill Condon</td>
    </tr>
    <tr>
      <th>2871</th>
      <td>2018-06-14</td>
      <td>超人特攻隊2</td>
      <td>1242805359</td>
      <td>Brad Bird</td>
    </tr>
    <tr>
      <th>2681</th>
      <td>2017-04-12</td>
      <td>玩命關頭8</td>
      <td>1238764765</td>
      <td>F. Gary Gray</td>
    </tr>
    <tr>
      <th>1915</th>
      <td>2013-04-18</td>
      <td>鋼鐵人 3</td>
      <td>1214811252</td>
      <td>Shane Black</td>
    </tr>
    <tr>
      <th>2318</th>
      <td>2015-06-17</td>
      <td>小小兵</td>
      <td>1156730962</td>
      <td>Kyle Balda</td>
    </tr>
  </tbody>
</table>
</div>




```python
rev_outlier = mgt2001.des.outlier(movie_df['revenue'].dropna(), show=False)[0] # [:20]
roi_outlier = mgt2001.des.outlier(movie_df['ROI'].dropna(), show=False)[0] # [:5]
budget_outlier = mgt2001.des.outlier(movie_df['budget'].dropna(), show=False)[0] # [:5]

def filter_rows_by_values(df, col, values):
    return df[df[col].isin(values) == False]

rev_df = movie_df[movie_df['revenue'] >= 1e5 * 9] # 排除 90 萬以下票房的資料點（這些點沒有被移除）
rev_df = filter_rows_by_values(rev_df, 'revenue', rev_outlier).reset_index(drop=True)
roi_df = filter_rows_by_values(movie_df, 'ROI', roi_outlier).reset_index(drop=True)
budget_df = filter_rows_by_values(movie_df, 'budget', budget_outlier).reset_index(drop=True)

u_movie_df = movie_df[movie_df['revenue'] >= 1e5 * 9] # 排除 90 萬以下票房的資料點（這些點沒有被移除）
u_movie_df = filter_rows_by_values(u_movie_df, 'revenue', rev_outlier).reset_index(drop=True)
u_movie_df = filter_rows_by_values(u_movie_df, 'ROI', roi_outlier).reset_index(drop=True)
u_movie_df = filter_rows_by_values(u_movie_df, 'budget', budget_outlier).reset_index(drop=True)

print(u_movie_df.info()) 

# Plot
fig = plt.figure(figsize=(9, 3))
row, col = 1, 3
fig.subplots_adjust(hspace=0.2, wspace=.5)
ax = fig.add_subplot(row, col, 1)
ax = sns.boxplot(y=u_movie_df['revenue']) # orient='h' results in horizontal boxplot
plt.title('Revenue')
ax.grid(True)
ax = fig.add_subplot(row, col, 2)
ax = sns.boxplot(y=u_movie_df['ROI']) # orient='h' results in horizontal boxplot
plt.title('ROI')
ax.grid(True)

ax = fig.add_subplot(row, col, 3)
ax = sns.boxplot(y=u_movie_df['budget']) # orient='h' results in horizontal boxplot
plt.title('budget')
ax.grid(True)


plt.show()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2248 entries, 0 to 2247
    Data columns (total 33 columns):
     #   Column                 Non-Null Count  Dtype         
    ---  ------                 --------------  -----         
     0   id                     2248 non-null   int64         
     1   title                  2248 non-null   object        
     2   budget                 2248 non-null   int64         
     3   genres                 2248 non-null   object        
     4   original_language      2248 non-null   object        
     5   production_companies   2248 non-null   object        
     6   release_date           2248 non-null   datetime64[ns]
     7   TW_release_date        500 non-null    object        
     8   revenue                2248 non-null   int64         
     9   runtime                2248 non-null   int64         
     10  cast                   2248 non-null   object        
     11  cast_cnt               2248 non-null   int64         
     12  crew_cnt               2248 non-null   int64         
     13  female_cast_cnt        2248 non-null   int64         
     14  male_cast_cnt          2248 non-null   int64         
     15  cast_popularity_ave    2237 non-null   float64       
     16  director               2247 non-null   object        
     17  direcotr_gender        2247 non-null   float64       
     18  TMDB_score             2248 non-null   float64       
     19  TMDB_vote_count        2248 non-null   int64         
     20  profit                 2248 non-null   int64         
     21  ROI                    2248 non-null   float64       
     22  rotten_score           1921 non-null   float64       
     23  rating                 1880 non-null   object        
     24  rotten_aud_score       1921 non-null   float64       
     25  zh_title               1848 non-null   object        
     26  belongs_to_collection  486 non-null    object        
     27  has_homepage           2248 non-null   int64         
     28  has_collection         2248 non-null   int64         
     29  pre_covid              2248 non-null   int64         
     30  post_covid             2248 non-null   int64         
     31  release_year           2248 non-null   int64         
     32  release_month          2248 non-null   int64         
    dtypes: datetime64[ns](1), float64(6), int64(16), object(10)
    memory usage: 579.7+ KB
    None



![png](output_12_1.png)



```python
u_movie_df.sort_values(by='revenue', ascending=False).head(5)[['release_date', 'title', 'zh_title', 'revenue', 'director', 'release_month']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_date</th>
      <th>title</th>
      <th>zh_title</th>
      <th>revenue</th>
      <th>director</th>
      <th>release_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1655</th>
      <td>2014-12-17</td>
      <td>Night at the Museum: Secret of the Tomb</td>
      <td>博物館驚魂夜3</td>
      <td>363204635</td>
      <td>Shawn Levy</td>
      <td>12</td>
    </tr>
    <tr>
      <th>942</th>
      <td>2009-04-02</td>
      <td>Fast &amp; Furious</td>
      <td>玩命關頭4</td>
      <td>363164265</td>
      <td>Justin Lin</td>
      <td>4</td>
    </tr>
    <tr>
      <th>422</th>
      <td>2004-12-09</td>
      <td>Ocean's Twelve</td>
      <td>瞞天過海2：長驅直入</td>
      <td>362744280</td>
      <td>Steven Soderbergh</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1554</th>
      <td>2014-03-07</td>
      <td>Noah</td>
      <td>挪亞方舟</td>
      <td>362637473</td>
      <td>Darren Aronofsky</td>
      <td>3</td>
    </tr>
    <tr>
      <th>118</th>
      <td>2001-07-25</td>
      <td>Planet of the Apes</td>
      <td>決戰猩球</td>
      <td>362211740</td>
      <td>Tim Burton</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))
fig.subplots_adjust(hspace=0.3, wspace=0.4)
u_movie_df.set_index('release_date').resample('M').agg(dict(revenue='mean')).to_period('M').plot(ax=axes[0])
u_movie_df.set_index('release_date').resample('M').agg(dict(ROI='mean')).to_period('M').plot(ax=axes[1])
u_movie_df.set_index('release_date').resample('M').agg(dict(budget='mean')).to_period('M').plot(ax=axes[2])
plt.show()
```


![png](output_14_0.png)


雖然這明顯地去除掉許多 outliers，但我們可以發現一件事：**去掉 outliers 後，可以看到以前的電影表現比較平均一點，越後期的電影看起來只有少數賣座電影在撐場而已**，最高的是博物館驚魂夜3，其次是玩命關頭系列的玩命關頭4。前十名的電影裡面，幾乎都是一些老牌電影（2012 前上映）。整體收入平均也有明顯的下降趨勢。當然，這對在 2020 和 2021 之間上映的電影來說非常不公平。

所以我們最後只去除前 20 個 outliers 以防止這種一年不如一年的情況發生。


```python
rev_outlier = sorted(mgt2001.des.outlier(movie_df['revenue'].dropna(), show=False)[0], reverse=True)[:20]
roi_outlier = sorted(mgt2001.des.outlier(movie_df['ROI'].dropna(), show=False)[0], reverse=True)[:5]
budget_outlier = sorted(mgt2001.des.outlier(movie_df['budget'].dropna(), show=False)[0], reverse=True)[:5]
                        
def filter_rows_by_values(df, col, values):
    return df[df[col].isin(values) == False]

rev_df = movie_df[movie_df['revenue'] >= 1e5 * 9] # 排除 90 萬以下票房的資料點（這些點沒有被移除）
rev_df = filter_rows_by_values(rev_df, 'revenue', rev_outlier).reset_index(drop=True)
roi_df = filter_rows_by_values(movie_df, 'ROI', roi_outlier).reset_index(drop=True)
budget_df = filter_rows_by_values(movie_df, 'budget', budget_outlier).reset_index(drop=True)

u_movie_df = movie_df[movie_df['revenue'] >= 1e5 * 9] # 排除 90 萬以下票房的資料點（這些點沒有被移除）
u_movie_df = filter_rows_by_values(u_movie_df, 'revenue', rev_outlier).reset_index(drop=True)
u_movie_df = filter_rows_by_values(u_movie_df, 'ROI', roi_outlier).reset_index(drop=True)
u_movie_df = filter_rows_by_values(u_movie_df, 'budget', budget_outlier).reset_index(drop=True)

print(u_movie_df.info()) 

# Plot
fig = plt.figure(figsize=(9, 3))
row, col = 1, 3
fig.subplots_adjust(hspace=0.2, wspace=.5)
ax = fig.add_subplot(row, col, 1)
ax = sns.boxplot(y=u_movie_df['revenue']) # orient='h' results in horizontal boxplot
plt.title('Revenue')
ax.grid(True)
ax = fig.add_subplot(row, col, 2)
ax = sns.boxplot(y=u_movie_df['ROI']) # orient='h' results in horizontal boxplot
plt.title('ROI')
ax.grid(True)

ax = fig.add_subplot(row, col, 3)
ax = sns.boxplot(y=u_movie_df['budget']) # orient='h' results in horizontal boxplot
plt.title('budget')
ax.grid(True)

plt.show()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2788 entries, 0 to 2787
    Data columns (total 33 columns):
     #   Column                 Non-Null Count  Dtype         
    ---  ------                 --------------  -----         
     0   id                     2788 non-null   int64         
     1   title                  2788 non-null   object        
     2   budget                 2788 non-null   int64         
     3   genres                 2788 non-null   object        
     4   original_language      2788 non-null   object        
     5   production_companies   2788 non-null   object        
     6   release_date           2788 non-null   datetime64[ns]
     7   TW_release_date        762 non-null    object        
     8   revenue                2788 non-null   int64         
     9   runtime                2788 non-null   int64         
     10  cast                   2788 non-null   object        
     11  cast_cnt               2788 non-null   int64         
     12  crew_cnt               2788 non-null   int64         
     13  female_cast_cnt        2788 non-null   int64         
     14  male_cast_cnt          2788 non-null   int64         
     15  cast_popularity_ave    2775 non-null   float64       
     16  director               2787 non-null   object        
     17  direcotr_gender        2787 non-null   float64       
     18  TMDB_score             2788 non-null   float64       
     19  TMDB_vote_count        2788 non-null   int64         
     20  profit                 2788 non-null   int64         
     21  ROI                    2788 non-null   float64       
     22  rotten_score           2411 non-null   float64       
     23  rating                 2361 non-null   object        
     24  rotten_aud_score       2410 non-null   float64       
     25  zh_title               2360 non-null   object        
     26  belongs_to_collection  789 non-null    object        
     27  has_homepage           2788 non-null   int64         
     28  has_collection         2788 non-null   int64         
     29  pre_covid              2788 non-null   int64         
     30  post_covid             2788 non-null   int64         
     31  release_year           2788 non-null   int64         
     32  release_month          2788 non-null   int64         
    dtypes: datetime64[ns](1), float64(6), int64(16), object(10)
    memory usage: 718.9+ KB
    None



![png](output_16_1.png)



```python
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))
fig.subplots_adjust(hspace=0.3, wspace=0.4)
u_movie_df.set_index('release_date').resample('M').agg(dict(revenue='mean')).to_period('M').plot(ax=axes[0])
u_movie_df.set_index('release_date').resample('M').agg(dict(ROI='mean')).to_period('M').plot(ax=axes[1])
u_movie_df.set_index('release_date').resample('M').agg(dict(budget='mean')).to_period('M').plot(ax=axes[2])
plt.show()
```


![png](output_17_0.png)


我們可以看到，用 20-5-5 去除掉 outliers 後，結果不僅較為合理，也幫我們去除掉了非常大、不合理的數字。因此我們便用剩下的 2788 筆資料進行更近一步的分析。另外，在這邊也要注意到，不是所有的 column 都是 2788 筆資料，有些 data 是有少的。所以在做分析時要格外小心。


```python
u_movie_df['log_revenue'] = np.log1p(u_movie_df['revenue'])
u_movie_df['log_budget'] = np.log1p(u_movie_df['budget'])
u_movie_df['log_ROI'] = np.log1p(u_movie_df['ROI'])

# 年份以及月份
u_movie_df['release_month'] = u_movie_df['release_date'].apply(lambda x: x.month)
u_movie_df['release_year'] = u_movie_df['release_date'].apply(lambda x: x.year)
```


```python
u_movie_df.sort_values(by='revenue', ascending=False).head(20)[['release_date', 'title', 'zh_title', 'revenue', 'director', 'release_month']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_date</th>
      <th>title</th>
      <th>zh_title</th>
      <th>revenue</th>
      <th>director</th>
      <th>release_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2220</th>
      <td>2016-04-27</td>
      <td>Captain America: Civil War</td>
      <td>美國隊長3：英雄內戰</td>
      <td>1153296293</td>
      <td>Anthony Russo</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2618</th>
      <td>2018-12-07</td>
      <td>Aquaman</td>
      <td>水行俠</td>
      <td>1148461807</td>
      <td>James Wan</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2680</th>
      <td>2019-06-28</td>
      <td>Spider-Man: Far From Home</td>
      <td>蜘蛛人：離家日</td>
      <td>1131927996</td>
      <td>Jon Watts</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2646</th>
      <td>2019-03-06</td>
      <td>Captain Marvel</td>
      <td>驚奇隊長</td>
      <td>1128276090</td>
      <td>Ryan Fleck</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>2011-06-28</td>
      <td>Transformers: Dark of the Moon</td>
      <td>變形金剛3：黑月降臨</td>
      <td>1123794079</td>
      <td>Michael Bay</td>
      <td>6</td>
    </tr>
    <tr>
      <th>384</th>
      <td>2003-12-01</td>
      <td>The Lord of the Rings: The Return of the King</td>
      <td>魔戒三部曲：王者再臨</td>
      <td>1118888979</td>
      <td>Peter Jackson</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1664</th>
      <td>2012-10-25</td>
      <td>Skyfall</td>
      <td>007：空降危機</td>
      <td>1108561013</td>
      <td>Sam Mendes</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1616</th>
      <td>2012-07-16</td>
      <td>The Dark Knight Rises</td>
      <td>黑暗騎士：黎明昇起</td>
      <td>1081041287</td>
      <td>Christopher Nolan</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2705</th>
      <td>2019-10-02</td>
      <td>Joker</td>
      <td>小丑</td>
      <td>1074251311</td>
      <td>Todd Phillips</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2734</th>
      <td>2019-12-18</td>
      <td>Star Wars: The Rise of Skywalker</td>
      <td>STAR WARS：天行者的崛起</td>
      <td>1074144248</td>
      <td>J.J. Abrams</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2676</th>
      <td>2019-06-19</td>
      <td>Toy Story 4</td>
      <td>玩具總動員4</td>
      <td>1073394593</td>
      <td>Josh Cooley</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1291</th>
      <td>2010-06-16</td>
      <td>Toy Story 3</td>
      <td>玩具總動員3</td>
      <td>1066969703</td>
      <td>Lee Unkrich</td>
      <td>6</td>
    </tr>
    <tr>
      <th>714</th>
      <td>2006-07-06</td>
      <td>Pirates of the Caribbean: Dead Man's Chest</td>
      <td>神鬼奇航2：加勒比海盜</td>
      <td>1065659812</td>
      <td>Gore Verbinski</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2334</th>
      <td>2016-12-14</td>
      <td>Rogue One: A Star Wars Story</td>
      <td>星際大戰外傳：俠盜一號</td>
      <td>1056057273</td>
      <td>Gareth Edwards</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2666</th>
      <td>2019-05-22</td>
      <td>Aladdin</td>
      <td>阿拉丁</td>
      <td>1047612394</td>
      <td>Guy Ritchie</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2408</th>
      <td>2017-06-15</td>
      <td>Despicable Me 3</td>
      <td>神偷奶爸3</td>
      <td>1031552585</td>
      <td>Kyle Balda</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2245</th>
      <td>2016-06-16</td>
      <td>Finding Dory</td>
      <td>海底總動員2：多莉去哪兒</td>
      <td>1028570889</td>
      <td>Andrew Stanton</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1247</th>
      <td>2010-03-03</td>
      <td>Alice in Wonderland</td>
      <td>魔境夢遊</td>
      <td>1025467110</td>
      <td>Tim Burton</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2188</th>
      <td>2016-02-11</td>
      <td>Zootopia</td>
      <td>動物方城市</td>
      <td>1023784195</td>
      <td>Byron Howard</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1673</th>
      <td>2012-11-26</td>
      <td>The Hobbit: An Unexpected Journey</td>
      <td>哈比人：意外旅程</td>
      <td>1021103568</td>
      <td>Peter Jackson</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
u_movie_df[['log_revenue', 'log_budget', 'log_ROI']].hist()
plt.show()
```


![png](output_21_0.png)
