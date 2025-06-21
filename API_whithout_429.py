import praw
import os
import pandas as pd
import time
import random
from dotenv import load_dotenv

load_dotenv()

# User-Agent 
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Reddit API，add requestor_delay 
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=random.choice(USER_AGENTS),
    requestor_delay=2  # Avoid 429
)


cerave_keywords = [
    "CeraVe", "CeraVe Foaming Cleanser", "CeraVe Hydrating Cleanser", "CeraVe Moisturizing Lotion", 
    "CeraVe SA Cleanser", "CeraVe Sunscreen", "CeraVe Night Cream",
    "CeraVe for dry skin", "CeraVe for oily skin", "CeraVe for acne-prone skin",
]


subreddits = ["SkincareAddiction", "beauty", "makeup", "MakeupAddiction", "TheOrdinarySkincare", "SkincareAddicts", "beautytalkph", "Skincare_Addiction"]


data = []


def retry_request(subreddit, keyword, max_retries=5):
    for attempt in range(max_retries):
        try:
            print(f"search: {keyword} in {subreddit}")
            search_results = list(reddit.subreddit(subreddit).search(keyword, limit=100))
            return search_results  
        except Exception as e:
            if "429" in str(e):  
                wait_time = (attempt + 1) * 10  
                print(f"⚠️ 429 error， will automatically retry after {wait_time} second ...")
                time.sleep(wait_time)
            else:
                print(f"⚠️ other error: {e}")
                return []
    return []

for keyword in cerave_keywords:
    for subreddit_name in subreddits:
        search_results = retry_request(subreddit_name, keyword)
        for post in search_results:
            try:
                
                post.comments.replace_more(limit=2)  
                top_comments = [comment.body for comment in post.comments[:5]]

                data.append({
                    "title": post.title,
                    "text": post.selftext,
                    "upvotes": post.score,
                    "comments": " | ".join(top_comments),
                    "timestamp": post.created_utc,
                    "url": post.url,
                    "subreddit": subreddit_name,
                    "keyword": keyword,
                })
                
                
                time.sleep(random.uniform(5, 10))

            except Exception as e:
                print(f"⚠️ 無法爬取 {keyword} in {subreddit_name}: {e}")


df = pd.DataFrame(data)
df.to_csv("data/CeraVe_reddit_full_data_V2.csv", index=False, encoding="utf-8")

print(f" {len(data)} scraped CeraVe posts in 'CeraVe_reddit_full_data_V2.csv'")
