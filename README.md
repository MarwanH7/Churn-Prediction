# Churn-Prediction

## Introduction:
  
<div align="justify">
Customer Chrun is a problem faced by many industries such as the telecom industry, gaming industy, SaaS, retail, banking and the list goes on. For context, customer churn refers to when a person stops using a company's services or products and ceases to be a customer. The survival of any business greatly depends on its ability to retain customers and keep bringing in annual recurcing revenue. When a company's retention rate is low (Churn is high) the compay losses a percent of its cashflow and the pain is felt almost instantly. This is very expensive and unsolved chrun at high rates will hinder a company's growth and my cause bankrupcy. 
  
## Problem statment: 
  
A telecommunications company (hereby “Telco”) is experiencing a massive customer churn rate of nearly 27%. This level of churn may be enough to bankrupt a real-life company.
  
  
## Solution: 
  
  * Better products 
  * Better delivery methods 
  * Lower prices 
  * Better marketing 
  * Building great relationships
  * Great customer communications
  
  
## Project Objectives: 
  
  Focused on the last two bullet points from the solutions section, this projects objectives are:
  
  * Explore the Data to know more about the customers, this will help with relationships & communication. It will also help interprut our models resutls     & design new features.  
  * Design Machine learning models to predict the likelihood of a customer churning 
  * Deploy the software so that the company can use the probability of churn for each customer as a metric added to their original data set 
  
  
## Project Workflow (10 days timeline):
  
### First Five: 
  
   Build an end to end minimal viable product Base Model, the workflow was as follows: 
  
   * Cleaning 
   * EDA (Univariate)
   * Feature engineering (Simple)
   * Model Selection (Logistic Regression)
   * Model design and train 
   * Serialize & deploy (Single output)

### Second Five:
  
   Build an improved model 1, improve on each step from Base Model, the workflow was as follows: 
  
   * Cleaning 
   * EDA (bivariate)
   * Feature engineering (Aggregate columns)
   * Model Selection (Pipeline, GridSearch,hyperparameter turning, crossfold validation)  
   * Model design and train   
   * Serialize & deploy (Entire CSV dataset in, entire CSV dataset out with an added probability churn column)
 
  
## Data Set
  
  [IBM DataSet](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

## Exploratory Data Analysis
  
(I'll show an example of each here, if you want to see more insights pulled from EDA check out the two EDA notebooks) 
  
  
Basemodel: univariate (One variable vs Chrun target variable) 
  
  
Gender vs Chrun
  
  
![Screen Shot 2022-10-18 at 5 44 03 PM](https://user-images.githubusercontent.com/56262986/196550614-98590ca3-25b6-4921-aea3-57e9b59f9c0f.png)

  
Model 1: bivariate (Churners, feature vs feature)
  

Gender Churners vs Payment method 

![Screen Shot 2022-10-18 at 5 44 24 PM](https://user-images.githubusercontent.com/56262986/196550721-7464c093-cb4f-4e7c-a9da-94991b9db232.png)

  
Notice how females with credit cards churn numbers are greater than Males. Eventhought univariate analysis female & male churners were equal in number. Layers of exploratory data analysis allows for deeper customer understanding on many levels. 
  
  
  
## Model Evaluation Metric 
  
  I used F1 for my scoring in my models, here is breakdown of the confusion matrix from a business standpoint: 
  * TP: Customers identified as churning and actually churned
  * TN: Customers identified as staying and actually stayed. 
  * FP: Customers identified as churning but actually stayed 
  * FN: Customers identified as staying but actually churned (most expensive) 
  

## Model Selection, design, train, and results: 
  ### Basemodel: Used logistic regression with hyperparamter tunning. Results 
  
 ![Screen Shot 2022-10-18 at 5 51 26 PM](https://user-images.githubusercontent.com/56262986/196551729-813b5e43-475b-4682-9867-6f8c2c25594a.png)

  ### Model 1: Used XGB Classifier with hyperparamter tunning. Results 
  
 ![Screen Shot 2022-10-18 at 5 57 20 PM](https://user-images.githubusercontent.com/56262986/196552621-39cd16df-180e-499d-a8b2-a0a269c930bf.png)
  
F1 score and accuracy imporved to 97% after doing some more cleaning, adding aggergate feature enigeering columns such as Total Average Charges per Service, Monthly Average Charges per Service and balancing the data using oversampling & undersampling techniques(SMOTE). 
  
  
## Deployment 

  ### Base model (Flask)
  
  ![Screen Shot 2022-10-18 at 6 00 39 PM](https://user-images.githubusercontent.com/56262986/196553282-d2f6c47a-77ca-4a9c-8e08-223eda651905.png)
  
   Input each value for the 22 features. 
  
  ![Screen Shot 2022-10-18 at 6 02 22 PM](https://user-images.githubusercontent.com/56262986/196553506-05a4e9b1-c947-4a9c-896e-bda8b79b08a8.png)
  
  Get a Customer likely to churn or not and a confidence (probability)

  ### Model 1:  (Streamlit)
 
 ![Screen Shot 2022-10-18 at 5 40 25 PM](https://user-images.githubusercontent.com/56262986/196550078-fc47781e-25d3-4b02-bcb9-698ab9ab9662.png)
  
  Upload data set with original 22 features
  
 ![Screen Shot 2022-10-18 at 5 39 27 PM](https://user-images.githubusercontent.com/56262986/196549955-e5558457-6496-4c3e-8a32-223203ad5663.png)
  
Get back the same data set with the chrun probability column added for each client, this can be used by employees with access to the clients data who interact with clients on a regular basis. wether its the Marketing team , cusotmer service team, sales team, adminstration, and staff. All can utalize the probability metric to gauge the level of risk this client has for churnning and use this metric amongst other to drive better business decisions. 
  
  
  ## Future Goals for this project 
  
  * Do more exploratory analysis to gain deeper insights about the clients 
  * Improve the output of the streamlit app, to show along with the churn probability column prediction from my model the important features and where       that client falls in terms of previous segmentations from the exploratory data analysis. 



