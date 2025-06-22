from collections import deque
from wiki_api import get_links

def shortest_wiki_path(start_title, end_title, max_depth=5):
    visited = set()
    queue = deque([(start_title, [start_title])])
    cache = {}

    while queue:
        current_title, path = queue.popleft()
        if len(path) > max_depth:
            continue

        if current_title == end_title:
            return path

        if current_title in visited:
            continue
        visited.add(current_title)

        if current_title in cache:
            links = cache[current_title]
        else:
            links = get_links(current_title)
            cache[current_title] = links

        for link in links:
            if link not in visited:
                queue.append((link, path + [link]))

    return None
