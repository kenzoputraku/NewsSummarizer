# library for GUI
import tkinter as tk
# library for downloading a model
import nltk
# libary for sentiment analysis
from textblob import TextBlob
# library for summarizer
from newspaper import Article
# model for sentiment analysis
nltk.download('punkt')

url = 'https://www.reuters.com/world/us/burning-man-festival-exodus-set-start-through-drying-mud-2023-09-04/'
# Create an Article object from the url
article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

# Sentiment analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')