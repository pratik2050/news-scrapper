import os
import requests
from bs4 import BeautifulSoup
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


def scrape_news_livemint(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    #getting all h2 with class headline and has attribute data-title
    for headline_h2 in soup.find_all('h2', class_='headline', attrs={'data-title': True}):
        #getting the content of the attribute data-title
        data_title_content = headline_h2['data-title'].strip()
        headlines.append(data_title_content)

    return headlines


def scrape_news_TOI(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    
    #getting all ul with class list5
    ul_list5 = soup.find('ul', class_='list5')
    if ul_list5:
        #getting all li's inside ul
        for li_tag in ul_list5.find_all('li'):
            #headline is inside span so getting span from each li
            span_tag = li_tag.find('span', class_='w_tle')
            if span_tag:
                #each span has a tag that has the title as link
                a_tag_inside_span = span_tag.find('a')
                text_inside_a = a_tag_inside_span.text.strip() if a_tag_inside_span else None
                headlines.append(text_inside_a)

    return headlines


def scrape_news_CNBC(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []

    #getting all div with class Card-titleContainer
    for headline_h2 in soup.find_all('div', class_='Card-titleContainer'):
        #each div has a tag as its headline
        a_tag = headline_h2.find('a')
        text_inside_a = a_tag.text.strip()
        headlines.append(text_inside_a)

    return headlines


def aggregate_news(*news_sources):
    #aggregating all lists to one major list
    all_news = [news for source_news in news_sources for news in source_news]
    #removing duplicates with set
    deduplicated_news = list(set(all_news))

    return deduplicated_news


#storing the headlines in a json
def save_to_json(news, filename='output/aggregated_news.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(news, file)


#using nltk sentiment analyser for each headline
def analyze_sentiment(news):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = [sid.polarity_scores(headline) for headline in news]
    return sentiment_scores
