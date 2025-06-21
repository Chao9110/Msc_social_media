# CeraVe Reddit Discussion Analysis

This project analyzes user discussions about the skincare brand **CeraVe** on Reddit over the past five years. It combines **natural language processing (NLP)** and **sentiment analysis** to identify key topics and public sentiment trends.

## 🔍 Project Goals

- Understand how consumers talk about CeraVe online
- Identify key discussion topics using **LDA topic modeling**
- Analyze sentiment changes over time using **VADER**
- Explore post popularity in relation to sentiment and keywords

## 🛠️ Tools and Methods

- `praw` API to collect Reddit posts from skincare-related subreddits
- Data cleaning and preprocessing with `pandas` and `re`
- **Topic modeling** with `gensim` LDA
- **Sentiment analysis** with `nltk` VADER
- Visualization using `matplotlib`, `seaborn`, and `wordcloud`

## 📊 Key Findings

- Top topics include: acne treatment, product ingredients, routine recommendations, and comparisons with brands like The Ordinary.
- Posts with higher sentiment polarity (positive/negative) tended to receive more upvotes.
- Topic shifts occurred during specific years (e.g., during the pandemic and TikTok trend boosts).

## 📁 File Structure

MSc_social_media/
│
├── notebooks/
│ ├── Data_Cleaning.ipynb
│ ├── popularity_numeric.ipynb
│ └── analyze6.ipynb
│
├── data/
│ ├── CeraVe_reddit_with_sentiment.csv
│ └── CeraVe_Dominant_Topics.csv
│
└── README.md


## ⚠️ Note

- Data has been sampled to reduce size and protect original subreddit users.
- For full datasets or model files, please contact the author.

## 👩‍💻 Author

Tzu-Chia Chao  
MSc Business Analytics – University of Bristol  
[GitHub Profile](https://github.com/Chao9110)

