import nltk.data
import sentiment
import news_scraper
#import twitter_analyze
#nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
classifier = sentiment.load_classifier()
def articleClassifier(s):
	bodies = [a.get_text() for a in s[1]]
	positives = 0
	total = 0
	for body in bodies:
		sentences = tokenizer.tokenize(body)
		for sentence in sentences:
			if sentiment.classify_string(sentence, classifier) == 'positive':
				positives += 1
			total += 1
	if positives * 2 < total:
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
def candidateClassifier(links, articles):
	postive = 0;
	for link in links:
		article = articles[link]
		print("hello")
		reaction = articleClassifier(article)
		print("hello2")
		if reaction == 'positive':
			postive += 1

	return positive/len(links), len(links)

def generateDict():
	text_file = open("portfolio.txt", "r")
	candidates = text_file.readlines()
	states_file = open("states.csv", "r")
	states = states_file.readlines()
	finalMap = {}
	candidates, articles = news_scraper.accumulate()
	for state in states:
		state = state.strip()
		stateMap = {}
		for candidate in candidates:
			candidate = candidate.strip()
			links = candidates[candidate][state]
			stateMap[candidate] = candidateClassifier(links, articles)
		finalMap[state] = stateMap
	return finalMap


candidates, articles = news_scraper.accumulate()
links = candidates['Joe Biden']['Texas']
print(candidateClassifier(links, articles))