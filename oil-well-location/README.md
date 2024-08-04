# Project: Oil Well Location (Machine Learning)

## Description

For this project, my task was to find the best location for a new well for a mining company. Geological exploration data was split into three regions. The goal was to build a model that would help pick the region with the highest profit margin by analyzing potential profit and risks using the *Bootstrapping* technique to find the distribution of profit.

I had to find average profit, the 95% confidence interval, and risk of losses (which had to be lower than 2.5%). Using the findings, I had to suggest a region for development of oil wells and justify the choice.
 
## Data Description

* *id* — unique oil well identifier
* *f0, f1, f2* — three features of points (their specific meaning is unimportant, but the features themselves are significant)
* *product* — volume of reserves in the oil well (thousand barrels)

## Tools

* Pandas, NumPy, Seaborn, scikit-learn, SciPy
