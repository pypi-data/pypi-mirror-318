import sys
from . import wiki_to_markdown

async def main():
    # expect wikipedia article title as argument

    if len(sys.argv) != 2:
        print("Please provide a single Wikipedia article title as an argument.")
        sys.exit(1)

    title = sys.argv[1]
    print(await wiki_to_markdown(title))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())