#!/usr/bin/env python2
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Import the python libraries we need to
import os 
import time
import tweepy
import sys
from random import randrange



## Authentication Boilerplate

# Be sure to paste your keys and tokens in here because it won't work otherwise!
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""


# Send our keys and tokens to Twitter
credentials = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
credentials.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Authenticate with Twitter to get access
the_twitter_api = tweepy.API(credentials)

MYDIR = os.path.dirname(__file__)
fp = open(os.path.join(MYDIR, "lastid.py"), 'r')  
last_id_replied = fp.read()
fp.close()

# choose a heart
heart = randrange(0,150)
if heart == 0:
	heartprint = '♡'
if heart == 1:
	heartprint = '♥'  
if heart == 2:
	heartprint = '❤'
if heart == 3:
	heartprint = '❦'
if heart == 4:
	heartprint = '💓'
if heart == 5:
	heartprint = '💕'
if heart == 6:
	heartprint = '💖'
if heart == 7:
	heartprint = '💗'
if heart == 8:
	heartprint = '💘'
if heart == 9:
	heartprint = '💙'
if heart == 10:
	heartprint = '💚'
if heart == 11:
	heartprint = '💛'
if heart == 12:
	heartprint = '💜'
if heart == 13:
	heartprint = '💝'
if heart == 14:
	heartprint = '💞'
if heart == 15:
	heartprint = '💟'

if heart > 15:
	print('no heart this time')  
else:
# print out the heart
	something = heartprint
	the_twitter_api.update_status(status=something)
	print('done!')

## Put the code that defines the bot's behavior below

## something = "Text to be automatically tweeted."

# Tweet something 
# Note: this design means the bot quits after tweeting instead of running continuously
#the_twitter_api.update_status(status=something)

"""query = '@botlovesyou'
max_tweets = 20
recent_mentions = [status for status in tweepy.Cursor(the_twitter_api.mentions_timeline, q=query, since_id=last_id_replied).items(max_tweets)]
reverse_mentions = reversed(recent_mentions)

print(reverse_mentions)

for status in reverse_mentions:
  # choose a heart
    atheart = randrange(0,15)
    if atheart == 0:
      atheartprint = '♡'
    if atheart == 1:
      atheartprint = '♥'  
    if atheart == 2:
      atheartprint = '❤'
    if atheart == 3:
      atheartprint = '❦'
    if atheart == 4:
      atheartprint = '💓'
    if atheart == 5:
      atheartprint = '💕'
    if atheart == 6:
      atheartprint = '💖'
    if atheart == 7:
      atheartprint = '💗'
    if atheart == 8:
      atheartprint = '💘'
    if atheart == 9:
      atheartprint = '💙'
    if atheart == 10:
      atheartprint = '💚'
    if atheart == 11:
      atheartprint = '💛'
    if atheart == 12:
      atheartprint = '💜'
    if atheart == 13:
      atheartprint = '💝'
    if atheart == 14:
      atheartprint = '💞'
    if atheart == 15:
      atheartprint = '💟'
    sn = status.user.screen_name
    m = ("@%s " + atheartprint) % (sn)
    print(m)
    the_twitter_api.update_status(m, status.id)
    fp = open(os.path.join(MYDIR, "lastid.py"), 'w')
    fp.write(str(status.id))
    fp.close()
    print("done messaging people")"""