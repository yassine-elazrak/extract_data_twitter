
consumer_key="yoIwFkjZGYDa49aO16XqSNqcN"
consumer_secret="gl4LQOItV7Z1aFwNrlvaiKJ3t8o8h99blMIAmnmdHxYjzjRAxO"
access_token="624310916-E7fDF2IE8P6bfY1oVFglASf6F8RnxMd3vgSXFqnZ"
access_token_secret="ID9JcoXHsDcKtvNcnmBGcCQhUlO0wmwAxBJ6LCesiUAas"


import tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication ok")
except:
    print("Error during authentication")

#public_tweets = api.home_timeline()

#for tweet in public_tweets
#print("weet.text","\n")
name = "@RAM_Maroc"
#"LunarCRiSH"
tweet_id=""
tweets=tweepy.Cursor(api.search, q='to:' + name , result_type='recent', timeout=999999).items(1)
for tweet in tweets:
    print(tweet.text,"\n")
