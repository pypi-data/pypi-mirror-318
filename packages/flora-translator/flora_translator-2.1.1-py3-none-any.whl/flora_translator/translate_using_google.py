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

GOOGLE_LANGUAGES_TO_CODES = {'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','assamese': 'as','aymara': 'ay','azerbaijani': 'az','bambara': 'bm','basque': 'eu','belarusian': 'be','bengali': 'bn','bhojpuri': 'bho','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb','chichewa': 'ny','chinese_simplified': 'zh','chinese_traditional': 'zh','corsican': 'co','croatian': 'hr','czech': 'cs','danish': 'da','dhivehi': 'dv','dogri': 'doi','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','ewe': 'ee','filipino': 'tl','finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el','guarani': 'gn','gujarati': 'gu','haitian_creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'he','hindi': 'hi','hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','ilocano': 'ilo','indonesian': 'id','irish': 'ga','italian': 'it','japanese': 'ja','javanese': 'jv','kannada': 'kn','kazakh': 'kk','khmer': 'km','kinyarwanda': 'rw','konkani': 'kok','korean': 'ko','krio': 'kri','kurdish_kurmanji': 'ku','kurdish_sorani': 'ckb','kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lingala': 'ln','lithuanian': 'lt','luganda': 'lg','luxembourgish': 'lb','macedonian': 'mk','maithili': 'mai','malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','meiteilon_manipuri': 'mni','mizo': 'lus','mongolian': 'mn','myanmar': 'my','nepali': 'ne','norwegian': 'no','odia_oriya': 'or','oromo': 'om','pashto': 'ps','persian': 'fa','polish': 'pl','portuguese': 'pt','punjabi': 'pa','quechua': 'qu','romanian': 'ro','russian': 'ru','samoan': 'sm','sanskrit': 'sa','scots_gaelic': 'gd','sepedi': 'nso','serbian': 'sr','sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so','spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','tatar': 'tt','telugu': 'te','thai': 'th','tigrinya': 'ti','tsonga': 'ts','turkish': 'tr','turkmen': 'tk','twi': 'tw','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'}

def map_language_to_code(*languages):
    for language in languages:
        if language == "auto":
            yield language
        elif language in GOOGLE_LANGUAGES_TO_CODES.keys():
            yield GOOGLE_LANGUAGES_TO_CODES[language]
        else:
            raise Exception("language not found!")

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
    from_language , into_language = map_language_to_code(from_language,into_language)
    res = translate(batch=sents,source=from_language,target=into_language)

    full_res = ""
    for i in res:
        if i == None:continue
        full_res = full_res + i

    return str(full_res)