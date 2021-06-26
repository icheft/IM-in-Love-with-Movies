# 資料收集

為了整篇分析報告的完整性，這邊我們使用另外的檔案進行抓取。

簡單來說，收集的過程可以分為兩個步驟：

1. 收集電影 ID
2. 收集個別電影詳細資訊

## 1. 收集電影 ID

主要程式碼如下。我們透過 `tmdbv3api` 的 `Discover()` class 搜尋符合條件的資料（在這邊是設定從 2000 年到 2021 年的電影，其中粉絲評分數要超過 400 則）。

程式碼裡頭的 `tqdm` 則是幫助我們在 Terminal 看得到進度條的工具。

```python
discover = Discover()
vote_bound = 400  # 只抓 400 票觀眾投票以上的
movie = []
for year in tqdm(range(2000, 2022)):
    page = 1
    try:
        while True and page <= 1000:  # 1000 是頁數上限
            new_movie = discover.discover_movies({
                'primary_release_year': year,
                'vote_count.gte': vote_bound,
                'sort_by': 'primary_release_date.desc',
                'page': page
            })
            if len(new_movie) > 0:
                movie += new_movie
                page += 1
            else:
                break
    except:
        # 萬一不小心超出該年的 page 上限
        continue


movie_id = [m.id for m in movie]
```

## 2. 收集個別電影詳細資訊

接下來再透過 `tmdbv3api` 的 `Movie()` class 收集個別電影 ID 的相對應資訊。

我們會搜集的資訊如下：

> *括號內為變數名稱。

* 預算 (budget)
* 類別（genres）
* 語言（original_language）
* 製片公司（production_companies）
* 美國上映時間（release_date）
* 全球票房收入（revenue）
* 電影獲利（profit）
* ROI（ROI）
* 電影時長（runtime）
* 電影原文名稱（title）
* 電影中文名稱（zh_title）
* 有無電影續集 (has_collection)
* 電影續集名稱（belongs_to_collection）
* 有無官方首頁 (has_homepage)
* 演員數量（cast_cnt）：因為演員數量實在太多，我們最後將演員受歡迎度不到 2 的人剔除。
    * 男演員數量（male_cast_cnt）
    * 女演員數量（female_cast_cnt）
* 演員平均受歡迎度（cast_popularity_ave）
* 導演（director）
* 導演性別（direcotr_gender）
* 工作人員數量（crew_cnt）
* 影評評分 (rotten_score)：爛番茄評分。此項評分標準為「The percentage of Approved Tomatometer Critics who have given this movie a positive review.」
* 觀眾評分（rotten_aud_score）：加入觀眾評分，來取代原本 TMDb 所提供的資料。此項評分標準為「The percentage of users who rated this 3.5 stars or higher.」


<div class="alert alert-block alert-info"><b>說明：</b>最後因為人手與時間的關係，並不是所有欄位都有用到，這也是為什麼我們後續會想要再進一步查看更多變數以及電影間的關係的原因。</div>

程式碼如下：

```python
movie_df = pd.DataFrame(columns=col_names)

for ID in tqdm(movie_id):
    movie_obj = Movie()
    m = movie_obj.details(ID)
    data_row = dict()
    data_row['id'] = m.id
    data_row['title'] = m.title
    data_row['budget'] = m.budget

    gen = [g['name'] for g in m.genres]
    data_row['genres'] = gen

    data_row['original_language'] = m.original_language

    pcs = [pc['name'] for pc in m.production_companies]
    data_row['production_companies'] = pcs

    data_row['release_date'] = m.release_date

    if m['homepage'] != "":
        data_row['has_homepage'] = 1
    else:
        data_row['has_homepage'] = 0

    TW_release_date_flag = False
    for loc in m.release_dates['results']:
        for key, value in loc.items():
            if value == 'TW':
                TW_release_date_flag = True
                data_row['TW_release_date'] = loc['release_dates'][0]['release_date']
            else:
                continue
    if not TW_release_date_flag:
        data_row['TW_release_date'] = np.nan

    try:
        belongs_to_collection = m['belongs_to_collection']['name']
        data_row['belongs_to_collection'] = belongs_to_collection
    except:
        data_row['belongs_to_collection'] = np.nan

    data_row['revenue'] = m.revenue
    data_row['runtime'] = m.runtime

    pop_bound = 2
    cn = [c['name']
          for c in m.casts['cast'] if c['popularity'] >= pop_bound]
    data_row['cast'] = cn
    data_row['cast_cnt'], data_row['crew_cnt'] = len([c for c in movie_obj.credits(ID)[
        'cast'] if c['popularity'] >= pop_bound and c['gender'] != 0 and c['gender'] != 3]), len(movie_obj.credits(ID)['crew'])
    data_row['female_cast_cnt'] = len(
        [c['gender'] for c in m.casts['cast'] if c['gender'] == 1 and c['popularity'] >= pop_bound])
    data_row['male_cast_cnt'] = len(
        [c['gender'] for c in m.casts['cast'] if c['gender'] == 2 and c['popularity'] >= pop_bound])
    data_row['cast_popularity_ave'] = np.mean(
        [c['popularity'] for c in m.casts['cast'] if c['popularity'] >= pop_bound])
    try:
        data_row['director'] = [c['name']
                                for c in movie_obj.credits(ID)['crew'] if c['job'] == 'Director'][0]
        data_row['direcotr_gender'] = [c['gender']
                                       for c in movie_obj.credits(ID)['crew'] if c['job'] == 'Director'][0]
    except:
        data_row['director'] = np.nan
        data_row['direcotr_gender'] = np.nan

    data_row['TMDB_score'] = m.vote_average
    data_row['TMDB_vote_count'] = m.vote_count

    data_row['profit'] = data_row['revenue'] - data_row['budget']

    try:
        data_row['ROI'] = data_row['profit'] / data_row['budget']
    except:
        continue

    try:
        # 爛番茄爬蟲
        year = datetime.strptime(data_row['release_date'], '%Y-%m-%d').year
        movie_scraper = MovieScraper(movie_title=m.title, year=year)
        movie_scraper.extract_metadata()
        data_row['rotten_score'] = float(
            movie_scraper.metadata['Score_Rotten'])
        data_row['rotten_aud_score'] = float(
            movie_scraper.metadata['Score_Audience'])
        data_row['rating'] = movie_scraper.metadata['Rating']
    except:
        data_row['rotten_score'] = np.nan
        data_row['rating'] = np.nan
        data_row['rotten_aud_score'] = np.nan

    # zh_title
    zh_title_flag = False
    for loc in m.translations['translations']:
        for key, value in loc.items():
            if value == 'TW':
                data_row['zh_title'] = loc['data']['title']
                zh_title_flag = True
                break
            else:
                continue
    if not zh_title_flag:
        data_row['zh_title'] = np.nan

    movie_df = movie_df.append(data_row, ignore_index=True)
    
movie_df = movie_df.sort_values(by='release_date')
movie_df.to_excel('../data/sorted_all_movie.xlsx')
```
