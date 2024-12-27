import time
import lib_http as http
import lib_array as arr
import mysql.connector
import html

# Crawling categories
def get_grainger_categories(categories):
    time.sleep(3)
    for item in categories:
        html = http.get_from_url('https://www.grainger.com' + item['url'])
        item['description'] = get_description(html)
        res = arr.merge_arrays_to_dict_list('url', 'title', get_url(html), get_title(html))

        update_description(item)

        if len(res) > 0:
            item['subs'] = get_grainger_categories(res)

    return categories

def get_url(html):
    elements = http.get_elements_from_texts(html, '._3dXDpA a')
    return http.get_attributes_from_elements(elements, 'href')

def get_title(html):
    elements = http.get_elements_from_texts(html, '._3dXDpA a h2')
    return http.get_inner_html_from_elements(elements)

def get_description(html):
    element = http.get_elements_from_text(html, '.YHWWIR')
    if element:
        return element
    else:
        return 'None'


def update_description(item):
    if len(item['title']) > 0 :
        # SQL 실행
        cursor.execute('SELECT id, name_english, COUNT(*) AS cnt FROM category WHERE name_english = "' + html.unescape(item['title']) + '" GROUP BY name_english')
        row = cursor.fetchone()

        if not row:
            print('DATA NOT FOUND : ' + item['title'])
        else:
            if row[2] == 1 and item['description'] != 'None':
                cursor.execute('UPDATE category SET description_english = "' +item['description']+ '" WHERE id = ' + row[0] + ' LIMIT 1')
                print('DATA update : ' + item['title'])
            else:
                if row[2] > 1:
                    print('DATA duplicate : ' + item['title'])
                elif item['description'] == 'None' :
                    print('DATA NOT description : ' + item['title'])
                else:
                    print('DATA NONE : ' + item['title'])


# Settings
#tar = [{'url':'/category?analytics=nav', 'title': 'Entire'}]
# tar = [{'url':'/category/abrasives', 'title':'Abrasives'}]
tar = [{'url':'/category/abrasives/sanding-abrasives/sanding-discs', 'title':'Sanding Discs'}]
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mypass',
    database='buybly'
)
cursor = conn.cursor()

res = get_grainger_categories(tar)
# file.write_to_file('abrasives_tmp.json', json.dumps(res))

cursor.close()
conn.close()