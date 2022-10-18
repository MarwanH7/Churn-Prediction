# Churn-Prediction

## Introduction:

<div align="justify">
Predicting flights delay has always been an interesting and challenging topic for Data Scientists. Since the problem of flight delays cost both airplane operations and consumer alot of money and time, flight delay prediction plays a key role in the aviation industry. There is much research that has been tried to develop and deploy different Machine Learning models to increase the accuracy of prediction. In this one-week Midterm Project, our goal is to take a try at this challenging problem using the data science tools we learned and practiced throughout the first half of our bootcamp. We hope to learn and gain experince from this real world problem.
  

## Introduction:
  
<div align="justify">
Customer Chrun is a problem faced by many industrie such as the telecom industry, gaming industy, Saas, retail, banking and the list goes on. For context 
Customer Churn refers to when a person stops using a company's services or products and ceases to be a customer. The survival of any business greatly depends on its ability to retain customers and keep bringing in annual recurcing revenue. When a companies retention rate is low (Churn is high) the compay losses a percent of its cashflow and the pain is felt almost instantly. This is very expensive and unsolved chrun at high rates will hinder a companies growth and my cause bankrupcy. 
  
  
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
  
  First Five: 
  
  Build an end to end minimal viable product Base Model, the workflow was as follows: 
    * Cleaning 
    * EDA (Univariate)
    * Feature engineering (Simple)
    * Model Selection (Logistic Regression)
    * Model design and train 
    * Serialize & deploy (Single output)

  Second Five:

 Build an improved model 1, improve on each step from Base Model, the workflow was as follows: 
    * Cleaning 
    * EDA  (bivariate)
    * Feature engineering (Aggregate columns)
    * Model Selection (Pipeline, GridSearch,hyperparameter turning, crossfold validation)
    * Model design and train 
    * Serialize & deploy (Entire CSV dataset in, entire CSV dataset out with an added probability churn column)
 
  
## Data Set
  
  [IBM DataSet ]([https://github.com/MarwanH7/Churn-Prediction](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)) 

## EDA (I'll show an example of each here, if you want to see more insights pulled from EDA check out the two EDA notebooks) 
  
  Basemodel univariate (One variable vs Chrun target variable) 
  
  
  
  
  Model bivariate ( Churners, two varaiables vs 
  
  
  
## Model Selection, design, train, and results: 
  
  
  Basemodel: Used logistic regression with 
  
  
  
## 
  
## Deployment 
  
  Base model 
  
  
  Model 1: 
 
 ![Screen Shot 2022-10-18 at 5 40 25 PM](https://user-images.githubusercontent.com/56262986/196550078-fc47781e-25d3-4b02-bcb9-698ab9ab9662.png)
  
  Upload data set with original 22 features
  
 ![Screen Shot 2022-10-18 at 5 39 27 PM](https://user-images.githubusercontent.com/56262986/196549955-e5558457-6496-4c3e-8a32-223203ad5663.png)
  
  Get back the same data set with the chrun probability column added for each client. 



