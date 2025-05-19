import praw
from reddit.client import init_reddit_client
from reddit.sentiment import RedditSentimentAnalyzer
from utils.io import save_to_csv
import pandas as pd
import numpy as np
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def save_to_csv(self, results, filename="sentiment_output.csv"):
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} results to {filename}")
        return df

def main():
    song_name = "SEVEN - JungKook "
    reddit = init_reddit_client(
         client_id=os.getenv("REDDIT_CLIENT_ID"),
         client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
         user_agent=os.getenv("REDDIT_USER_AGENT"),
    )
    
    analyzer = RedditSentimentAnalyzer(reddit)
    comments = analyzer.get_comments(song_name)
    results = np.array(analyzer.analyze_comments(comments))
    analyzer.save_to_csv(results, f"./SongSentimentTool/{song_name}_sentiments.csv")

if __name__ == "__main__":
    main()
