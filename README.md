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
+ 資料處理
+ 資料分析
  + 票房分析
    + 一、疫情前後的票房差異
    + 二、票房與投入成本的關係
    + 三、票房與參演者的關係 - 男女演員的多寡會不會影響票房
    + 四、評分網站的差異：
      + 1. 影評人與大眾評分差異比較：
      + 2.不同平台間觀眾評分比較: TMDb vs Rotten Tomato
      + 3. 觀眾評分與電影類別的關係
    + 五、票房與原始語言的關係
    + 六、票房與電影級數的關係
    + 七、票房與上映時間的關係
      + 1. 寒暑假比較多電影？
      + 2. 過年大片是不是真的比較夯？
      + 3. 夏天的電影比較熱門？
    + 八、票房預測
      + 如果去掉 Outliers 的結果會如何？
  + 電影的賺錢程度 - ROI 與票房的關係





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

## Findings

+ **票房分析**
    + **一、疫情前後的票房差異**：2020年第四季的票房仍然受到疫情影響，但相比2020第三季的票房已有好轉。
    + **二、票房與投入成本的關係**：投入成本與票房相關，投入成本越高，票房著實越高。
    + **三、票房與參演者的關係 - 男女演員的多寡會不會影響票房**：女演員數量大於男演員數量時，票房較高。
    + **四、評分網站的差異：**
        + **1. 影評人與大眾評分差異比較：**：專業影評人的評分與觀眾有很大的差距。
        + **2.不同平台間觀眾評分比較: TMDb vs Rotten Tomato**：不同平台上的觀眾評分也不大相同。
        + **3. 觀眾評分與電影類別的關係**：若電影類別為 Drama 或 Animation，可預測其能獲得較高觀眾評分。
    + **五、票房與原始語言的關係**：原始語言為英語的電影票房較西班牙語、法語、義大利語好，但因資料中幾乎為英語片、且筆數差異懸殊，所以意義不大。
    + **六、票房與電影級數的關係**：G 和 PG 的票房差不多，大於 PG-13，R 的票房為最低。可以進一步推測電影票房和能觀看該電影的客群範圍大小有關。
    + **七、票房與上映時間的關係**
        + **1. 寒暑假比較多電影？**：寒暑假（12、7、8月）並沒有比較多電影上映
        + **2. 過年大片是不是真的比較夯？**：聖誕節所上映的片子確實較剩餘年度的票房要高。
        + **3. 夏天的電影比較熱門？**：夏天的電影確實比較熱門，此結果也與我們預期的相符。但實際上因為冬季中，一、二月的票房表現較不好，所以在四季的票房排名上掉到第三。
    + **八、票房預測**：雖然 Multiple Regression Model 的解釋力蠻高的（$R^2 = 0.816$）且模型的有效性也破足夠（$p$-value $= 0.0000$），預測的結果不太理想，標準差過大。可能票房本來就有一定的隨機性存在。
+ **電影的賺錢程度 - ROI 與票房的關係**：票房高的電影並不代表有較高的 ROI。

## Credits

We have to give credits to our friends at IM department for making the project possible. Many thanks to @gary1030, @Daedluz, @derekdylu, and @christine891225.