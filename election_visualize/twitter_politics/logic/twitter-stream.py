import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.api import API
import urllib
import os
import pandas as pd


access_token = "1431036625-KNRi0T7C0uflq1LmxejpZcPvjpQc8MAoxlqco5f"
access_token_secret = "LGbiEORzCTLdEGGLOHD9TSa92VxewJb1KBSWfUZ0dOt3p"
consumer_key = "ltanRMHcXoU8DgTLktTItfUWK"
consumer_secret = "XRBj0dTbxjkYntsvsEsB53XqE8pKyxQaWduN0K9DuFgwY4HkCE"
link = "https://stream.twitter.com/1.1/statuses/sample.json"
start_time = time.time()

search_terms = []
with open('portfolio.txt', 'r') as cur_portfolio:
  for p in cur_portfolio:
    search_terms.append(p.strip())


class listener(StreamListener):
	def __init__(self, start_time, time_limit=60):
		self.time = start_time
		self.limit = time_limit
	def on_data(self, data):
		while (time.time() - self.time) < self.limit:
			try:
				saveFile = open('raw_tweets.json', 'a')
				saveFile.write(data)
				saveFile.write('\n')
				saveFile.close()
				return True 
			except BaseException as e:

				print('failed ondata,', str(e))
				time.sleep(5)
				pass 
		exit()
 
	def on_error(self, status):
		print(status)


auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)
listener_object = listener(start_time, time_limit=20)
api = API(auth)
twitterStream = Stream(auth = api.auth, listener=listener_object) #initialize Stream object with a time out limit
twitterStream.filter(track=search_terms, languages=['en'])  #call the filter method to run the Stream Object






