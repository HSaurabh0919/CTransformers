from transformers import BertTokenizer, TFBertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertModel.from_pretrained('bert-base-uncased')

query = "What is the capital of France?"
sentence = "Paris is the capital of France."

# Concatenate the query and sentence with [SEP] token in between
input_text = "[CLS] " + query + " [SEP] " + sentence + " [SEP]"


# Tokenize the input text
input_ids = tokenizer.encode(input_text, add_special_tokens=True)

# Convert the input_ids to a tensor
input_ids = tf.constant(input_ids)[None, :]

# Pass the input_ids through the model to get the output
output = model(input_ids)
