## Document to Query Comparison Techniques,Papers, Data and Codes
### Papers:
1. [Pretrained Transformers for Text Ranking: BERT and Beyond](https://arxiv.org/abs/2010.06467)
2. [Multi Stage Ranking with BERT](https://www.researchgate.net/publication/360973402_Multi-Stage_Document_Ranking_with_BERT). Usage of multiple steps prediction helps for faster predictions.


### Code:
1. [ColBERT is a fast and accurate retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)
2. [Tensorflow For Ranking](https://github.com/tensorflow/ranking/blob/master/docs/tutorials/tfr_bert.ipynb) using Antique Dataset.
3. [Multi Stage Ranking with BERT](https://github.com/castorini/duobert)


### Personal Work and Codes

### Datasets:
1. [MS MARCO](https://microsoft.github.io/msmarco/) is a collection of datasets focused on deep learning in search. The first dataset was a question answering dataset featuring 100,000 real Bing questions and a human generated answer. 
2. [TREC Complex Answer Retrieval Overview](https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf)

### Performance Metrics
1. Mean Average Precision
2. Mean Reciprocal Rank

## Document to Data Comparison Techniques, Papers,Data and Codes
### Paper:
1. [Fine-tuned Siamese Sentence-BERT for
Matching Jobs and Job Seekers](https://arxiv.org/pdf/2109.06501.pdf). Explores Pooling of SBERT using sentence length, take the mean of last 4 layers of [CLS] sentences and taking first 512 tokens of each document(Seems naive but effective as per the author).
