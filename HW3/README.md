import requests
import pandas as pd
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # 設定目標網址
    url = "https://www.casetify.com/iphone-cases/iphone-15-pro-cases?nbt=nb%3Aadwords%3Ag%3A11813331349%3A117502735409%3A622083737674&nb_adtype=&nb_kwd=casetify&nb_ti=kwd-299194893737&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_si={sourceid}&nb_li_ms=&nb_lp_ms=&nb_fii=&nb_ap=&nb_mt=e&utm_source=google&utm_campaign=202012_MOFU_SN_Evergreen_TW_Brand_TCH&utm_medium=cpc&utm_content=&utm_term=casetify&gad_source=1&gclid=Cj0KCQjwir2xBhC_ARIsAMTXk85ZLFPSXAGCXOBM3_Icy3_TrTVBAmGSRXNDzxJ842QVFYMCXjC03F8aAjF6EALw_wcB"

    # 發送 HTTP 請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'  # 確保正確的編碼

    # 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有 'card' class 的 div 標籤
    items = soup.find_all('div', class_='card')
    index = 1
    data = []


    # 遍歷每個項目，爬取需要的資訊
    for item in items:
        try:
            #<p class="product-desc" data-v-dbc5a9d4="">iPhone 15 Pro<br>終極防摔手機殻</p>
            product_desc_tag = item.find('p', class_='product-desc')

            # 獲取產品名稱和特性描述的文本內容
            product_desc = product_desc_tag.text.strip()  # 整個產品描述的文本內容

            # 分離產品名稱和特性描述
            product_info = product_desc.split('<br>')
            phone_model = product_info[0].strip()  # 產品名稱
            product_type = product_info[1].strip()  # 特性描述

            artwork_desc = item.find('p', class_='artwork-desc').text.strip()
            color = item.find('p', class_='color-desc').text.strip()
            price = item.find('p', class_='price').text.strip()
            image_url = item.find('div', class_='block').find('img')['data-src']
            


            # title_tag = item.find('h4').find('a')
            # title = title_tag.get_text(strip=True)
            # language = item.find('div', class_='type clearfix').find('p').text.strip()
            # authors = [a.text for a in item.find('p', class_='author').find_all('a')]
            # author = ', '.join(authors)
            # price_info = item.find('ul', class_='price clearfix').find('li').get_text(strip=True)
            # price = price_info.split(',')[-1].strip()
            # image_url = item.find('div', class_='box').find('img')['data-src']


            # 將資料存儲到字典中
            temp_data = {
                "Phone_model" : phone_model,
                "Product_type" : product_type,
                "Artwork_desc" : artwork_desc,
                "Color" : color,
                "Price" : price,
                "Image URL": image_url

                # "Title": title,
                # "Language": language,
                # "Author": author,
                # "Price": price,
                # "Image URL": image_url
            }
            data.append(temp_data)


            print(f"----- casetify {index} -----")
            print(f"Phone_model: {phone_model}")
            print(f"Product_type: {product_type}")
            print(f"Artwork_desc: {artwork_desc}")
            print(f"Color: {color}")
            print(f"Price: {price}")
            index+=1
        except:
             continue
       
        #     print(f"----- Book {index} -----")
        #     print(f"Title: {title}")
        #     print(f"Language: {language}")
        #     print(f"Authors: {', '.join(authors)}")
        #     print(f"Price: {price}")
        #     print(f"Image URL: {image_url}")
        #     index+=1
        # except:
        #     continue
    print(artwork_desc)
    df = pd.DataFrame(data)
    filename = 'casetify_requests.csv'
    df.to_csv(filename, index=False, encoding='utf_8_sig')
