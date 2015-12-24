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

# Pass in these tokens using environment variables
# set them on the heroku app with: heroku config:set NAME="value"
# or pass them in with the command line: $ NAME="value" python file.py

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']


# Send our keys and tokens to Twitter
credentials = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
credentials.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Authenticate with Twitter to get access
the_twitter_api = tweepy.API(credentials)

last_status_dm = the_twitter_api.sent_direct_messages(count=1)

if last_status_dm:
	last_id_replied = last_status_dm[0].text
else:
	last_id_replied = None

# choose a heart
def pick_heart(heart):
	heartprint = ''

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
	return heartprint


heart = randrange(0,15)

if heart > 15:
	print('no heart this time')  
else:
	# print out the heart
	something = pick_heart(heart)
	the_twitter_api.update_status(status=something)
	print('done!')

query = '@botlovesyou'
max_tweets = 20
recent_mentions = [status for status in tweepy.Cursor(the_twitter_api.mentions_timeline, q=query, since_id=last_id_replied).items(max_tweets)]
reverse_mentions = reversed(recent_mentions)

print(reverse_mentions)

last_status_id = None

for status in reverse_mentions:
  # choose a heart
	atheart = randrange(0,15)
	sn = status.user.screen_name
	m = ("@%s " + pick_heart(atheart)) % (sn)
	print(m)
	the_twitter_api.update_status(m, status.id)
	last_status_id = str(status_id)

if last_status_id:
	the_twitter_api.send_direct_message(the_twitter_api.me().screen_name, last_status_id)

print("done messaging people")
