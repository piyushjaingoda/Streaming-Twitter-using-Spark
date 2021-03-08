# Streaming Twitter using Spark

This project is about processing real time data using Spark streaming API with the help of Python. We will be streaming real time tweets. The basic requirement is to get access to the streaming data; in this case, real time tweets. Twitter provides a very convenient API to fetch tweets in a streaming manner.Receive_Tweets.py is the python script which connects to the Twitter using twitter streaming API. The script will require your twitter authentication tokens(keys). Twitter_App.py reads the tweets from the twitter and saves the tweet in the parquet format.
