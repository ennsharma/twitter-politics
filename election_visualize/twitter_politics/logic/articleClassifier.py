import nltk.data
import sentiment
import news_scraper
#import twitter_analyze
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
classifier = sentiment.load_classifier()
def articleClassifier(s):
	print(s)
	sentences = tokenizer.tokenize(s)
	positives = 0
	for sentence in sentences:
		if sentiment.classify_string(sentence, classifier) == 'positive':
			positives += 1
	if positives * 2 < len(sentences):
		return 'negative'
	else:
		return 'positive'

#def twitterClassifier(s, state):
#	candidates = twitter_analyze.makeMap()
#	tweets = candidates[s]
#	instate = [x[0][0] for x in tweets if x[0][1] == state]
#	classifier = sentiment.load_classifier()
#	positives = 0
#	for tweet in instate:
#		reaction = setiment.classify_string(tweet, classifier)
#		if reaction == 'postive':
#			positives += 1
#	return positives / len(instate)
def candidateClassifier(s, state):
	candidates, articles = news_scraper.accumulate()
	links = candidates[s][state]
	postive = 0;
	for link in links:
		article = articles[link]
		reaction = articleClassifier(article)
		if reaction == 'positive':
			postive += 1

	return positive/len(links), len(links)

def generateDict():
	text_file = open("portfolio.txt", "r")
	candidates = text_file.readlines()
	states_file = open("states.csv", "r")
	states = states_file.readlines()
	finalMap = {}
	for state in states:
		state = state.strip()
		stateMap = {}
		for candidate in candidates:
			candidate = candidate.strip()
			stateMap[candidate] = candidateClassifier(candidate, state)
		finalMap[state] = stateMap
	return finalMap



print(candidateClassifier('Joe Biden', 'Texas'))