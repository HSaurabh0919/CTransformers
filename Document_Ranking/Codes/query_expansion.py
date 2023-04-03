from transformers import AutoTokenizer, AutoModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained BERT model and tokenizer
model_name = 'bert-large-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Define the original query
query = "what is the capital of France"

# Tokenize the query
tokens = tokenizer.encode(query, add_special_tokens=False, return_tensors='pt').squeeze()

# Generate embeddings for each token in the query
with torch.no_grad():
    outputs = model(tokens.unsqueeze(0))
    embeddings = outputs.last_hidden_state.squeeze(0)

# Define a vocabulary of similar words and phrases
vocab = ["Paris", "French capital", "City of Lights", "Eiffel Tower"]

# Calculate the cosine similarity between each token and each word or phrase in the vocabulary
similarities = cosine_similarity(embeddings.numpy(), np.array([tokenizer.encode(v, add_special_tokens=False) for v in vocab]))

# Select the most similar words or phrases for each token based on the cosine similarity
max_indices = similarities.argmax(axis=1)
selected_words = [vocab[i] for i in max_indices]

# Combine the original query with the selected words or phrases to form an expanded query
expanded_query = query + " " + " ".join(selected_words)

print(expanded_query)
