import os
import numpy as np
from src.argparse import parser
from src.embedding import search, index

args = parser.parse_args()

allowed_extensions = ['.jpg', '.jpeg', '.png', '.webp']

def index_command():
    image_folder = args.folder
    print(f'Loading CLIP model and indexing images in folder "{image_folder}"...')

    all_files = os.listdir(image_folder)
    images = [file for file in all_files if os.path.splitext(file)[1].lower() in allowed_extensions]

    print(f'Total number of images: {len(images)}')

    image_vectors = index([os.path.join(image_folder, image) for image in images])

    vectors_file_path = os.path.join(image_folder, "vectors.npz")
    np.savez(vectors_file_path, **image_vectors)
    print(f'Saved vectors in file {vectors_file_path}')


def search_command():
    image_folder = args.folder
    print(f'Searching relevant images in folder "{image_folder}"...')

    vectors_path = os.path.join(image_folder, "vectors.npz")
    if not os.path.exists(vectors_path):
        print(f'File vectors.npz doesn\'t exist in folder "{image_folder}". Index the folder first.')
        exit()

    data = np.load(vectors_path)

    sorted_similarity_dict = search(data, args.query)

    print()
    print("Search results:")
    for filename, similarity in sorted_similarity_dict.items():
        print(f"{filename} {similarity:.4f}")

    return sorted_similarity_dict

def main():
    search_command() if args.command == 'search' else index_command()


if __name__ == "__main__":
    main()
