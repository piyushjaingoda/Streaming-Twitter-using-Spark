#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("parquetFile").getOrCreate()

output = spark.read.parquet('file:////Users/piyushjaingoda/Downloads/Twitter Analysis/parc')
output.show()
