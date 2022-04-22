import praw
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET=os.getenv("REDDIT_SECRET")
REFRESH_TOKEN=os.getenv("REDDIT_REFRESH_TOKEN")

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    refresh_token=REFRESH_TOKEN,
    user_agent="eGirlsDiscordBot by u/RapidFireUnderpants"
)

subreddits = []
with open('src/subreddits.txt', 'r') as f:
    subreddits = [line.strip() for line in f]

data = ""
# n = 0
for sr in subreddits:
    for s in reddit.subreddit(sr).top(limit=100):
        # n += 1
        data += s.permalink + "," + s.url + "\n"

with open('src/imagelinks.txt', 'w') as f:
    # ndata = str(n) + "\n" + data
    # f.write(ndata)
    f.write(data)