# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from pytz import timezone
from datetime import datetime

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "YV2UtuGINWMJ3rqblX2dSOmcG"
CONSUMER_SECRET = "3X8qloM9kWovmWo3eHxLvVPodSvpBGUuf590lDH2qQvjVTzyGA"

OAUTH_TOKEN = "2884644275-OyciI4HVHyaMQhyCYwNBKYKZS2nNjd0UgEfYMPg"
OAUTH_TOKEN_SECRET = "16Tj3u1OMCln4gqGP1al02CV82fx930FGznjgHct6Vp4h"

proxy = {"http": "http://proxy.iiit.ac.in:8080", "https" : "https://proxy.iiit.ac.in:8080"}

def __get_oauth__():
    oauth = OAuth1(CONSUMER_KEY,
    client_secret=CONSUMER_SECRET,
    resource_owner_key=OAUTH_TOKEN,
    resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def index():
    ist = timezone('Asia/Kolkata')
    utc = timezone('UTC')
    tweet_list = []
    search_query = None
    if request.vars:
        search_query = request.vars['search']
        url = "https://api.twitter.com/1.1/search/tweets.json?q="+search_query+"&count=100"
        oauth = __get_oauth__()
        r = requests.get(url = url, auth = oauth, proxies = proxy)
        r = r.json()
        tweet_list = r['statuses']
    form = FORM(TABLE(TR(TD(), TD(INPUT(_name="search", _placeholder="Search Twitter")), TD(INPUT(_type="submit", _value="Search", _class="btn btn-info")))), _method="GET")
    t = TABLE(_class="table")
    tweet_counter = 0
    for i in tweet_list:
        tweet_counter += 1
        username = i['user'].get('screen_name', '')
        media_object = i['entities'].get('media', None)
        created_at = datetime.strptime(i['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        utc_created_at = utc.localize(created_at)
        ist_created_at = utc_created_at.astimezone(ist).strftime('at %H:%M on %a, %b %d, %Y')
        media_path = "";
        the_image = ''
        if media_object:
            media_path = media_object[0].get('media_url', '')
            the_image = IMG(_src=media_path, _height=media_object[0]['sizes']['thumb']['h'], _width=media_object[0]['sizes']['thumb']['w'])
        if i.get('retweeted_status', None) is not None:
            t.append(TR(TD(unicode(tweet_counter)+"."), TD(IMG(_src=i['user']['profile_image_url'])), TD(A("@"+username, _href="http://twitter.com/"+username)), TD(MARKMIN("RT @" + i['retweeted_status']['user']['screen_name'] + ": " + i['retweeted_status']['text']), DIV(the_image, P(ist_created_at, _class="text-muted small")))))
        else:
            t.append(TR(TD(unicode(tweet_counter)+"."), TD(IMG(_src=i['user']['profile_image_url'])), TD(A("@"+username, _href="http://twitter.com/"+username)), TD(MARKMIN(i['text']), DIV(the_image, P(ist_created_at, _class="text-muted small")))))
    return dict(t = t, form = form, search_query = search_query)
    
