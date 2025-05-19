import praw

def init_reddit_client(client_id, client_secret, user_agent="RedditAnalyzer"):
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )