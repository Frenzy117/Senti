
# 🎵 Senti - Reddit Sentiment Analyzer for Songs

This project is a very, very, very basic Natural Language Processing (NLP) application that analyzes public sentiment on Reddit about newly released songs. It fetches user comments from relevant Reddit posts and classifies them into positive, neutral, or negative sentiments using the VADER sentiment analysis tool. 


## 🔍 Features

- Retrieves Reddit comments from specific subreddits (e.g., r/popheads)
- Filters posts by flair (e.g., "FRESH" for new releases)
- Analyzes comment sentiment using VADER SentimentIntensityAnalyzer
- Outputs results to a CSV file for further analysis
- Modular Python codebase with separation of concerns

## 📁 Project Structure

```
.
├── main.py                  # Entry point for running sentiment analysis
├── reddit/
│   ├── __init__.py
│   ├── client.py            # Reddit API client setup using PRAW
│   └── sentiment.py         # Core logic for fetching and analyzing comments
├── .env                     # Stores API credentials (not committed)
├── requirements.txt         # Project dependencies
└── README.md                # Project overview (this file)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Reddit API credentials (create a Reddit app at https://www.reddit.com/prefs/apps)

### Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/RedditSentimentAnalyzer.git
cd RedditSentimentAnalyzer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your `.env` file:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

4. Run the analysis:

```bash
python main.py
```

## 📊 Example Output

The script generates a CSV file `sentiment_output.csv` with the following fields:

- `Comment`: The Reddit comment text
- `Compound`: Overall sentiment score
- `Positive`, `Negative`, `Neutral`: Detailed sentiment breakdown

## 🧠 Why This Project?

This project is part of a larger learning journey into NLP, with the eventual goal of applying similar techniques for evaluating prompts in an AI-based prompt engineering tool. I just did this project for fun since the best way to learn and enjoy it is through a project-based experience. I wanted to get a nice idea about NLP and how Sentiment Analysis works. I will use the skills and insights from this project for Qrion, as well as my Stock Sentiment Analysis tool, soon.

## 🔮 Future Improvements

- Add YouTube comment support
- Integrate spaCy for deeper linguistic analysis
- Deploy as a Streamlit web app for interactive analysis
- Improve flair-based filtering using ML models

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


---

Built with ❤️ by [@Frenzy117](https://github.com/Frenzy117)
