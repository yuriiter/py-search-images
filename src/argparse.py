import argparse

parser = argparse.ArgumentParser(description="Image Vector Processing Tool")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

index_parser = subparsers.add_parser("index", help="Index images and create vectors")
index_parser.add_argument("-f", "--folder", type=str, help="Path to the folder with images")

search_parser = subparsers.add_parser("search", help="Search for similar images by text")
search_parser.add_argument("query", type=str, help="Text query for searching images")
search_parser.add_argument("-f", "--folder", type=str, help="Path to the folder with images")
