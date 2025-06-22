# Wikipedia Path Finder Game

This project is a command-line game that finds the **shortest path between two Wikipedia articles** by crawling their hyperlinks. It's based on the "Wiki Game" where players try to get from one random article to another using only internal links.

---

## How the Game Works

- You enter a **start** and **end** Wikipedia article title.
- The program uses **Breadth-First Search (BFS)** to explore hyperlinks between pages.
- It attempts to find the **shortest chain of links** that connects the start page to the end page.

Example:

> Start: `Python (programming language)`  
> End: `Mahatma Gandhi`  
> Output (example path):  
> `Python (programming language)` → `Artificial intelligence → Philosophy of artificial intelligence → Philosophy of mind → Consciousness → Mind → Human → Human rights → Civil rights movement → Nonviolence → Mahatma Gandhi`

---

## How to Run

### 1. Clone or download this repository.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python main.py
```

You'll be prompted to enter two Wikipedia article titles.

---

## Files in This Project

- `main.py` — CLI interface for user input and path output.
- `bfs_path.py` — Core BFS logic to compute the shortest path.
- `wiki_api.py` — Handles Wikipedia API requests to get page links.
- `requirements.txt` — Lists required Python packages.

---

## Notes

- The search can take a long time depending on article popularity (lots of links).
- Results depend on Wikipedia API speed and availability.
- If the program runs too slowly, consider reducing search depth or using a cached/preprocessed graph instead.

---

## Future Improvements

- Use asynchronous requests for faster crawling
- Add a graphical UI

---

## Inspiration

This game is inspired by the popular online [Wikipedia Game](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game) where players race to find connections between topics.
