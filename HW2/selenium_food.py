# 導入必要的庫
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 設置 Chrome 驅動程式的路徑和啟動 WebDriver
service = Service("C:\\Users\\abc99\\HW2\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 打開目標網頁
driver.get("https://online.carrefour.com.tw/zh/%E9%A3%B2%E6%96%99%E9%9B%B6%E9%A3%9F")

# 等待網頁加載，確保所需元素已經存在於網頁中
wait = WebDriverWait(driver, 10)
food = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "hot-recommend-item.line")))

# 解析網頁並抓取資料
data = []
index = 1

for item in food:
       
    try:

        commodity = item.find_element(By.CLASS_NAME, "commodity-desc").find_element(By.TAG_NAME, 'a').text.strip()# 獲取商品名稱
        quantity = item.find_element(By.CLASS_NAME, "box-img").find_element(By.TAG_NAME, 'span').text.strip()# 獲取商品價格
        price = item.find_element(By.CLASS_NAME, "commodity-operation").find_element(By.CLASS_NAME, "current-price").find_element(By.TAG_NAME, 'em').text.strip()# 獲取商品備註
        remark = item.find_element(By.CLASS_NAME, "little-label").find_element(By.TAG_NAME, 'span').text.strip()# 獲取商品備註
        image_url = item.find_element(By.CLASS_NAME, 'box-img').find_element(By.TAG_NAME, 'img').get_attribute('src')# 獲取商品圖片 URL
        
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

        index += 1
    except:
        continue

# 將抓取的資料轉換為 DataFrame，並保存為 CSV 檔案
df = pd.DataFrame(data)
df.to_csv("selenium_food.csv", encoding='utf_8_sig', index=False)

# 關閉瀏覽器
driver.quit()
