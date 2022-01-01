# [CTransformers](https://github.com/CCsaurabh/CTransformers/)

Implementing wide variety of transformers (improvised version),finetuning as well as trying architectural variants from various research papers and blogs.

1. Roberta Pretraining : Basic Implemenatation , More detail about the model can be found [here](https://huggingface.co/transformers/model_doc/roberta.html). 
2. Implementing Fast Transformers: Failed Attempt, FastTransformer Algorithm can be found [here](https://github.com/CCsaurabh/fast-transformer-pytorch).
3. Adaptive Transformers for multimodal Representations: Research paper can be found [here](https://arxiv.org/abs/2005.07486).
4. Learning Cross-Modality Encoder Representation from transformers: Paper can be found [here](https://arxiv.org/abs/1908.07490). 

# [Linguistic Models](https://github.com/CCsaurabh/CTransformers/)
My text generation model trained on Bhagvad_Gita (Holy Hindu Scripture English version) is now available on [huggingface](https://huggingface.co/) and can be found [here](https://huggingface.co/epsil/bhagvad_gita). 

The easiest way to use them is as below:
```

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("epsil/bhagvad_gita")

model = AutoModelForCausalLM.from_pretrained("epsil/bhagvad_gita")

```
