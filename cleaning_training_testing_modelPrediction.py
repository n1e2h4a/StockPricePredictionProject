import pandas as pd
import boto3

'''Pass the path of file which is in s3 bucket'''

data=pd.read_csv('s3://historicalstockfivejune2020/HistoricalQuotes.csv')

'''creating client obj for s3'''

client=boto3.client("s3")
path = "s3://historicalstockfivejune2020/HistoricalQuotes.csv"

'''Loading file from aws s3 using pandas'''

df = pd.read_csv(path)
df.head()

'''# Preprocessing DATA ANALYSIS'''

'''check/print some important information for further process'''
df.count()
df.dtypes
df.info()

'''convert string Date into Datetime format '''

df['Date'] = pd.to_datetime(df.Date)
df['Date'] = df ["Date"].dt.strftime('%m/%d/%y')
df['Date']

'''# converting the object columns to list'''

df.columns.tolist()

'''Rename the column names'''
df = df.rename(columns={df.columns[1] : 'Close'})
df = df.rename(columns={df.columns[2] : 'Volume'})
df = df.rename(columns={df.columns[3] : 'Open'})
df = df.rename(columns={df.columns[4] : 'High'})
df = df.rename(columns={df.columns[5] : 'Low'})


'''convert object column type to float and remove $ sign from the columns by two methods'''
'''Removing Dollar sign from the file by using function'''

'''def remove_dollar():
    try:
        df[df.columns[1:]] = df[df.columns[1:]].replace('[\$,]', '', regex=True).astype(float)
    except ValueError:
        print("Could not convert data to an integer.")
remove_dollar()'''

'''Removing Dollar sign from the file by using normal pandas'''

df['Close'] = df['Close'].str.replace(',','').str.replace('$','').astype('float')
df['Open'] = df['Open'].str.replace(',','').str.replace('$','').astype('float')
df['High'] = df['High'].str.replace(',','').str.replace('$','').astype('float')
df['Low'] = df['Low'].str.replace(',','').str.replace('$','').astype('float')

'''Now check the changed datatype'''

df.dtypes

'''checking null values in columns'''

df.isnull().sum()

'''Print the data after cleaning'''

print(df)

'''Here we start Data Modeling by pyspark our clean data available on 'df'''

'''First import all important libraries of pyspark for modeling process'''

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

'''Convert pandas Dataframe to pyspark Dataframe'''

sc = SparkContext()
sparkSession = SparkSession(sc)
stock_price_data = sparkSession.createDataFrame(df)
#print(stock_price_data)

'''check the dataframe schema'''
stock_price_data.printSchema()

'''Perform descriptive analytics operations'''

stock_price_data.describe().toPandas().transpose()

'''TRANSFORMATION'''

'''vectorizing the columns assembler combine all  features before training or scoring the model'''
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

featureassembler=VectorAssembler(inputCols=["Open","High","Low"],outputCol="Independent Features")

output=featureassembler.transform(stock_price_data)
output.show()
'''see the vectorized feature'''
output.select("Independent Features").show()
output.columns
'''get the sorted column'''
finalized_data=output.select("Independent Features","Close")
finalized_data.show()

'''Divide the data for Training and Testing'''

train_data,test_data=finalized_data.randomSplit([0.75,0.25])

'''BUILDING MODEL'''
'''USe linear regression alogorithm for model fiting'''

from pyspark.ml.regression import LinearRegression
regressor=LinearRegression(featuresCol='Independent Features', labelCol='Close')
regressor=regressor.fit(train_data)

lr = LinearRegression(featuresCol = 'Independent Features', labelCol='Close', maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(train_data)
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))

'''TESTING'''
'''testing the data get the accuracy by using root mean square '''

lr_predictions = lr_model.transform(test_data)
lr_predictions.select("Close","Independent Features","prediction").show(5)

'''EVALUATION'''

from pyspark.ml.evaluation import RegressionEvaluator
lr_evaluator = RegressionEvaluator(predictionCol="prediction", \
                 labelCol="Close",metricName="r2")
print("R Squared (R2) on test data = %g" % lr_evaluator.evaluate(lr_predictions))

'''Saving Model'''

from pyspark.ml.regression import LinearRegressionModel
lr_model.save("stockModel")
print("saved succesfully")


'''By using Pickle
import pickle
Pkl_Filename = "Pickle_LR_Model"
with open(Pkl_Filename, 'wb') as f:
    pickle.dump(lr_model, f)'''
