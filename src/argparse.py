import argparse

parser = argparse.ArgumentParser(description="Image Vector Processing Tool")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

index_parser = subparsers.add_parser("index", help="Index images and create vectors")
index_parser.add_argument("-f", "--folder", type=str, help="Path to the folder with images", required=True)

search_parser = subparsers.add_parser("search", help="Search for similar images by text")
search_parser.add_argument("query", type=str, help="Text query for searching images")
search_parser.add_argument("-f", "--folder", type=str, help="Path to the folder with images", required=True)
search_parser.add_argument("-n", "--num", type=int, help="Number of results, default 10", default=10)
search_parser.add_argument("-v", "--verbose", help="Verbose - append similarity numbers", action="store_true")
