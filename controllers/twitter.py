# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "YV2UtuGINWMJ3rqblX2dSOmcG"
CONSUMER_SECRET = "3X8qloM9kWovmWo3eHxLvVPodSvpBGUuf590lDH2qQvjVTzyGA"

OAUTH_TOKEN = "2884644275-OyciI4HVHyaMQhyCYwNBKYKZS2nNjd0UgEfYMPg"
OAUTH_TOKEN_SECRET = "16Tj3u1OMCln4gqGP1al02CV82fx930FGznjgHct6Vp4h"

proxy = {"http": "http://proxy.iiit.ac.in:8080", "https" : "https://proxy.iiit.ac.in:8080"}

def get_oauth():
	oauth = OAuth1(CONSUMER_KEY,
	client_secret=CONSUMER_SECRET,
	resource_owner_key=OAUTH_TOKEN,
	resource_owner_secret=OAUTH_TOKEN_SECRET)
	return oauth

if __name__ == "__main__":
	url = "https://api.twitter.com/1.1/search/tweets.json?q=deepika padukone&count=100"
	oauth = get_oauth()
	r = requests.get(url = url, auth = oauth, proxies = proxy)
	r = r.json()
	for i in r['statuses']:
		username = i['user'].get('screen_name', '')
        print i
        print username + " : " + i['text']
	
