# library for GUI
import tkinter as tk
# library for downloading a model
import nltk
# libary for sentiment analysis
from textblob import TextBlob
# library for summarizer
from newspaper import Article

# model for sentiment analysis
#nltk.download('punkt')

def summarize():
    url = urltext.get('1.0', "end")
    # Create an Article object from the url
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    date.delete('1.0', 'end')
    date.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Sentiment analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    

# GUI implementation
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# title 
titleLabel = tk.Label(root, text="Title")
titleLabel.pack()
title = tk.Text(root, height=1, width=140)
# Prevent user from editing the textbox
title.config(state='disabled', bg='#dddddd')
title.pack()


# author 
authorLabel = tk.Label(root, text="Author")
authorLabel.pack()
author = tk.Text(root, height=1, width=140)
# Prevent user from editing the textbox
author.config(state='disabled', bg='#dddddd')
author.pack()

# publication date 
dateLabel = tk.Label(root, text="Publication Date")
dateLabel.pack()
date = tk.Text(root, height=1, width=140)
# Prevent user from editing the textbox
date.config(state='disabled', bg='#dddddd')
date.pack()

# Summary
summaryLabel = tk.Label(root, text="Summary")
summaryLabel.pack()
summary = tk.Text(root, height=20, width=140)
# Prevent user from editing the textbox
summary.config(state='disabled', bg='#dddddd')
summary.pack()

sentimentLabel = tk.Label(root, text="Sentiment Analysis")
sentimentLabel.pack()
sentiment = tk.Text(root, height=1, width=140)
# Prevent user from editing the textbox
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

urlLabel = tk.Label(root, text="URL")
urlLabel.pack()

urltext = tk.Text(root, height=1, width=140)
urltext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()







root.mainloop()