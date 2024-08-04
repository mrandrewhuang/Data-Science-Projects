# Project: Bank Customer Churn (Supervised Learning)

## Description

For this project, a bank has been experiencing a steady exist of customers every month. The bankers figured out that it’s cheaper to save the existing customers rather than to attract new ones.

My goal was to predict whether a customer would leave the bank soon. The dataset provided included data on customers' past behavior as well as termination of contracts with the bank.

Examine the balance of classes. Train the model without taking into account the imbalance. Briefly describe your findings.
Improve the quality of the model. Make sure you use at least two approaches to fixing class imbalance. Use the training set to pick the best parameters. Train different models on training and validation sets. Find the best one. Briefly describe your findings.
Perform the final testing.

I had to build a model with a maximum possible F1 score of at least 0.59, checked against the test set; examine and fix class imbalance; improve the quality of the model; tune hyperparameters. Additionally, the AUC-ROC metric had to be measured and compared with the F1 score.

## Data Description

### Features

* *RowNumber* — data string index
* *CustomerId* — unique customer identifier
* *Surname* — surname
* *CreditScore* — credit score
* *Geography* — country of residence
* *Gender* — gender
* *Age* — age
* *Tenure* — period of maturation for a customer’s fixed deposit (years)
* *Balance* — account balance
* *NumOfProducts* — number of banking products used by the customer
* *HasCrCard* — customer has a credit card
* *IsActiveMember* — customer’s activeness
* *EstimatedSalary* — estimated salary

### Target

* *Exited* — сustomer has left

## Tools

* Pandas, Seaborn, scikit-learn
