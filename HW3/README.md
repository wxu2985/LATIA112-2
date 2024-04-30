import pandas as pd
from bs4 import BeautifulSoup

def parse_product_card(card):
    """
    解析單個產品卡片的資訊
    """
    try:
        product_desc = card.find('p', class_='product-desc').text.strip()
        artwork_desc = card.find('p', class_='artwork-desc').text.strip()
        color_desc = card.find('p', class_='color-desc').text.strip()
        price = card.find('p', class_='price').text.strip()

        return {
            "Product Description": product_desc,
            "Artwork Description": artwork_desc,
            "Color Description": color_desc,
            "Price": price
        }
    except Exception as e:
        print("Error parsing product card:", e)
        return None

def main():
    # 輸入原始碼
    html_content = """
    <div class="card" data-v-dbc5a9d4=""><div class="block" data-v-dbc5a9d4=""><div class="holder" data-v-dbc5a9d4=""></div><div class="image-container" data-v-dbc5a9d4=""><img class="preview-image" src="https://cdn-image02.casetify.com/usr/8405/29948405/~v89/27729581_iphone-15-pro__color_natural-titanium_16006964.png.350x350-w.m80.webp" alt="iPhone 15 Pro - Daisy by Katie-s Collective" loading="lazy" data-v-dbc5a9d4=""></div><!----></div><div class="details" data-v-dbc5a9d4=""><p class="product-feature af-orange highlight-DLP_HIGHLIGHT_MAGSAFE prefix-icon magsafe" data-v-dbc5a9d4="">MagSafe 兼容</p><p class="product-desc" data-v-dbc5a9d4="">iPhone 15 Pro<br>終極防摔手機殻</p><p class="artwork-desc" data-v-dbc5a9d4="">Daisy by Katie-s Collective</p><p class="color-desc" data-v-dbc5a9d4="">6 款顏色</p><p class="price" data-v-dbc5a9d4="">NT$2750</p></div><a class="product-link" title="iPhone 15 Pro 終極防摔手機殻 - Daisy by Katie-s Collective" href="/zh_TW/product/daisy-by-katie-s-collective/iphone-15-pro/bounce-case#/16006964" rel="nofollow" data-v-dbc5a9d4=""></a></div>
    """
    
    # 解析 HTML 內容
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 找到所有卡片
    cards = soup.find_all('div', class_='card')
    
    # 解析每個卡片的資訊
    data = [parse_product_card(card) for card in cards]
    
    # 去除空值
    data = [d for d in data if d is not None]
    
    # 將資料轉換為 DataFrame
    df = pd.DataFrame(data)
    
    # 將 DataFrame 寫入 CSV 檔案
    filename = 'product_info.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"CSV 檔案 '{filename}' 已儲存。")

if __name__ == '__main__':
    main()
