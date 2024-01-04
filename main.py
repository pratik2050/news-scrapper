from scrapper import (
    scrape_news_livemint,
    scrape_news_TOI,
    scrape_news_CNBC,
    aggregate_news,
    save_to_json,
    analyze_sentiment,
)

def main():
    # URLs for scraping
    livemint_url = 'https://www.livemint.com/economy'
    TOI_url = 'https://timesofindia.indiatimes.com/business/india-business'
    CNBC_url = 'https://www.cnbc.com/finance/'

    # Scraping data from different sources
    livemint_data = scrape_news_livemint(livemint_url)
    TOI_data = scrape_news_TOI(TOI_url)
    CNBC_data = scrape_news_CNBC(CNBC_url)

    # Aggregating and deduplicating data
    aggregated_news = aggregate_news(livemint_data, TOI_data, CNBC_data)

    # Save aggregated news to a JSON file
    save_to_json(aggregated_news)

    # Analyze sentiment of the headlines
    sentiments = analyze_sentiment(aggregated_news)
    save_to_json(sentiments, "sentiments.json")


if __name__ == "__main__":
    main()
