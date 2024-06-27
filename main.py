import lib_http as http
import lib_array as arr
import lib_file as file
import json

# Crawling
def get_grainger_categories(categories):
    for item in categories:
        response = http.get_from_url('https://www.grainger.com' + item['url'])

        elements = http.get_elements_from_text(response, '._3dXDpA a')
        hrefs = http.get_attributes_from_elements(elements, 'href')

        elements = http.get_elements_from_text(response, '._3dXDpA a h2')
        texts = http.get_inner_html_from_elements(elements)

        res = arr.merge_arrays_to_dict_list('url', 'title', hrefs, texts)
        
        print(texts[0] if len(texts) else '*')

        if len(res):
            item['subs'] = get_grainger_categories(res) 

    return categories

# Exporting
def export_categories_to_table(head, data):
    res = ''

    for item in data:
        res = res + '<tr>' + head + '<td><a href="https://www.grainger.com' + item['url'] + '">' + item['title'] + '</a></td></tr>'
        
        if 'subs' in item:
            res = res + export_categories_to_table(head + '<td>' + item['title'] + '</td>', item['subs'])

    return res

# Settings
tar = [{'url':'/category?analytics=nav', 'title': 'Entire'}]
res = get_grainger_categories(tar)
file.write_to_file('res.json', json.dumps(res))
tbl = export_categories_to_table('', res)

# Print
file.write_to_file('res.html', '<table>' + tbl + '</table>')