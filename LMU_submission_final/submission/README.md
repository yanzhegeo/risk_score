# COVID_Risk_Competition
The competition of getting risk scores for each city in LA county


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
File Name: COVID_Challenge.ipynb
```
### Data

The Data are all stored in their corresponding URL, so there is no need to download the data  

### Prerequisites

```
Python 3
R
```

### Installing Packages

```
Pandas
Numpy
Matplotlib.pyplot
Sklearn  
Tensorflow
Math
```

## Running the codes

```
Run each section in the file named COVID_Challenge.ipynb in the folder. 
Each section in the notebook is labelled, and there are comments explaining the code.
```

### Break down into end to end tests

A. Covid19 case prediction (Hazard measures from SEIR model)
Note that the Covid19 predicted cases (you will need later) are derived from the attached R script
detailed explanation on the prediction models and codes are avaible in the script. 
	cases_fit.csv: our model fitting and prediction on the total infected cases
	cases_fit_summary.csv: our model fitting summary
	cases_model.csv: the 10 sets of parameters of the SEIR that we use for total infected cases prediction

	deaths_fit.csv: our model fitting and prediction on the total deaths 
	deaths_fit_summary.csv: our model fitting summary
	deaths_model.csv: the 10 sets of parameters of the SEIR that we use for total deaths prediction
        
        LA County.csv: the covid19 cases infomation for LA county, obtained from https://www.tableau.com/covid-19-coronavirus-data-resources  


B. Location-based risk score (Vulnerability*Hazard)


•       Two models: one for death, one for cases

•       Predicted numbers as hazard

Hazard * vulnerability = Risk

Our innovation: we defined two types of risk: one for death and one for infection

•       locaton-based social-economic data is from here:

•       https://lahub.maps.arcgis.com/home/item.html?id=8659eeee6bf94eabb93398773aa25416&view=list#overview

```step1. classify features into groups```

•       vulnerable factors related to death cases

•       elderly

•       asthma

•       cardiovascular

•       vulnearble factors related to infected cases

•       poverty

•       traffic

•       population


```step2. get raw scores```

•       those features are measured at different unit and maginitude

•       normalize them before summarize

•       (obs - min(obs))/(max(obs) - min(obs))

•       then each entry bocomes 0 to 1

•       and take a sum to get a raw score for death vulnerablity and case vulnerabilty

•       and put the two raw score column into a sigmoid function -->two sigmoid_raw_score, one for death and one for cases

```step3. calcualte the risk score```

•       multiply each score with the corresponding predicted infected-cases or deaths for a specfic day or period. Each city would have two risk scores at a given time. The scores are dynamic.


## Authors

* **Eric Wu** 
* **Rongxing Chen**
* **Kayla Tanli**
* **Zuo Zuo**

Mentor: Richard Zhen Tang

## License

This project is licensed under the RMDS


