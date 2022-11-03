# resend_pec_mail
## 大量重寄醫事人員教補系統測試信

本程式主要是重寄台灣醫事人員教補系統問卷

相信各職類的教學負責人應該都會有這個困擾，每年10月要處理教補系統指標，老師學生換來換去，也不知道他們提供的mail是不是正確的，這個程式就是利用爬蟲的方式，快速批次寄出測試信或是重寄帳號密碼信件

教補系統的網站
https://pec.mohw.gov.tw/MONITOR_INDICATOR/Monitor_Questionnaire.aspx

https://medium.com/drunk-wis/python-selenium-chrome-browser-%E8%88%87-driver-%E6%83%B1%E4%BA%BA%E7%9A%84%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-cbaf1d1861ce
裡面有用到一個自動更新chrome driver的功能，是參考這個網站達成的，感謝他解決這個難搞的瀏覽器版本問題

### 使用說明
1. 需要安裝的函式庫在第二列
2. 老師或學生資料再file/教補問卷名單.xlsx裡面維護，我的名單來源是乾淨的，所以沒有在裡面做防呆
3. 裡面就兩個功能，基本上是一樣的，只是差在最後點哪一個按鈕
