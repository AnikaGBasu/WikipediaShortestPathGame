# Wikipedia Path Finder Game

This project is a command-line game that finds the **shortest path between two Wikipedia articles** by crawling their hyperlinks. It's based on the "Wiki Game," where players try to get from one article to another using only internal Wikipedia links.

---

## Two Versions: Synchronous vs. Asynchronous

This project includes **two implementations** of the same idea:

### 1. Synchronous Version (`/sync`)
- Uses Python’s built-in `requests` library to fetch hyperlinks **one at a time**.
- Easier to understand for beginners learning BFS and web scraping.
- **Slower**, especially when exploring many articles (hundreds of HTTP requests happen sequentially).
- Best for learning or testing with simple examples.

### 2. Asynchronous Version (`/async`)
- Uses `aiohttp` and `asyncio` to fetch multiple Wikipedia pages **in parallel**.
- Much **faster** for large or deep searches (especially beyond depth=2).
- Includes concurrency-safe BFS logic and request caching.

---

## How the Game Works

- You enter a **start** and **end** Wikipedia article title.
- The program uses **Breadth-First Search (BFS)** to explore hyperlinks.
- It finds the **shortest chain of links** connecting the two articles.

Example:

> Start: `Python (programming language)`  
> End: `Mahatma Gandhi`  
> Output (example path):  
> `Python (programming language)` → `Artificial intelligence` → `Philosophy of artificial intelligence` → … → `Mahatma Gandhi`

---

## How to Run

### 1. Clone or download this repository

### 2. Navigate to a version

```bash
cd sync        # or: cd async
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python main.py
```

You'll be prompted to enter two Wikipedia article titles.

---

## Project Structure

```
wiki_path_finder/
├── sync/
│   ├── main.py
│   ├── bfs_path.py
│   ├── wiki_api.py
│   └── requirements.txt
├── async/
│   ├── main.py
│   ├── bfs_path_async.py
│   ├── wiki_api_async.py
│   └── requirements.txt
```

---

## Notes

- The synchronous version can hang or take a long time for large searches.
- The asynchronous version is significantly faster but requires an internet connection and a working event loop.
- If you're seeing timeout errors in the async version, check your network or firewall settings.

---

## Future Improvements

- Add a graphical UI
- Visualize the article graph
- Add a random start/end mode
- Use a local Wikipedia dump to enable offline search

---

## Inspiration

Inspired by the [Wikipedia Game](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game), where players race to connect topics using only hyperlinks.
