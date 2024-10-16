# CLI Tool: Image Search Using CLIP and Vector Embeddings

This CLI tool allows you to index images from a specified folder and search for similar images based on a text query using CLIP (Contrastive Language-Image Pretraining), PyTorch and NumPy. It generates image vectors and allows you to perform semantic searches efficiently.

## Features

- Index images and generate vector embeddings.
- Search for images based on text queries.
- Supports multiple image formats (.jpg, .jpeg, .png, .webp).

## Usage

**To search for images by text query, you must first index the folder containing the images using this tool.**

### Index Images

To index images from a folder `images`, run:

```sh
(venv) ➜ vector-embeddings python main.py index -f images
```

This command will process the images in the images folder, generate their vector embeddings using the CLIP model, and save them to vectors.npz in the same folder.

### Search for Relevant Images

To search for similar images based on a text query, run:

```sh
(venv) ➜ vector-embeddings python main.py search "Your text query" -f images
```

Replace "Your text query" with the description of the image you are looking for. The tool will load the vectors from vectors.npz and return the most similar images.
