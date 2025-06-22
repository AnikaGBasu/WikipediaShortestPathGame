import requests

def get_links(title):
    """
    Given a Wikipedia article title, return a list of linked article titles.
    """
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "titles": title,
        "pllimit": "max"
    }

    links = []
    while True:
        R = S.get(url=URL, params=PARAMS)
        if R.status_code != 200:
            break

        DATA = R.json()
        pages = DATA['query']['pages']
        for page_id in pages:
            if 'links' in pages[page_id]:
                links.extend([link['title'] for link in pages[page_id]['links']])

        if 'continue' in DATA:
            PARAMS.update(DATA['continue'])
        else:
            break

    return links