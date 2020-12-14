
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
# #"LunarCRiSH"
# tweet_id=""
# tweets=tweepy.Cursor(api.search, q='to:' + name , result_type='recent', timeout=999999).items(1)
# for tweet in tweets:
#     print(tweet.text,"\n")


# name = 'LunarCRUSH'
# tweet_id = '1270923526690664448'
# replies=[]
# t = tweepy.Cursor(api.search,q='to:'+name, result_type='recent').items(10)
# if not t:
#     for i in t:
#         print(i)
# tweets =  tweepy.Cursor(api.search,q='to:'+name).items(100)
tweets=api.search(q=name, count=222)
#------
for tweet in tweets:
     print(f"{tweet.created_at}   -- id is ->{tweet.in_reply_to_status_id_str} ==>{tweet.user.name} ===: {tweet.text}\n\n")
  
# import tweepy, datetime, time

# def get_tweets(api, username):
#     page = 1
#     deadend = False
#     while True:
#         tweets = api.user_timeline(username, page = page)

#         for tweet in tweets:
#             if (datetime.datetime.now() - tweet.created_at).days < 1:
#                 #Do processing here:

#                 print tweet.text.encode("utf-8")
#             else:
#                 deadend = True
#                 return
#         if not deadend:
#             page+=1
#             time.sleep(500)

# get_tweets(api, "anmoluppal366")



# import csv
# import tweepy

# # get credentials at developer.twitter.com
# auth = tweepy.OAuthHandler('API Key', 'API Secret')
# auth.set_access_token('Access Token', 'Access Token Secret')

# api = tweepy.API(auth)

# # update these for whatever tweet you want to process replies to
# name = 'patrick_oshag'
# tweet_id = '1101551802930077696'

# replies=[]
# for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
#     if hasattr(tweet, 'in_reply_to_status_id_str'):
#         if (tweet.in_reply_to_status_id_str==tweet_id):
#             replies.append(tweet)

# with open('replies_clean.csv', 'wb') as f:
#     csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
#     csv_writer.writeheader()
#     for tweet in replies:
#         row = {'user': tweet.user.screen_name, 'text': tweet.text.encode('ascii', 'ignore').replace('\n', ' ')}
#         csv_writer.writerow(row)

##https://stackoverflow.com/questions/52307443/how-to-get-the-replies-for-a-given-tweet-with-tweepy-and-python
#import sys
#replies=[]
#for tweet in tweepy.Cursor(api.search,q='to:'+name,result_type='recent',timeout=999999).items(1000):
    #if hasattr(tweet, 'in_reply_to_status_id_str'):
    #  if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
#   replies.append(tweet.text)
#print("\n\nTweet :",full_tweets.text.translate(non_bmp_map),"\n\n")
#for elements in replies:
 #   print("\nReplies :=>> ", elements)
#replies.clear()
