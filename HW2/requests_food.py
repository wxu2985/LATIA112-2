import requests
import pandas as pd
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 設定目標網址
    url = "https://online.carrefour.com.tw/zh/%E9%A3%B2%E6%96%99%E9%9B%B6%E9%A3%9F"

    # 發送 HTTP 請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 確保正確的編碼

    # 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有 'card class 的 div 標籤
    items = soup.find_all('div', class_='hot-recommend-item line')
    index = 1
    data = []

   

    # 遍歷每個項目，爬取需要的資訊
    for item in items:
        try:
            
            commodity = item.find('div',class_="commodity-desc").find('a').get_text(strip=True)  # 獲取商品名稱
            quantity = item.find('div',class_="box-img").find('span').text.strip() # 獲取商品數量
            price = item.find('div',class_="commodity-operation").find('div',class_="current-price").find('em').text.strip()# 獲取商品價格
            remark = item.find('div',class_="little-label").find('span').text.strip() # 獲取商品備註
            image_url = item.find('div', class_='box-img').find('img')['src']# 獲取商品圖片 URL

            # 將資料存儲到字典中
            temp_data = {
                "飲料零食": commodity,
                "數量" : quantity,
                "價錢" : price,
                "備註" : remark,
                "Image URL": image_url
            }
            data.append(temp_data)

             # 輸出商品資訊到終端機
            print(f"----- 家樂福 {index} -----")
            print(f"飲料零食: {commodity}")
            print(f"數量: {quantity}")
            print(f"價錢: {price}")
            print(f"備註: {remark}")
            print(f"Image URL: {image_url}")
            index+=1
        except:
            continue

    # 將爬取到的資料轉換成 DataFrame
    df = pd.DataFrame(data)

    # 將 DataFrame 存儲為 CSV 檔案
    filename = 'food_requests.csv'
    df.to_csv(filename, index=False, encoding='utf_8_sig')

