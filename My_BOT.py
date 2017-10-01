########################
# Twitter Bot by Ahmux
# 1/10/2017
########################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from time import sleep


# Keys from your Twitter application:
CONSUMER_KEY = '*********************'          #keep the quotes,  consumer key
CONSUMER_SECRET = '********************************************'          #keep the quotes, your consumer secret key
ACCESS_KEY = '****************************************************'                #keep the quotes, raccess token
ACCESS_SECRET = '***************************************'       #keep the quotes,  access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#My account user_a informations
user = api.me()
user_a = user.screen_name
print (user_a)
followers = api.followers_ids(user_a)
friends = [user.id] + api.friends_ids(user_a)
print ("following: " + str(len(friends)))
print ("followers: ", len(followers))
unfollwers = []
for u in friends:
    if u not in followers:
        unfollowers.append(u)
print ("not following back: " , len (unfollowers))
print ("################### \n")

#searching for treds + following hashtags    
def search_keyword():

    while True:
        try:    
            trends1 = api.trends_place(23424802)  #searching for EGYPT trends
            data  = trends1[0]
            trends = data['trends']
            # grab the name from each trend
            names = [trend['name'] for trend in trends]
            for s in names:
                print (s)
                if "فولو" in s:
                    print ("\n", s)
                    keyword = s
                    for status in tweepy.Cursor(api.search, keyword).items(100):
                  #      print (status.text)
                  #      print (status.user.screen_name)
                        if status.user.id   not in friends:
                            target = status.user.id
                            print (status.user.screen_name)
                            api.create_friendship(target)
                            friends.append(target)
            print ("twitter sleeeeping zzzzzzzzzzzzzzzzzzz")
            sleep(3600 * 3)            
        except tweepy.TweepError:
            print ("errorrrrrrrrrrrrrr")
            sleep(60 * 15)
            continue
        except StopIteration:
            print ("StopIteration ..... breeeeeeeak")
            break

#NOT following back 
def unfollow_back():
    unfollowers = []
    for u in friends:
        if u not in followers:
            unfollowers.append(u)
    print ("not following back: " , len (unfollowers))

    for x in unfollowers[0:20]:     #unfollowing limits
        print (api.get_user(x).screen_name)
        api.destroy_friendship(x)       

unfollow_back()
search_keyword()







