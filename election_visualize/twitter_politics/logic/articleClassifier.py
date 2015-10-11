import nltk.data
import sentiment
import news_scraper
def articleClassifier(s):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	fp = open(s)
	data = fp.read()
	sentences = tokenizer.tokenize(data)
	positives = 0
	classifier = sentiment.load_classifier()
	for sentence in sentences:
		if classify_string(sentence, classifier) == 'positive':
			positives += 1
	if positives * 2 < len(sentences):
		return 'negative'
	else:
		return 'positive'


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