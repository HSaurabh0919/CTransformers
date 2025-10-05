[Fraud detection](https://github.com/HSaurabh0919/CTransformers/tree/main/Fraud%20Detection) in machine learning can be approached using supervised methods like logistic regression and random forests trained on labeled fraudulent and legitimate data, or unsupervised/anomaly detection techniques such as isolation forests and autoencoders that identify unusual behavior without prior labels.
Hybrid models combining rule-based systems and ML algorithms are also common to enhance detection accuracy and reduce false positives.

Fraud detection can use supervised learning approaches like logistic regression or random forests, which rely on labeled data to accurately classify known fraud patterns.
Unsupervised approaches, such as clustering or anomaly detection, identify unusual behavior without labeled data, making them valuable for detecting new or evolving fraud types.

###  Algorithms for Fraud Detection : 

| Algorithm | Pros | Cons |
|-----------|-----------|-----------|
| Rule Based Detection System  | Interpretable  | Need tuning  |
| Supervised Learning | Good for handle previous known cases | Need curated dataset |
| Unsupervised Learning | Good for handling cases  | Usually Time Complexity is high |


### Common Issues when designing Fraud Detection System 

1. Sampling Bias : Sampling bias in fraud detection occurs when the training data doesn’t accurately represent the real-world distribution of transactions — for example, if fraudulent cases are over- or under-represented. This bias can lead the model to overfit to common patterns or miss rare fraud cases, reducing its ability to generalize and detect new or unseen fraudulent behavior in production. Some of the ways to deal with this is by having some random selection, models that are cost-sentitive
