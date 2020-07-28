# StockPricePredictionProject

StockPricePrediction
The Project Focused on Google Stock Price on real time data.i use 5 year back Historical Google stock price data for training and built the effective model for predicting Stock prices and display data on web page using flask web application and deploy my model on AWS EC2 instance.

<img src=captured.gif>


# Software Prerequisites:

- Python3

- Java 8,

- Kafka_2.11-1.0.0,

- Apache-zookeeper-3.5.5,

- pyspark

- refer requirements.txt


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
  
  ## Step 4
  ## Training and testing the model 
   - First convert the pandas dataframe to Spark RDD so import SQLcontext and Sparkcontext from pyspark and convert the dataframe to spark RDD
   - import pyspark mlib library so that we can use all the facilities of machine learning
   - import vector assembler . it make all the independent variables to a single column called  Independent features.
   - splitting the data set in ratio in such a way that training should give more data and testing should give less data.so that we get accurate model
   - Linear Regression algorithm on the dataset columns Independent features and target variable close and we have to fit the model on train_data
   - Trained the model with .99% accuracy.
   
   ----Now Model is Ready---
   
## Alpha Vantage
- It is a leading provider of Free API’s for real time and historical data on stocks We have to register with this it will generate a key for us and we have to   - copy that key and save that file in our project directory.
   
   
## Kafka and Zookeeper

- Apache Kafka is a community distributed event streaming platform capable of handling trillions of events a day. Initially conceived as a messaging queue, Kafka - is based on an abstraction of a distributed commit log. Since being created and open sourced by LinkedIn in 2011, Kafka has quickly evolved from messaging queue - to a full-fledged event streaming platform.

- Zookeeper keeps track of status of the Kafka cluster nodes and it also keeps track of Kafka topics, partitions etc. Zookeeper it self is allowing multiple  - - - clients to perform simultaneous reads and writes and acts as a shared configuration service within the system.
 
## Kafka Installation
- Install Java
- Install kafka
```
-wget http://www-us.apache.org/dist/kafka/2.4.0/kafka_2.13-2.4.0.tgz
```
- Then extract the archive file
```
-tar xzf kafka_2.13-2.4.0.tgz
-mv kafka_2.13-2.4.0 /usr/local/kafka
```
-Setup Kafka Systemd Unit Files
 create systemd unit files for the Zookeeper and Kafka service. This will help to manage Kafka services to start/stop using the systemctl command.
First, create systemd unit file for Zookeeper with below command:
```
vim /etc/systemd/system/zookeeper.service
```
-Add below content:

```
-[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
ExecStart=/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties
ExecStop=/usr/local/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

Save the file and close it.

```
-vim /etc/systemd/system/kafka.service
```
Add the below content. Make sure to set the correct JAVA_HOME path as per the Java installed on your system.

```
-[Unit]
Description=Apache Kafka Server
Documentation=http://kafka.apache.org/documentation.html
Requires=zookeeper.service

[Service]
Type=simple
Environment="JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64"
ExecStart=/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties
ExecStop=/usr/local/kafka/bin/kafka-server-stop.sh

[Install]
WantedBy=multi-user.target
```
- Save file and close.

- Reload the systemd daemon to apply new changes.
```
-systemctl daemon-reload
```
- Start Kafka Server

Kafka required ZooKeeper so first, start a ZooKeeper server on your system. You can use the script available with Kafka to get start a single-node ZooKeeper instance.

```
- sudo systemctl start zookeeper
- sudo systemctl start kafka
- sudo systemctl status kafka
```
- create the topic "stock"
```
- cd /usr/local/kafka
- bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stock

Created topic stock
```
- cd/usr/local/kafka

- run both the command for Producer and consumer 
```
-bin/kafka-console-producer.sh --broker-list localhost:9092 --topic stock
-bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic stock --from-beginning

