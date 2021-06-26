<center>
<img src="https://gist.githubusercontent.com/icheft/caa4b43f0f3393ae32dc9d82d6bbce01/raw/63b61f680033999ef788ebebeb4cd8e146fb416e/favpng_film-cinema-video.png" alt="pws-project-logo" width="200">
<br>
<h1 align='center'>
GenEdu 5010 Final Project
</h1>
<h3 align="center">IM in Love with Movies 🍿</h3>
<div align="center">
  <a href="https://icheft.github.io/IM-in-Love-with-Movies/slides.pdf" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Slides-簡報請點此-B7472A?style=for-the-badge&logo=Microsoft PowerPoint">
  </a>
</div>
<h5 align="center">
B07705031 陳立軒 資管二 • 
B08705028 葉柏辰 資管二 <br>
B08705027 林暐倫 資管二 • 
B08705003 楊佳芊 資管二 <br>
</h5>
</center>


+ [簡介](#)
    + [動機](#_1)
    + [Packages 介紹](#packages)
+ [資料收集](data_collection/#_1)
    + [1. 收集電影 ID](data_collection/#1-id)
    + [2. 收集個別電影詳細資訊](data_collection/#2)
+ [資料處理](data-processing/#_1)
+ [資料分析](data-analysis/#_1)
    + [票房分析](data-analysis/#_2)
        + [一、疫情前後的票房差異](data-analysis/#_3)
        + [二、票房與投入成本的關係](data-analysis/#_4)
        + [三、票房與參演者的關係 - 男女演員的多寡會不會影響票房](data-analysis/#-)
        + [四、評分網站的差異：](data-analysis/#_5)
            + [1. 影評人與大眾評分差異比較：](data-analysis/#1)
            + [2.不同平台間觀眾評分比較: TMDb vs Rotten Tomatoes](data-analysis/#2-tmdb-vs-rotten-tomatoes)
            + [3. 觀眾評分與電影類別的關係](data-analysis/#3)
        + [五、票房與原始語言的關係](data-analysis/#_6)
        + [六、票房與電影級數的關係](data-analysis/#_7)
        + [七、票房與上映時間的關係](data-analysis/#_8)
            + [1. 寒暑假比較多電影？](data-analysis/#1_1)
            + [2. 過年大片是不是真的比較夯？](data-analysis/#2)
            + [3. 夏天的電影比較熱門？](data-analysis/#3_1)
        + [八、票房預測](data-analysis/#_9)
            + [如果去掉 Outliers 的結果會如何？](data-analysis/#outliers)
    + [電影的賺錢程度 - ROI 與票房的關係](data-analysis/#-roi)
+ [結論](conclusion/#_1)
    + [懶人包](conclusion/#_2)
    + [外來展望](conclusion/#_3)

### 動機

首先，在疫情期間，或許很多人第一時間都會想到和疫情有關的主題，因此我們想尋找其他有趣的方向作為專案主題。而我們會選擇現在這個主題是因為我們組員中有電影的愛好者，平時就十分關注電影相關資訊。

因此我們想利用這個機會，應用在課堂上學到的爬蟲和其他 Python 技巧，加上我們在統計課程中學到的知識，用程式幫助我們分析電影產業的現況。

### Packages 介紹

此部分用英文解釋比較順一點，所以：

+ Data Collection
    + [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction) and 3rd Party Python Library [tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)
    + Scraping from Rotten Tomatoes using BeautifulSoup to parse HTML documents with a little help from another [Python package](https://github.com/pdrm83/rotten_tomatoes_scraper) that is made to do this job
    + Pandas and Numpy: for storing and exporting the data fetched from the Internet
+ Visualization
    + matplotlib
    + seaborn
    + ~~Dash (an extension of Plotly)~~
    + ~~Plotly~~
+ Data Analysis
    + mgt2001 ([documentation](https://icheft.github.io/mgt2001-docs/) and [repo](https://github.com/icheft/mgt2001/)): a little python package @icheft made for his statistic course. Since we are heavily using the concept we learned from our statistics class, we manage to make good use of it. 
    + Pandas and Numpy are again used
    + [SciPy](https://www.scipy.org) are [statsmodels](https://www.statsmodels.org/stable/index.html) are two main packages that are used to test the hypotheses 

