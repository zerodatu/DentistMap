#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# ベースURL
base_url = "https://www.shika-town.com/accounts/search/list"

# スクレイピングした歯医者のリストを格納するリスト
dentists = []

# ユーザーエージェントを設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_page(page):
    params = {"page": page}
    response = requests.get(base_url, params=params, headers=headers)
    result = []

    if response.status_code != 200:
        print(f"ページ {page} を取得できませんでした。ステータスコード: {response.status_code}")
        return result

    soup = BeautifulSoup(response.content, "html.parser")

    # 'single_box'クラス内の情報を取得
    items = soup.find_all("div", class_="single_box")
    if not items:
        print(f"ページ {page} に結果がありません。")
        return result

    for item in items:
        # 歯医者名を取得
        name_tag = item.find("div", class_="com_title_box").find("h2")
        name = name_tag.text.strip() if name_tag else "N/A"

        # 住所と電話番号を取得
        table = item.find("table", class_="data auto")
        if table:
            rows = table.find_all("tr")
            address = "N/A"
            phone = "N/A"

            for row in rows:
                header = row.find("th")
                data = row.find("td")
                if header and data:
                    header_text = header.text.strip()
                    data_text = data.text.strip()
                    if "住所" in header_text:
                        address = data_text
                    if "電話" in header_text:
                        phone = data_text

            result.append({
                "name": name,
                "address": address,
                "phone": phone
            })

    return result

# 並列処理の設定
max_workers = 10  # 並列処理するスレッド数
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    future_to_page = {executor.submit(scrape_page, page): page for page in range(1, 7002)}
    for future in as_completed(future_to_page):
        page = future_to_page[future]
        try:
            data = future.result()
            dentists.extend(data)
        except Exception as exc:
            print(f"ページ {page} で例外が発生しました: {exc}")

# 結果をテキストファイルに保存
with open("dentists_list.txt", "w", encoding="utf-8") as f:
    for dentist in dentists:
        f.write(f"{dentist['name']}, {dentist['address']}, {dentist['phone']}\n")

print(f"{len(dentists)} 件の歯医者のリストが 'dentists_list.txt' に保存されました。")