```
now kafka installation is completed here
- for running producer.py and consumer.py python file first start the server by using the above command.

## python script file for producer and consumer

- Create producer file 
- Create consumer file
- Load the path of the model
- Get the Actual and Predicted value 

## Install Flask 

- create html file for Graph Representation "index.html"
- import all the sorce which is required for the  representation.
- give all the chart discription this file i use highcharts because Highcharts is a charting library written in pure JavaScript, offering an easy way of adding - - interactive charts to your web site or web application.
- import the model in app file and also index file so that chart show on web.
- first run PRODUCER.py
- second run app.py

- Graph is ready http://127.0.0.1:5000/



## Deployment
- To deploy a flask application, create an EC2 instance with t2 medium and - minimum of 15GB of storage with ubuntu OS on AWS.

- Create a http security group to allow the public to view web sites.
- Download the .pem file to access the instance from the local terminal.
- To access instance from local terminal, make ssh connection
```
**ssh -i flask.pem ubuntu@<Elastic IP address of ec2 instance>
```

We can create an Elastic IP so that the ip address may be constant without changing when we start an instance.

Now update packages
```
**sudo apt-get update
```
Install git
```

**sudo apt-get install git
```
Clone the project
```
**Install pip
sudo apt-get install python3-pip
```
Now install required libraries
```
pip3 install -r requirements.txt
```
Install Gunicorn3, it is a Python Web Server Gateway Interface HTTP server.
```
**pip3 install gunicorn3
```
Configure the gunicorn3 Open flaskapp
```
**$ cd ls
```
run
```
 $ gunicorn3 app:app
``` 
Create Gunicorn as a Service
```
**Go to /etc/systemd/system/
Cd /etc/systemd/system/
$ sudo vim gunicorn3.service
**[Unit]
Description=Gunicorn service
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Flaskapp
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app
**$ sudo systemctl daemon-reload
$ sudo service gunicorn3 start
$ sudo service gunicorn3 status
```
Now Install nginx, Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
```
**sudo apt-get install nginx
```
Set up the environment as above mentioned procedures such as downloading kafka and running zookeeper and kafka server. Now going to the kafkahome and run the command to start zookeeper.properties
```
**bin/zookeeper-server-start.sh config/zookeeper.properties
```
From kafkahome now run the command to start kafka server
```
**bin/kafka-server-start.sh config/server.properties
```
Go to nginx sites-enabled directory
```
**cd /etc/nginx/sites-enabled
```
create new file
```

**sudo nano flaskapp
```
Configure following
```

**server{
    listen 8080;
    server_name <your ec2 instace elastic IP address>;
    
    location / {
          proxy_pass http://127.0.0.1:8000;
    }
}
```
Now restart nginx server
```
** sudo service nginx restart
```
Now go to the project directory and run the Prod.py in the terminal to read live data from alpha vantage and send it to the kafka server. We can check the previous jobs by using command

** jobs -l
Now run the app command using gunicorn3
```
**gunicorn3 --threads=4 app:app
```
Check the result on web using elasticip followed by 8080 port

## Job Scheduler

Create job schedule to performane operation autometically.
The Stock Price Prediction of streaming data's Graph display on webpage with aws instance, have to schedule 4 jobs.
First running two servers, zookeeper and kafka with a time gap of 5 minutes.
Running Producer and Visualization code with time gap of 5 minutes.
Create a crontab for jobs scheduling within 5 minutes.
create path files in instance to schedule jobs.
Open Instance in sysytem
Check "$ crontab -l" for list of running job schedule
create new jobs then create "crontab -e" It need Minutes(0-60), Hours(1-24), day of month(1-31), month(1-12), Week(0-6) and job ToDo or location of file Schedule to work
Job schedule to zookeeper
            01 06 * * * cd /home/ubuntu/kafka/nohup bin/zookeeper-server-start.sh config/zookeeper.properties &
                           
        2. Job schedule to kafka
             
            06 06 * * * cd /home/ubuntu/kafka/bin/kafka-server-start.sh config/server.properties

        3. Job schedule to Producer

           11 06 * * * cd python3 /home/ubuntu/Bridgelabz2020/Producer.py
        
        4. Job schedule to visulazation

           11 06 * * * cd gunicorn3 --threads=4 /home/ubuntu/Bridgelabz2020/visualization:app



## LICENSE
 (Niharika) 
 Licensed under [MIT LICENSE](LICENSE)
