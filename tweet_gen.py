import os
import csv

def parse_stanford_data_1(pos_path, neg_path):
	print("Parsing Stanford_1 Database...")
	pos_tweets, neg_tweets = [], []
	for _, _, files in os.walk(pos_path):
		for filename in files:
			f = open(pos_path + filename, 'r')
			pos_tweets.append((f.read(), 'positive'))
			f.close()

	for _, _, files in os.walk(neg_path):
		for filename in files:
			f = open(neg_path + filename, 'r')
			neg_tweets.append((f.read(), 'negative'))
			f.close()
	print("Done.")
	print("....................")
	return pos_tweets, neg_tweets

# NOTE: This function parses data obtained from Sentiment140
def parse_stanford_data_2(filename):
	print("Parsing Stanford_2 Database...")
	pos_tweets, neg_tweets = [], []
	f = open(filename, 'r', encoding='utf-8')
	reader = csv.reader(f, delimeter=',')
	for line in reader:
		if line[0] == 4:
			pos_tweets.append((line[5], 'positive'))
		elif line[0] == 0:
			neg_tweets.append((line[5]), 'negative')
	print("Done.")
	print("....................")
	f = open(filename, 'r', encoding='ISO-8859-1')
	reader = csv.reader(f)
	for line in reader:
		if int(line[0]) == 4:
			pos_tweets.append((line[5], 'positive'))
		elif int(line[0]) == 0:
			neg_tweets.append((line[5], 'negative'))
	print("Done.")
	print("....................")
	print(len(pos_tweets), len(neg_tweets))
	return pos_tweets, neg_tweets

def parse_umich_data(filename):
	print("Parsing UMich Database...")
	pos_tweets, neg_tweets = [], []
	f = open(filename, 'r')
	raw_data = [line.split('\t') for line in f]
	for sentiment, text in raw_data:
		if int(sentiment) == 1:
			pos_tweets.append((text, 'positive'))
		else:
			neg_tweets.append((text, 'negative'))
	print("Done.")
	print("....................")
	return pos_tweets, neg_tweets

def generate_tweet_lists():
	pos_tweets_stanford_1, neg_tweets_stanford_1 = parse_stanford_data_1("./data/stanford_1/pos/", "./data/stanford/neg/")
	pos_tweets_stanford_2, neg_tweets_stanford_2 = parse_stanford_data_2("./data/stanford_2/training.csv")
	pos_tweets_umich, neg_tweets_umich = parse_umich_data("./data/umich/training.txt")
	pos_tweets, neg_tweets = pos_tweets_stanford_1 + pos_tweets_stanford_2 + pos_tweets_umich, neg_tweets_stanford_1 + neg_tweets_stanford_2 + neg_tweets_umich
	
	if len(pos_tweets) > len(neg_tweets):
		pos_tweets = pos_tweets[:len(neg_tweets)]
	elif len(pos_tweets) < len(neg_tweets):
		neg_tweets = neg_tweets[:len(pos_tweets)]

	return pos_tweets, neg_tweets

