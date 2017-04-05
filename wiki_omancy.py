#selenium webdriver that jumps around wikipedia, providing random insights
#thanks, Leon again for the starter code

#random word to seed
#needs to jump to a random link on the page - plan b: press random article again
#separate random function determines how many times this plays out

import time, random, ConfigParser
from selenium import webdriver
from random_words import RandomWords
# import noun_extract
from textblob import TextBlob
from bs4 import BeautifulSoup

def randWord():

	nouns = list()
	for line in open("nouns.txt", "r"):
		line = line.strip()
		# print line 
		nouns.append(line)

	word = random.choice(nouns)
	return word

def getLinks(page):
	links = []
	for link in page.find_all('a'):
		links.append(link)

		url = link.get('href')
		if url:
			if '/wiki/'in url:
				links.append(url)

	# print "what i found", links
	return links


def visitPages(page):

	links_list = getLinks(page)
	# print links_list
	chosen_link = random.choice(links_list)
	print chosen_link
	# browser.get(chosen_link)


def Main():
	
	## Initiate browser
	browser = webdriver.Chrome()

	# Go to first random wiki
	word = randWord()
	random_wiki = 'https://en.wikipedia.org/wiki/' + word

	browser.get(random_wiki)
	# print random_wiki
	page_title = browser.title
	print page_title
	page = BeautifulSoup(browser.page_source, "lxml")
	time.sleep(random.uniform(0.5,1.4)) 


	# cycle through a random number of pages
	# number_end = random.randint(3,4)
	# print "(this will cycle " + str(number_end) + " time(s))"

	for i in range(3):
		# visitPages(page)
		#plan b
		# browser.get('/wiki/special:random')
		randomPage_Element = browser.find_element_by_id("n-randompage")
		randomPage_Element.click()
		# print randomPage_Element
		page_title = browser.title
		print page_title
		time.sleep(random.uniform(3,10))
		

	browser.close()

if __name__ == '__main__':
	Main()
