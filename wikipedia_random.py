import requests
import time

#wikipediaに接続するための基本設定
S = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"

#wikipediaのランダム記事リスト（idとタイトル）を取得するためのパラメータの設定
RANDOM_PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "5",
    "rnnamespace": "0"
}

#記事本体を取得するためのパラメータの設定
ARTICLE_PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "explaintext": True,
    "exsectionformat": "plain",
}

#ランダム記事リストの取得
RANDOM_R = S.get(url=URL, params=RANDOM_PARAMS)
RANDOM_DATA = RANDOM_R.json()
RANDOMS = RANDOM_DATA["query"]["random"]

#ランダム記事リストから各記事本体を取得
for r in RANDOMS:
    #ページIDと記事タイトルを変数に格納
    page_id = r["id"]
    title = r["title"]

    #ページIDから記事情報の取得
    ARTICLE_PARAMS["pageids"] = str(page_id)
    ARTICLE_R = S.get(url=URL, params=ARTICLE_PARAMS)
    ARTICLE_DATA = ARTICLE_R.json()

    #結果の出力
    print(title)
    print(ARTICLE_DATA["query"]["pages"][str(page_id)]["extract"])
    print("-"*40)

    #高速でリクエストを繰り返すことで負担をかけないように1秒待つ
    time.sleep(1)

print("終了しました")