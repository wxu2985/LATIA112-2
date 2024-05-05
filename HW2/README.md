requirements:
pip install pandas
pip install selenium
pip install webdriver_manager
pip install beautifulsoup4
pip install requests

/h1使用requests
main_requests.py 為執行檔案，requests_books.csv為爬取的內容。

/h1使用selenium
main_selenium.py 為執行檔案，Chromedriver是符合我本地的chrome driver，如需執行，請更改成自己的版本，selenium_books.csv為爬取的內容。

爬取網頁:博客來網站搜尋(程式)
url:https://search.books.com.tw/search/query/key/%E7%A8%8B%E5%BC%8F/cat/all
爬取內容
書名
語言
作者
價格
書的圖片
