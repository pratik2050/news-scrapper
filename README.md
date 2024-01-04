# Financial News Scraper

## Objective

Scrape and aggregate financial news from multiple sources. 

### Note: 
This scrapper will scrap the following news websites for finance section
- Times of India
- livemint
- CNBC

## Tasks

1. Write a Python script to scrape financial news headlines from at least three different news websites.
2. Implement a method to aggregate and deduplicate news stories.
3. Store the aggregated news in a structured format (like JSON or a database).
4. Apply basic natural language processing (using libraries like NLTK or spaCy) to categorize news by sentiment or topic.

## Getting Started

### Prerequisites
- Python must be installed on machine version >= 3.8

### Clone the Repository

```
git clone https://github.com/pratik2050/news-scrapper

cd news-scrapper
```

### Initialize Virtual Environment
```bash
python -m venv venv
```

For VS Code set the interpreter to the virtual environment ```ctrl + shift + p``` select interpreter. Select one under .venv/

### Install all dependencies
```
pip install -r requirements.txt
```

### Run the scrapper
```bash
python main.py
```
