import numpy as np
import clip
import torch
import os
from PIL import Image

def index(images, device="cpu"):
    image_vectors = {}
    model, preprocess = clip.load("ViT-B/32", device=device)
    for image_path in images:
        filename = os.path.basename(image_path)
        try:
            image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
            with torch.no_grad():
                image_features = model.encode_image(image).cpu().numpy()
                image_features /= np.linalg.norm(image_features)
            image_vectors[filename] = image_features
        except Exception as e:
            print(f"Error processing image {filename}: {e}")
    return image_vectors

def search(vectors_data, query, device="cpu", verbose=False):
    image_vectors = {key: vectors_data[key] for key in vectors_data.keys()}
    image_vector_array = np.array(list(image_vectors.values()))

    if image_vector_array.ndim == 1:
        image_vector_array = image_vector_array.reshape(1, -1)

    model, preprocess = clip.load("ViT-B/32", device=device)
    text_input = clip.tokenize([query]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text_input).cpu().numpy()
        text_features /= np.linalg.norm(text_features, axis=1, keepdims=True)
    
    image_vector_array /= np.linalg.norm(image_vector_array, axis=1, keepdims=True)
    
    similarities = np.dot(image_vector_array, text_features.T).flatten()
    similarity_dict = {filename: similarity for filename, similarity in zip(image_vectors.keys(), similarities)}

    if verbose:
        print("Similarity scores:", similarity_dict)

    sorted_similarity_dict = dict(sorted(similarity_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_similarity_dict
