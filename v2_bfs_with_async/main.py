import asyncio
from bfs_path_async import shortest_wiki_path_async

def main():
    start = input("Enter the START Wikipedia article title: ")
    end = input("Enter the END Wikipedia article title: ")
    
    print(f"\nSearching for shortest path from '{start}' to '{end}'...\n")
    path = asyncio.run(shortest_wiki_path_async(start, end))

    if path:
        print(" → ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
