# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setting.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yelazrak <yelazrak@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/15 14:04:50 by yelazrak          #+#    #+#              #
#    Updated: 2020/12/15 14:04:53 by yelazrak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import tweepy
import datetime
import time
import csv

consumer_key = "yoIwFkjZGYDa49aO16XqSNqcN"
consumer_secret = "gl4LQOItV7Z1aFwNrlvaiKJ3t8o8h99blMIAmnmdHxYjzjRAxO"
access_token = "624310916-E7fDF2IE8P6bfY1oVFglASf6F8RnxMd3vgSXFqnZ"
access_token_secret = "ID9JcoXHsDcKtvNcnmBGcCQhUlO0wmwAxBJ6LCesiUAas"

csv_columns = ['date_creat', 'user', 'reply']
csv_file = "replies_tweets.csv"


# print(f"--{(datetime.datetime.now() - tweet.created_at).days}yyydata_now{datetime.datetime.now()}==>yy{tweet.created_at}   -- id is ->{tweet.in_reply_to_status_id_str} ==>{tweet.user.name} ===: {tweet.text}\n\n")
# tweets=api.search(q=name, count=1000)


def get_all_replies(api, name):
    try:
        with open(csv_file, 'a+') as fd:
            writer = csv.DictWriter(fd, fieldnames=csv_columns)
            writer.writeheader()
            while True:
                # tweets = tweepy.Cursor(api.search,
                #            q=name,
                #            since="2020-12-11",
                #            until="2020-12-").items()
                tweets = tweepy.Cursor(api.search, name).items()
                for tweet in tweets:
                # if (datetime.datetime.now() - tweet.created_at).days <= 1:
                    row = {'date_creat': tweet.created_at, 'user': tweet.user.screen_name,
                           'reply': str(tweet.text).replace('\n', ' ')}
                    writer.writerow(row)
    except IOError as e:
        print("I/O error", e)


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication ok")
    except:
        print("Error during authentication")
    get_all_replies(api, "@RAM_Maroc")


if __name__ == "__main__":
    main()
