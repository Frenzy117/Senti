import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

class RedditSentimentAnalyzer:
    def __init__(self, reddit_client):
        self.reddit = reddit_client
        self.analyzer = SentimentIntensityAnalyzer()

    def get_comments(self, query, subreddit="popheads", flair_filter="FRESH", max_posts=2, max_comments=50):
        #positive sentiment: compound score >= 0.05
        #neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
        #negative sentiment: compound score <= -0.05
        all_comments = []
        posts = self.reddit.subreddit(subreddit).search(query, sort="relevance", time_filter="all", limit=max_posts)
        
        for post in posts:
            if flair_filter and post.link_flair_text:
                if flair_filter.upper() not in post.link_flair_text.upper():
                    continue  # Skip non-matching flairs
            post.comments.replace_more(limit=0)
            all_comments += [c.body for c in post.comments.list()[:max_comments]]
        
        return all_comments
    
    def analyze_comments(self, comments):
        results = []
        for comment in comments:
            if (comment.find("bot") != -1):
                continue
            scores = self.analyzer.polarity_scores(comment)
            results.append([comment,scores["compound"],scores["pos"],scores["neg"],scores["neu"]])
        return results
    
    def save_to_csv(self, results, filename="sentiment_output.csv"):
        df = pd.DataFrame(np.array(results), columns=["Comment", "Compound", "Positive", "Negative", "Neutral"])
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} results to {filename}")
        return df