# StockPricePredictionProject

StockPricePrediction
The Project Focused on Google Stock Price on real time data.i use 5 year back Historical Google stock price data for training and built the effective model for predicting Stock prices and display data on web page using flask web application and deploy my model on AWS EC2 instance.

# Software Prerequisites:

- Python3

- Java 8,

- Kafka_2.11-1.0.0,

- Apache-zookeeper-3.5.5,

- pyspark


## Requirements:

- Create AWS account and Access keys

- model the data

- Download kafka

- Create api key on alphavantage site

- predict Live Data

- Draw graph for Actual data and Predicted data vs DateTime

- Install Flask

 - Highcharts
 
 ## Amazon WEB services Account Generation and  configure the service 

 ## Step 1 --
 
  - Create AWS account and also create group and user for the "s3" service. Give full permission to the user so that user can use this s3 service easily.
  
  - opening the terminal in ubuntu and install AwsCLI to do that run the following commands curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o         "awscliv2.zip" unzip awscliv2.zip **sudo ./aws/install Now check the aws version using command aws --version Now we have to configure the aws using command       aws configure and write the access key and security key their.
  
 ## Uplaod csv file into AWS s3 bucket

 ## Step 2 --
 
  - Generate the keys access key and secrete key 
  - Save this key in a file name 'aws'
  - Create the bucket with unique name
  - By using python upload the file in bucket.
  
  
  ## Data Reading, Cleaning and Modeling for Exploratory Data Analysis
  
  ## Step 3 --
 - AWS S3 using python script So for that we have to import boto3 and read the data using pandas.
 - Read the data first 
    * While reading the data from S3 please check the time of your vm and actual time If there is any difference it may throw a error call permission Forbidden.
 - Clean the data.
    * check data types of the columns in the dataset by default is object so we have changed that to float and date to date type.
    * Rename the Columns
    * checked the null values in the columns if any null value is present better to replace it with the average of that column.
    * set the format of Datetime column
    
  - Now the data is ready for the modeling Process
  
  ## Training and testing the model 
   - First convert the pandas dataframe to Spark RDD so import SQLcontext and Sparkcontext from pyspark and convert the dataframe to spark RDD
   - import pyspark mlib library so that we can use all the facilities of machine learning
   - import vector assembler . it make all the independent variables to a single column called  Independent features.
   - splitting the data set in ratio in such a way that training should give more data and testing should give less data.so that we get accurate model
   - Linear Regression algorithm on the dataset columns Independent features and target variable close and we have to fit the model on train_data
   - Trained the model with .99% accuracy.
   
   ----Now Model is Ready---
   
## Kafka and Zookeeper

 Apache Kafka is a community distributed event streaming platform capable of handling trillions of events a day. Initially conceived as a messaging queue, Kafka is based on an abstraction of a distributed commit log. Since being created and open sourced by LinkedIn in 2011, Kafka has quickly evolved from messaging queue to a full-fledged event streaming platform.

 Zookeeper keeps track of status of the Kafka cluster nodes and it also keeps track of Kafka topics, partitions etc. Zookeeper it self is allowing multiple  clients to perform simultaneous reads and writes and acts as a shared configuration service within the system.
## Kafka Installation
- Install Java
```- wget http://www-us.apache.org/dist/kafka/2.4.0/kafka_2.13-2.4.0.tgz
```
 


## Alpha Vantage

- Create api key on alphavantage site

- Install Flask 

To upload csv file 

**Download historical stock data from nasdaq**
- Create AWS account and s3 services
- Create aws_credential file containing all access keys with aws configure
```
- Create and run Python script for creating s3 buckets and upload csv file in it
```
