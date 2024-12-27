import requests
from bs4 import BeautifulSoup

def get_from_url(url):

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    #     'Accept-Language': 'en-US,en;q=0.9',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Upgrade-Insecure-Requests': '1',
    # }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Content-Length': '10000',
        'Content-Type': 'application/json',
        'Origin': 'https://www.grainger.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://www.grainger.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'macOS',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        "Cookie": "AD1=A; DS2=B; LDC=B4E88BA9E4F8323438CF4E1E7520E5DA; s_ecid=MCMID|13867938534111727794305114338318393546; _gcl_au=1.1.997246555.1735204505; _fbp=fb.1.1735204505495.798796302665288542; _ga=GA1.1.343179246.1735204506; aam_uuid=13947756574926643104313052157534949015; TLTSID=DFBFD9C6D864E9C17E87EDA439B25F32; signin=C; reg=A; PIM-SESSION-ID=RNIxbxFyvFmSWuwV; AMCVS_FC80403D53C3ED6C0A490D4C@AdobeOrg=1; AMCV_FC80403D53C3ED6C0A490D4C@AdobeOrg=1176715910|MCIDTS|20084|MCMID|13867938534111727794305114338318393546|MCAAMLH-1735879764|11|MCAAMB-1735879764|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1735282164s|NONE|MCAID|NONE|vVersion|5.4.0; JSESSIONID=2118A6BDE9DC3A4D55FD8C89FF18DEE3.422bcc08; at_check=true; s_ivc=true; s_cc=true; maId={\"cid\":\"a8f673c558dac01a1ebdac8c2ef2d581\",\"sid\":\"268e32e6-c4a6-43bc-a57a-4102d9568b52\",\"isSidSaved\":true,\"sessionStart\":\"2024-12-27T04:49:28.000Z\"}; CIP=183.98.146.90; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+27+2024+14%3A26%3A53+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=dd684465-c027-4abf-83d4-5730e426c82f&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0007%3A1%2CC0003%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false; datadome=KbemybaPKliDHHYY1lv0STCyQBiBETtPKTZ6vTRPDL0RroUWjLQjxGtekY9pKa80MsWP2nwdtkRfAg10wxmWhtNannMnCvztDV8_YO0NB5Djfthchj34jOcrvafwIhFq; _ga_94DBLXKMHK=GS1.1.1735274967.2.1.1735277213.59.0.0; _abck=C49740BC0CB77E9A8AE0C296B5AEF984~-1~YAAQTnpGaKmLD+CTAQAAMB6VBg1g/Yf4RojJQ1w7sbkUk62woR3TXZPtsT4z+V/a7aa76NOcfVnCpa0+KQdnmK1ryck+dOl3JIixrIu0PMvt5mQ/IkKyEjiedOPt6cwl6kbBB6mmseWTM0licOzcHynvm7Z04mthziK52ap9EYbuKIFW6UHp/aB/pvVCi0kUCIKU8Vdf1mFk2MN188ezbyPVOl1TgQnjdOBchiAhw/ZdeHVekT0aVMExYNF4ph53kQz3ARWvsJOyrravvo2bogDIJIE984dYje090ChObLAS3z6WTi4noLylDAWcE8w+lv21l+kQfzBMbQDaTT85XkgDPzjzqxhl+vkXYHzWz9chiXO3MgBjtWkvxyirwFMthdxLrrhUEK1ZVJllOEGZ4J13Eo2ltJDucDd6wQ1ouKQYXnI13p8+WOOEsyeBZVIDb57AM7mlXVI7z1JCjAgyKOXWecUAMfj/jWM5sb87hIpv1NTRpny94qCE++lFqC1IzsmTN8/A923r6Q"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    return response.text

def get_elements_from_texts(text, css_selector):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.select(css_selector)
    
def get_elements_from_text(text, css_selector):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.select_one(css_selector)

def get_inner_html_from_elements(elements):
    return [element.decode_contents() for element in elements]

def get_inner_html_from_text(element):
    return element.get_text()

def get_attributes_from_elements(elements, attribute_name):
    attribute_values = []
    for element in elements:
        attribute_value = element.get(attribute_name)
        if attribute_value:
            attribute_values.append(attribute_value)
    return attribute_values