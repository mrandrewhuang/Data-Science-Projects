# Project: Telecom Churn Forecast (Final Project)

## Description

For this final project, a telecom company wants to be able to forecast their churn of clients. The company offeres two types of services, both with additional plan options: landline and internet. The datasets provided included their customers' personal data (including information about their plans and contracts). The target feature: `'Churned'` (feature-engineered from `'EndDate'`), and the evaluation metric: AUC-ROC.

## Data Description

The data consists of files obtained from different sources:

* `contract.csv` — contract information
* `personal.csv` — the client's personal data
* `internet.csv` — information about Internet services
* `phone.csv` — information about telephone services

In each file, the column `customerID` contains a unique code assigned to each client.

The contract information is valid as of February 1, 2020.

## Notes

* An acknowledgement that ideally the evaluation metric for this project should've been more than just AUC-ROC. Accuracy score would've been included as an additional metric if I were to revisit this project

## Tools

* Pandas, NumPy, Seaborn, scikit-learn, XGBoost, LightGBM, CatBoost
