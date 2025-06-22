import aiohttp
import asyncio
import ssl

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

async def fetch_links(session, title):
    """
    Fetch links from a Wikipedia article asynchronously using aiohttp.
    """
    params = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "titles": title,
        "pllimit": "max"
    }

    links = []

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    while True:
        async with session.get(WIKI_API_URL, params=params, ssl=ssl_context) as resp:
            if resp.status != 200:
                return []

            data = await resp.json()
            pages = data['query']['pages']
            for page_id in pages:
                if 'links' in pages[page_id]:
                    links.extend([link['title'] for link in pages[page_id]['links']])

            if 'continue' in data:
                params.update(data['continue'])
            else:
                break

    return links
