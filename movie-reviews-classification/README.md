# Project: Movie Reviews Classification (Machine Learning for Texts)

## Description

For this project, a trendy online community for classic movie enthusiasts is developing a system for filtering and categorizing movie reviews. My goal was to train a model to automatically detect negative reviews, using a dataset of IMBD movie reviews with polarity labeling to build a model for classifying positive and negative reviews. The requirement was achieving a F1 score of at least 0.85.

Classification models based on logistic regression and gradient boosting were incorporated in the project. Training the *BERT* model required processing power that I ultimately did not have, so the related code has been kept in the notebook but commented out.

## Data Description

_The data was provided by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). **Learning Word Vectors for Sentiment Analysis.** The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011)._

Description of selected fields:

* `review`: the review text
* `pos`: the target, '0' for negative and '1' for positive
* `ds_part`: 'train'/'test' for the train/test part of dataset, correspondingly

## Notes

* The datasets are excluded here as they was too large to upload

## Tools

* Pandas, NumPy, scikit-learn, Seaborn, NLTK, spaCy, LightGBM
