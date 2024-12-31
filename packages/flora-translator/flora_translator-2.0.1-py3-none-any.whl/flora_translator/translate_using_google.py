import requests
from bs4 import BeautifulSoup

def translate(batch: list[str], source: str = "auto", target: str = "en", proxies: dict = None) -> str:
    if not batch:
        raise Exception("Enter your text list that you want to translate")
    arr = []
    for i, text in enumerate(batch):
        if not text.strip():
            return text
        base_url = "https://translate.google.com/m"
        params = {
            "sl": source,
            "tl": target,
            "q": text,
        }
        response = requests.get(base_url, params=params, proxies=proxies)
        if response.status_code != 200:
            raise Exception(f"error: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        element = soup.find("div", class_="result-container")
        if element:
            translated_text = element.get_text(strip=True)
        else:
            raise Exception("translate not found!")

        arr.append(translated_text)
    return arr
    

def translate_using_google (src:str, from_language:str, into_language:str):
    sents = []

    current_sent = ""
    num = 0
    for i in src:
        if num >= 250:
            sents.append(current_sent)
            current_sent = ""
            num = 0
        current_sent = current_sent + i
        num = num + 1

    sents.append(current_sent)
    res = translate(batch=sents,source=from_language,target=into_language)

    full_res = ""
    for i in res:
        if i == None:continue
        full_res = full_res + i

    return str(full_res)
