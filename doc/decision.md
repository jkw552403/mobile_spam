1. 抓PTT MobileComm的文章(時間至少兩天前，為了等推文推完全)
將文章內文跟推文存成sqlite的兩張表，如MobileCommArtilce, MobileCommComment。
    * 命名為ptt.db放在data底下
    * 使用Beautifulsoup抽取各attribute。
    * 處理推文時間或者不存時間
2. 抓eprice的手機列表 將品牌跟手機型號做對應
存成json，放在res/底下。
3. 掃過內文標題以及推文的內容，將型號換成品牌，再統計user提到品牌的次數。
    * 全部資訊換小寫
    
4. Others
    * 呈現成果
    * 品牌熱度
    * 帳號出現點
