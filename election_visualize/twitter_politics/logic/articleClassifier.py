import nltk.data
import sentiment
import news_scraper
#import twitter_analyze
nltk.download('punkt')
def articleClassifier(s):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(s)
	positives = 0
	classifier = sentiment.load_classifier()
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
	candidates = news_scraper.candidateLinks()
	links = candidates[s][state]
	postive = 0;
	for link in links:
		article = news_scraper.findArticle(link)
		reaction = articleClassifier(article)
		if reaction == 'positive':
			postive += 1

	return positive/len(links)


def mostTalkedAboutClassifer(state):
	return null

print(candidateClassifier('Joe Biden', 'Texas'))