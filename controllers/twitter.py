from TwitterSearch import *

import urllib3.contrib.pyopenssl
import json, sys
urllib3.contrib.pyopenssl.inject_into_urllib3()

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(sys.argv[1:]) # let's define all words we would like to have a look for
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'YV2UtuGINWMJ3rqblX2dSOmcG',
        consumer_secret = '3X8qloM9kWovmWo3eHxLvVPodSvpBGUuf590lDH2qQvjVTzyGA',
        access_token = '2884644275-OyciI4HVHyaMQhyCYwNBKYKZS2nNjd0UgEfYMPg',
        access_token_secret = '16Tj3u1OMCln4gqGP1al02CV82fx930FGznjgHct6Vp4h',
        verify = True,
        proxy = 'https://proxy.iiit.ac.in:8080'
    )
    
  #  f = open('applications/crowdsourcing/controllers/temp', 'w')
    tweet_list = []
    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
       # f.write("@" + tweet['user']['screen_name'].encode('utf8') + ": " + tweet['text'].encode('utf8') + "\n\n")
       tweet_list.append((tweet['user']['screen_name'].encode('utf8'), tweet['text'].encode('utf8')))

    print json.dumps(tweet_list)

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print e
