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

 ## Step1--
 
  - Create AWS account and also create group and user for the s3 service. Give full permission to the user so that user can use this s3 service easily.
  
 ## step2 --
 
  generate the keys access key and secrete key 
  save this key in a file name 'aws'
  create the bucket with unique name
  by using python i upload the file in bucket.

- Download kafka

- Create api key on alphavantage site

- Install Flask 

## Uplaod csv file into AWS s3 bucket
To upload csv file 

**Download historical stock data from nasdaq**
- Create AWS account and s3 services
- Create aws_credential file containing all access keys with aws configure
```
- Create and run Python script for creating s3 buckets and upload csv file in it
```
