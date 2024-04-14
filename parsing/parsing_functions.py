import requests
from bs4 import BeautifulSoup as bs
# from seleniums import get_sourse_html

#resp = "/Крупа_гречана" #/Крупа_рис

def parse_prices():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"
    }
    # MinFin parser
    url = 'https://index.minfin.com.ua/ua/markets/product-prices/'
    page_prz = requests.get(url, headers=headers)
    rezult = bs(page_prz.text, "html.parser")
    result_list = []
    header_message = f'{rezult.find("caption").text}\n\n'
    result_list.append(header_message)
    products = rezult.findAll('tr')
    for i in products[1:34]:
        for_msg_line = i.findAll('td')
        try:
            msg_line = f'{for_msg_line[0].text} - {for_msg_line[1].text} за {for_msg_line[2].text}\n'
            result_list.append(msg_line)
        except:
            continue

    text_for_msg = ''.join(result_list)

    return text_for_msg
