import os

def generate_tweet_lists(pos_path, neg_path):
	pos_tweets, neg_tweets = [], []
	print('Generating positive tweets: ')
	print()
	for _, _, files in os.walk(pos_path):
		for filename in files:
			print("Parsing file: " + filename)
			f = open(pos_path + filename, 'r')
			pos_tweets.append((f.read(), 'positive'))
			f.close()
	print()

	print('Generating negative tweets: ')
	print()
	for _, _, files in os.walk(neg_path):
		for filename in files:
			print("Parsing file: " + filename)
			f = open(neg_path + filename, 'r')
			neg_tweets.append((f.read(), 'negative'))
			f.close()
	return pos_tweets, neg_tweets

pos_tweets, neg_tweets = generate_tweet_lists('./train/pos/', './train/neg/')