# Project: Used Car Estimator (Numerical Methods)

## Description

For this project, a used car sales service is developing an app to attract new customers. In the app, one can quickly find out the market value of their car. I was given access to historical sales data: technical specifications, trim versions, and prices. My goal was to build a model to determine car value. 

The client emphasized quality, speed, and training time required of the prediction. I had to compare gradient boosting methods with random forest, decision tree, and linear regression. The RMSE metric was used to evaluate the models.

To prevent excessive training times, hyperparameter tuning for the models was kept to a minimum.

## Data Description

### Features

* *DateCrawled* — date profile was downloaded from the database
* *VehicleType* — vehicle body type
* *RegistrationYear* — vehicle registration year
* *Gearbox* — gearbox type
* *Power* — power (hp)
* *Model* — vehicle model
* *Mileage* — mileage (measured in km due to dataset's regional specifics)
* *RegistrationMonth* — vehicle registration month
* *FuelType* — fuel type
* *Brand* — vehicle brand
* *NotRepaired* — vehicle repaired or not
* *DateCreated* — date of profile creation
* *NumberOfPictures* — number of vehicle pictures
* *PostalCode* — postal code of profile owner (user)
* *LastSeen* — date of the last activity of the user

### Target

* *Price* — price (Euro)

## Notes

* The datasets are excluded here as they was too large to upload

## Tools

* Pandas, NumPy, Matplotlib, scikit-learn, XGBoost, LightGBM, CatBoost
