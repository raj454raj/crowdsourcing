import os
def index():
    os.system('python applications/crowdsourcing/controllers/twitter.py')
    f = open('applications/crowdsourcing/controllers/temp', 'r')
    tweet_list = []
    for i in f.readlines():
        tweet_list.append(i)
    return dict(tweet_list  = tweet_list)

