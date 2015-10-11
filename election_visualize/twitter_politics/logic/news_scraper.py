import json
import requests
import nltk
import urllib
from urllib.request import urlopen
import html.parser
import os
import pickle
from bs4 import BeautifulSoup

search_file, state_file = 'portfolio.txt', 'states.csv'
positions, states = [], []
candidates_stateMap, link_article = {}, {}

with open(search_file, 'r') as cur_portfolio:
	for p in cur_portfolio:
		positions.append(p.strip())

with open(state_file, 'r') as state_file:
	for s in state_file:
		states.append(s.strip())

def accumulate():
	for position in positions:
		dic = {}
		for state in states:
			results = requests.get('http://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+position+" "+state +'%20stock&start=1').text
			parsed_json = json.loads(results)
			response_json = parsed_json['responseData']['results']
			urls = [x['unescapedUrl'] for x in parsed_json['responseData']['results']]
			dic[state] = urls
			i = 0
			for url in urls:
				i += 1
				if i > 100:
					break
				try:
					html = urlopen(url)
					raw = html.read()
					soup = BeautifulSoup(raw)
					titleSoup, paraSoup = soup.findAll("title"), soup.findAll("p")
					link_article[url] = [titleSoup, paraSoup]
				except urllib.error.URLError as e:
					pass
				except urllib.IncompleteRead as e:
					pass
				# cj = cookielib.CookieJar()
				# opener = build_opener(urllib.HTTPCookieProcessor(cj))
				# request = Request(url)
				# html = opener.open(request).read()
				# break
			# break
		candidates_stateMap[position] = dic
		# break
	with open('candidates_cache.pickle', 'wb') as candidates_cache:
		pickle.dump(candidates_stateMap, candidates_cache)
	with open('articles_cache.pickle', 'wb') as articles_cache:
		pickle.dump(link_article, articles_cache)
	return candidates_stateMap, link_article	

def candidateLinks():
	if os.path.exists('candidates_cache.pickle'):
		try:
			with open('candidates_cache.pickle', 'rb') as cache_file:
				print('load cached.') 
				candidates_stateMap = pickle.load(cache_file)
		except Exception:
			candidates_stateMap, link_article = accumulate()
	else:
		candidates_stateMap, link_article = accumulate()
	return candidates_stateMap

def findArticle(link):
	if os.path.exists('articles_cache.pickle'):
		try:
			with open('articles_cache.pickle', 'rb') as article_file:
				print('load cached.') 
				link_article = pickle.load(article_file)
		except Exception:
			_, link_article = accumulate()
	else:
		_,link_article = accumulate()
	if link in link_article:
		return link_article[link]
	return 'Invalid'

