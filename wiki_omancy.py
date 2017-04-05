#selenium webdriver that jumps around wikipedia, providing random insights
#thanks, Leon again for the starter code

#random word to seed
#needs to jump to a random link on the page - plan b: press random article again
#separate random function determines how many times this plays out

import time, random
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from textblob import TextBlob


# function to get all the links # not working
def get_links(page):
	links = []
	for link in page.find_all('a'):
		links.append(link)

		url = link.get('href')
		if url:
			if 'wikipedia.org/wiki/'in url:
				links.append(url)

	# print "what i found", links
	return links

# function to go to a page from list of links # not working
def visit_pages(page):

	links_list = getLinks(page)
	# print links_list
	chosen_link = random.choice(links_list)
	print chosen_link
	# browser.get(chosen_link)

def Main():
	
	## Initiate browser
	browser = webdriver.Chrome()

	# User inputs a word, goes to first page
	print "WIKIMANCY"
	print "\n"
	user_choice = str(raw_input("What do you seek the answer to?: "))
	print "\n"

	user_wiki = 'https://en.wikipedia.org/wiki/' + user_choice
	browser.get(user_wiki)
	page = BeautifulSoup(browser.page_source, "lxml")


	sentences = []

	page_text = page.p.get_text()
	sentences.append(page_text)

	time.sleep(random.uniform(2,4))


	count = 0

	# plan b - just click on the random page
	for i in range(3):
		#go to random page
		randomPage_Element = browser.find_element_by_id("n-randompage")
		randomPage_Element.click()


		count+=1
	
		asterisk = '*' 
		increase_asterisk = asterisk * count
		page_title = browser.title
		print increase_asterisk + ' ' + page_title

		# get <p> contents
		# need to determine current page
		page = BeautifulSoup(browser.page_source, "lxml")
		page_text = page.p.get_text()
		sentences.append(page_text)


		time.sleep(random.uniform(2,4))

	##PROPHECY GENERATOR
	## get verbs
	verbs = list()
	for line in open('data/verbs.txt', 'r'):
		line = line.strip()
		verbs.append(line)

	with open('data/ingWords.json') as data_file:    
	    ingWords = json.load(data_file)

	# select two random verbs
	verb1 = random.choice(verbs)
	verb2 = random.choice(ingWords)


	## Get list of nouns from scraped sentences, choose three randomly
	# create blob
	blob = TextBlob(str(sentences))

	# create new noun list
	nouns = []

	# for each noun phrase in <p>, take phrases and add to a new list
	for noun in blob.noun_phrases:
		nouns.append(noun)

	word1 = random.choice(nouns)
	word2 = random.choice(nouns)
	word3 = random.choice(nouns)

	print "\n"
	print "PROPHECY:"
	print "You will " + verb1 + " a " + word1.strip() + " when " + word2.strip() + " is " + verb2 + " with a " + word3.strip()


	browser.close()

if __name__ == '__main__':
	Main()
