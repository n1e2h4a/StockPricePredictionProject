import json
import pandas as pd
import time
import datetime
from datetime import datetime
import json
from json import loads


'''import pyspark library'''

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import hour,minute,second,col,avg,when
import pyspark.sql.functions as sql_functions

'''import kafka library for consumer'''
from kafka import KafkaConsumer

'''import kafka library for producer'''
from kafka import KafkaProducer

'''import pyspark mlib library'''
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.feature import VectorAssembler

sc = SparkContext()
sqlContext = SQLContext(sc)
try:
    Model_Path =  "stockModel"
    load_model = LinearRegressionModel.load(Model_Path)
except:
    print("model not found")

consumer  = KafkaConsumer('stock')
def stock_price_prediction():
    try:

        for message in consumer:
        #print(type(message.value))
            res_dict = json.loads(message.value.decode('utf-8'))
            data_list = list(res_dict.values())
            dataframe = pd.DataFrame([data_list], columns=['Open','Close','Volume','High','Low'])
            spark_dataframe = sqlContext.createDataFrame(dataframe)
            spark_Dataframe = spark_dataframe.selectExpr("cast(High as double) Volume",
                                   "cast(Open as double) Open",
                                   "cast(Low as double) Low",
                                    "cast(High as double) High",
                                    "cast(Close as double) Close",)
            vectorAssembler=VectorAssembler(inputCols=["Open","High","Low"],outputCol="Independent Features")

            spark_Dataframe_vect = vectorAssembler.transform(spark_Dataframe)
            spark_Dataframe_vect_features = spark_Dataframe_vect.select(['Independent Features','Close'])
            predictions = load_model.transform(spark_Dataframe_vect_features)
            predictions.select("prediction","Close","Independent Features").show()
            predict_value = predictions.select('prediction').collect()[0].__getitem__("prediction")
            close_value = predictions.select('Close').collect()[0].__getitem__('Close')
            print(message.key)
            date_time = message.key.decode('utf-8')
            return predict_value , close_value , date_time
    except:
        print("Invalid column exception")
stock_price_prediction()
