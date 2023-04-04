from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig

tok = BartTokenizer.from_pretrained("facebook/bart-large")
model = BartForConditionalGeneration(BartConfig())

input_string = "My dog is <mask> </s>"
decoder_input_string = "<s> My dog is cute"
labels_string = "My dog is cute </s>"

input_ids = tok(input_string, add_special_tokens=False, return_tensors="pt").input_ids
decoder_input_ids =tok(decoder_input_string, add_special_tokens=False, return_tensors="pt").input_ids
labels = tok(labels_string, add_special_tokens=False, return_tensors="pt").input_ids
 
loss = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids, labels=labels)[0]
