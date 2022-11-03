from TweepyAuthentication import TweepyAuthentication
from NewsAPIAuthentication import NewsAPIAuthentication
from ReferencedMentions import ReferencedMentions
from NewsFetch import NewsFetch
from ReplyTweet import ReplyTweet

if __name__ == "__main__":
    client_v1 = TweepyAuthentication(version_2=False, keys_file="Keys.json").getClient()
    client_v2 = TweepyAuthentication(keys_file="Keys.json").getClient()
    client_news_api = NewsAPIAuthentication(keys_file="Keys.json").getClient()
    user = client_v2.get_user(username="got_truth101", user_auth=True)
    mentions = ReferencedMentions(client_v2, user).getMentions()
    news_fetch = NewsFetch(client_news_api, 1)

    reply_tweet = ReplyTweet(client_v1)


    for mention in mentions:
        tweet = mention[1]
        news_url = news_fetch.fetchNews(tweet)
        if news_url is not None:
            reply_tweet.post_tweet(mention[0], news_url)
        print((mention[0], news_url, tweet))