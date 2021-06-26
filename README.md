<h1 align='center'>
<br>
<img src="https://gist.githubusercontent.com/icheft/caa4b43f0f3393ae32dc9d82d6bbce01/raw/63b61f680033999ef788ebebeb4cd8e146fb416e/favpng_film-cinema-video.png" alt="pws" width="200">
<br>
 GenEdu 5010 Final Project
</h1>
<h3 align="center">IM in Love with Movies 🎥</h3>
<div align="center">
  <a href="https://icheft.github.io/IM-in-Love-with-Movies/">
    <img src="https://img.shields.io/badge/GenEdu 5010-網頁版請點此-orange?style=for-the-badge&logo=python">
  </a>
</div>
<h5 align="center">
B07705031 陳立軒 資管二 • 
B08705028 葉柏辰 資管二 <br>
B08705027 林暐倫 資管二 • 
B08705003 楊佳芊 資管二 <br>
</h5>

\* 最終成果用網頁版看可能會比較合適！




## Outline
+ [資料處理](#資料處理)
+ [資料分析](#資料分析)
  + [票房分析](#票房分析)
    + [一、疫情前後的票房差異](#一疫情前後的票房差異)
    + [二、票房與投入成本的關係](#二票房與投入成本的關係)
    + [三、票房與參演者的關係 - 男女演員的多寡會不會影響票房](#三票房與參演者的關係---男女演員的多寡會不會影響票房)
    + [四、評分網站的差異：](#四評分網站的差異)
      + [1. 影評人與大眾評分差異比較：](#1-影評人與大眾評分差異比較)
      + [2.不同平台間觀眾評分比較: TMDb vs Rotten Tomato](#2不同平台間觀眾評分比較-tmdb-vs-rotten-tomato)
      + [3. 觀眾評分與電影類別的關係](#3-觀眾評分與電影類別的關係)
    + [五、票房與原始語言的關係](#五票房與原始語言的關係)
    + [六、票房與電影級數的關係](#六票房與電影級數的關係)
    + [七、票房與上映時間的關係](#七票房與上映時間的關係)
      + [1. 寒暑假比較多電影？](#1-寒暑假比較多電影)
      + [2. 過年大片是不是真的比較夯？](#2-過年大片是不是真的比較夯)
      + [3. 夏天的電影比較熱門？](#3-夏天的電影比較熱門)
    + [八、票房預測](#八票房預測)
      + [如果去掉 Outliers 的結果會如何？](#如果去掉-outliers-的結果會如何)
  + [電影的賺錢程度 - ROI 與票房的關係](#電影的賺錢程度---roi-與票房的關係)





## Skill Sets

+ Data Collection
    + [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction) and 3rd Party Python Library [tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)
    + Scraping from Rotten Tomatoes using BeautifulSoup to parse HTML documents with a little help from another [Python package](https://github.com/pdrm83/rotten_tomatoes_scraper) that is made to do this job
    + Pandas and Numpy: for storing and exporting the data fetched from the Internet
    + Outdated

        Originally, we try to scrape all the data from Taiwan Film & Audiovisual Institute to see if the data is useful for the analysis.

        The work is done using `wget` to download the Excel file and `BeautifulSoup` to locate the URL. 
+ Visualization
    + matplotlib
    + seaborn
    + ~~Dash (an extension of Plotly)~~
    + ~~Plotly~~
+ Data Analysis
    + mgt2001 ([documentation](https://icheft.github.io/mgt2001-docs/) and [repo](https://github.com/icheft/mgt2001/)): a little python package @icheft made for his statistic course. Since we are heavily using the concept we learned from our statistics class, we manage to make good use of it. 
    + Pandas and Numpy are again used
    + [SciPy](https://www.scipy.org) are [statsmodels](https://www.statsmodels.org/stable/index.html) are two main packages that are used to test the hypotheses 


## Credits

We have to give credits to our friends at IM department for making the project possible. Many thanks to @gary1030, @Daedluz, @derekdylu, and @christine891225.