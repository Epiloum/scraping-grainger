import requests
from bs4 import BeautifulSoup

def get_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
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

def get_attributes_from_elements(elements, attribute_name):
    attribute_values = []
    for element in elements:
        attribute_value = element.get(attribute_name)
        if attribute_value:
            attribute_values.append(attribute_value)
    return attribute_values