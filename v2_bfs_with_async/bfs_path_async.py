import asyncio
import aiohttp
from collections import deque
from wiki_api_async import fetch_links

async def shortest_wiki_path_async(start_title, end_title, max_depth=5):
    visited = set()
    queue = deque([(start_title, [start_title])])
    cache = {}
    
    async with aiohttp.ClientSession() as session:
        while queue:
            current_title, path = queue.popleft()

            if len(path) > max_depth:
                continue

            if current_title == end_title:
                return path

            if current_title in visited:
                continue
            visited.add(current_title)

            # Cache to avoid re-fetching
            if current_title in cache:
                links = cache[current_title]
            else:
                links = await fetch_links(session, current_title)
                cache[current_title] = links

            # Schedule multiple fetches in parallel for next layer
            for link in links:
                if link not in visited:
                    queue.append((link, path + [link]))

    return None
