import json
import pandas as pd
import re
import os

tweet_data_file = open('raw_tweets.json', 'r')
tweets_data = []
for line in tweet_data_file:
  try:
    tweet = json.loads(line)
    tweets_data.append(tweet)
  except:
    continue

search_terms, search_file = [], 'portfolio.txt'
with open(search_file, 'r') as cur_portfolio:
  for p in cur_portfolio:
    search_terms.append(p.strip())

tweets = pd.DataFrame()
def build_data_frame():
  tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
  tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))
  tweets['place'] = list(map(lambda tweet: tweet['place'] if tweet['place'] != None else None, tweets_data))
  for term in search_terms:
    tweets[term] = tweets['text'].apply(lambda tweet: word_in_text(term, tweet))

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

# {candidate: [(tweet, location)]}
candidate_tweetMap = {}
def makeMap():
  for i in range(len(tweets['text'])):
    tweet, place = tweets['text'][i], tweets['country'][i]
    for candidate in search_terms:
      if tweets[candidate][i]:
        if candidate in candidate_tweetMap:
          candidate_tweetMap[candidate].append((tweet, place))
        else:
          candidate_tweetMap[candidate] = [(tweet, place)]
  os.remove('raw_tweets.json')
  return candidate_tweetMap
  

