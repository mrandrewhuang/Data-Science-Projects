# Project: Gold Ore Recovery

## Description

For this project, I had to prepare a prototype of a ML model to predict the amount of gold recoverable from gold ore. The datasets provided included data from ore extraction and purification processes.

In order to solve the problem, I needed to use a new metric, *sMAPE*, similar to *MAE*, but expressed in relative values instead of absolute ones.

## Data Description

### Technological process

* *Rougher feed* — raw material
* *Rougher additions (or reagent additions)* — flotation reagents: *Xanthate, Sulphate, Depressant*
    * *Xanthate* — promoter or flotation activator;
    * *Sulphate* — sodium sulphide for this particular process;
    * *Depressant* — sodium silicate.
* *Rougher process* — flotation
* *Rougher tails* — product residues
* *Float banks* — flotation unit
* *Cleaner process* — purification
* *Rougher Au* — rougher gold concentrate
* *Final Au* — final gold concentrate

### Parameters of stages

* *air amount* — volume of air
* *fluid levels*
* *feed size* — feed particle size
* *feed rate*

## Notes

* The datasets are excluded here as they was too large to upload

## Tools

* Pandas, NumPy, Seaborn, scikit-learn
