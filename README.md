# [CTransformers](https://github.com/HSaurabh0919/CTransformers/)

Implementing wide variety of transformers (improvised version),finetuning as well as trying architectural variants from various research papers and blogs.

1. Roberta Pretraining : Basic Implementation , More detail about the model can be found [here](https://huggingface.co/transformers/model_doc/roberta.html). 
2. Implementing Fast Transformers: Failed Attempt, FastTransformer Algorithm can be found [here](https://github.com/HSaurabh0919/CTransformers/blob/main/Fast_Transformers.ipynb).
3. Adaptive Transformers for multimodal Representations: Research paper can be found [here](https://arxiv.org/abs/2005.07486).
4. Learning Cross-Modality Encoder Representation from transformers: Paper can be found [here](https://arxiv.org/abs/1908.07490). 

# [Text Generation Models](https://github.com/HSaurabh0919/CTransformers/)
My text generation model trained on Bhagvad_Gita (Holy Hindu Scripture English version) is now available on [huggingface](https://huggingface.co/) and can be found [here](https://huggingface.co/epsil/bhagvad_gita). 

The easiest way to use them is as below:
```

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("epsil/bhagvad_gita")

model = AutoModelForCausalLM.from_pretrained("epsil/bhagvad_gita")

```
# [Weak Supervision Models](https://github.com/HSaurabh0919/CTransformers/blob/main/WeakSupervision/Fin_SA_WeakSupervision.ipynb)
Weak Supervision model build wirh Snorkel and with Finance dataset taken from [here](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts). Majority Vote Modelling with some heuristics(rules) and currently work on 3 labelling function. Overall accuracy reached is about 61% and can be enhanced further by dealing with mixed sentence heuristics.

# [FineTune Sentence Transformers](https://github.com/HSaurabh0919/CTransformers/blob/main/BERT/Sbert_finetune.ipynb)
1. Finetuning of Sentence Transformer for customized dataset.
2. Improvements in Comparison Methods and Advanced Comparison Techniques.

# [Performance Evaluation of Open Source LLM Models](https://github.com/HSaurabh0919/CTransformers/blob/main/Llama/readme.md)
1. Performance evaluation of llama-7B Model
2. Performance evaluation of Redpajama-3B Model
3. Performance evaluation of Bloke Syntara-7B Model


# Stay Tuned !!!


   
