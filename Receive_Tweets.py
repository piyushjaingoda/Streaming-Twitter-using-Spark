#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json

# request to get credentials at http://developer.twitter.com
consumer_key    = 'n6T1OKV0v9i3UYY5jNfYhv***'
consumer_secret = 'mIqxDjH3Ik0q335lqNYpiveqbWL07iJeNtzNOxr7Nh5cSXi***'
access_token    = '1603771112-2fDsRiXRqP9UpOCVk2PZdZtaPHZvTZUdWtQv***'
access_secret   = 'oUNZitGZKSbXrjjkAer3TtzshIjcc2Cm2LCXwYbfDG***'

# we create this class that inherits from the StreamListener in tweepy StreamListener
class TweetsListener(StreamListener):
  # tweet object listens for the tweets
  def __init__(self, csocket):
    self.client_socket = csocket
    
  def on_data(self, data):
    try:  
      msg = json.loads(data)
      print("new message")
      # add at the end of each tweet "t_end" 
      # if tweet is longer than 140 characters
      if "extended_tweet" in msg:
        self.client_socket.send(str(msg['extended_tweet']['full_text']+"t_end").encode('utf-8'))         
        print(msg['extended_tweet']['full_text'])
      else:
        self.client_socket.send(str(msg['text']+"t_end").encode('utf-8'))
        print(msg['text'])
      return True
    except BaseException as e:
        print("Error on_data: %s" % str(e))
    return True

  def on_error(self, status):
    print(status)
    return True

 # authentication based on the credentials
def sendData(c_socket, keyword):
  print('start sending data from Twitter to socket')
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  # start sending data from the Streaming API 
  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track = keyword, languages=["en"])


if __name__ == "__main__":
    # server (local machine) creates listening socket
    s = socket.socket()
    host = "127.0.0.1"    
    port = 5555
    s.bind((host, port))
    print('socket is ready')
    # server (local machine) listens for connections
    s.listen(4)
    print('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    sendData(c_socket, keyword = ['trump'])
