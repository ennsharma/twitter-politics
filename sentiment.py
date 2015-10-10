pos_news = []
neg_news = []
test_samples = []
def canonicalize(l):
	canon_news = []
	for (words, sentiment) in l:
		filtered_words = [x.lower() for x in words.split() if len(x) >= 3]
		canon_news.append((filtered_words, sentiment))
	return canon_news
canon_news(pos_news + neg_news)
canon_news(test_samples)
#canonicalize tex

def all_words(l):
	a_words = []
	for (words, sentiment) in l:
		a_words.extend(words)
	return a_words

def extract_features(l):
	wordlist = nltk.FreqDist(l)
	return wordlist.keys()