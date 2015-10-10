import nltk
import tweet_gen

def clean(s):
	return s.translate(s.maketrans({ord(x) : '' for x in '.,/><!123456789'})).lower()
def canonicalize(l):
	canon_news = []
	for (words, sentiment) in l:
		filtered_words = [clean(x) for x in words.split() if len(x) >= 3]
		canon_news.append((filtered_words, sentiment))
	return canon_news

#canonicalize text

def all_words(l):
	a_words = []
	for (words, sentiment) in l:
		a_words.extend(words)
	return a_words

# This function exists for future proofing. 
# We might want to have a more advanced approach in the future.

def string_to_array(s):
	return s.split()

def extract_word_distribution(l):
	wordlist = nltk.FreqDist(l)
	return wordlist.keys()

def extract_overall_features(doc):
	doc_words = set(doc)
	word_features = extract_word_distribution(doc)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in doc_words)
	return features

def classify_string(tup, classifier):
	result = classifier.classify(extract_overall_features(string_to_array(tup[0])))
	return result

def test_accuracy(tests, classifier):
	successes = 0
	for test in tests:
		result = classify_string(test[0], classifier)
		if result != test[1]:
			print('FAILED TEST: ', test[0], 'was supposed to be', test[1], 'but was', result)
		else:
			successes += 1
	print(str(successes/len(tests)), 'success rate')


# pos_news = [('I love this car', 'positive'), ('This view is amazing', 'positive'), \
# 			('I feel great this morning', 'positive'), ('He is my best friend', 'positive')]
# neg_news = [('I do not like this car', 'negative'), ('This view is horrible', 'negative'), \
# 			('I feel tired this morning.', 'negative'), ('He is an enemy of mine', 'negative')]
pos_news, neg_news = tweet_gen.generate_tweet_lists()
test_samples = [('feel happy this morning', 'positive'), ('larry friend', 'positive'), ('not like that man', 'negative'), \
			('house not great', 'negative'), ('your song annoying', 'negative')]
all_news = canonicalize(pos_news + neg_news)
test_samples = canonicalize(test_samples)
training_data = nltk.classify.apply_features(extract_overall_features, all_news)
# now, we train the classifier.
classifier = nltk.NaiveBayesClassifier.train(training_data)
test_accuracy(test_samples, classifier)
classifier.show_most_informative_features(10)

