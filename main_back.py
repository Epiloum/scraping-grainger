import lib_http as http
import lib_array as arr
import lib_file as file
import json


# Crawling categories
def get_grainger_categories(categories):
    for item in categories:
        html = http.get_from_url('https://www.grainger.com' + item['url'])
        res = arr.merge_arrays_to_dict_list('url', 'title', get_url(html), get_title(html))

        print(res[0]['title'] if len(res) > 0 else "*")

        if len(res):
            item['subs'] = get_grainger_categories(res)
        else:
            item['subs'] = get_variants(html)

    return categories


def get_url(html):
    elements = http.get_elements_from_texts(html, '._3dXDpA a')
    return http.get_attributes_from_elements(elements, 'href')


def get_title(html):
    elements = http.get_elements_from_texts(html, '._3dXDpA a h2')
    return http.get_inner_html_from_elements(elements)


def get_variants(html):
    elements = http.get_elements_from_text(html, '#__PRELOADED_STATE__')
    if elements is None: return []
    data = json.loads(elements.decode_contents())
    categoryId = data['category']['category']['id']
    collections = data['category']['collections']

    tuples = []

    for collection in collections:
        tup = {'url': 'last category', 'title': collection['name'], 'variants': {}}
        columns = collection['columns']

        variantUrl = f'https://www.grainger.com/experience/pub/api/products/collection/{collection["id"]}?categoryId={categoryId}'
        variants = http.get_from_url(variantUrl)
        variant = json.loads(variants)[0]

        singular = [{'id': item['id'], 'name': item['label']} for item in columns]
        multiple = []

        if 'groupDifferingAttributes' in variant:
            att = variant['groupDifferingAttributes']
            if f'{categoryId}' in att:
                for item in att[f'{categoryId}']:
                    multiple.append(item['name'])
                    for s in singular:
                        if s['id'] == item['merchandisingAttributeId']:
                            singular.remove(s)

        tup['variants']['singular'] = [s['name'] for s in singular]
        tup['variants']['multiple'] = multiple
        tup['layout'] = check_layout(html)
        tuples.append(tup)

    return tuples


# Checking Product List Layout
def check_layout(html):
    if 'J5ihJT' in html:
        return 'Variants Table View'
    else:
        return 'Grid View'


# Exporting
def export_categories_to_table(head, data):
    res = ''

    for item in data:
        if 'subs' in item:
            res = res + export_categories_to_table(
                head + '<td><a href="https://www.grainger.com' + item['url'] + '">' + item['title'] + '</a></td>', item['subs']
            )
        else:
            depth = head.count('<td>')
            count_singular = len(item['variants']['singular'])
            count_multiple = len(item['variants']['multiple'])

            categories = head + '<td>' + item['title'] + '</td>' + ('<td></td>' * (8 - depth))
            layout = '<td>' + item['layout'] + '</td>'
            variants_singular = ''.join(['<td>' + s + '</td>' for s in item['variants']['singular']]) + (
                    '<td></td>' * (12 - count_singular))
            variants_multiple = ''.join(['<td>' + s + '</td>' for s in item['variants']['multiple']]) + (
                    '<td></td>' * (4 - count_multiple))
            res = res + '<tr>' + categories + layout + variants_singular + variants_multiple + '</tr>'

    return res


# Settings
# tar = [{'url':'/category?analytics=nav', 'title': 'Entire'}]
tar = [{'url': '/category/abrasives/sanding-abrasives/sanding-discs', 'title': 'Sanding Discs'}]
res = get_grainger_categories(tar)
file.write_to_file('tmp.json', json.dumps(res))
tbl = export_categories_to_table('', res)

# Print
file.write_to_file('tmp.html', '<table border="1" style="border-collapse:collapse">' + tbl + '</table>')
