# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests, urllib
from requests_oauthlib import OAuth1
from pytz import timezone
from datetime import datetime
import HTMLParser

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "YV2UtuGINWMJ3rqblX2dSOmcG"
CONSUMER_SECRET = "3X8qloM9kWovmWo3eHxLvVPodSvpBGUuf590lDH2qQvjVTzyGA"

OAUTH_TOKEN = "2884644275-OyciI4HVHyaMQhyCYwNBKYKZS2nNjd0UgEfYMPg"
OAUTH_TOKEN_SECRET = "16Tj3u1OMCln4gqGP1al02CV82fx930FGznjgHct6Vp4h"

proxy = {"http": "http://proxy.iiit.ac.in:8080", "https" : "https://proxy.iiit.ac.in:8080"}

INSTAGRAM_ACCESS_TOKEN = "1836108388.483db0f.2677865148ef43758ea27166ec0241cc"

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
    instagram_list = []
    search_query = None
    if request.vars:
        network = request.vars['network']
        search_query = request.vars['search']
        if network == "twitter":
            url = "https://api.twitter.com/1.1/search/tweets.json?q="+urllib.quote(search_query, '')+"&count=100&result_type=recent"
            oauth = __get_oauth__()
            r = requests.get(url = url, auth = oauth, proxies = proxy)
            r = r.json()
            tweet_list = r['statuses']
        elif network == "instagram":
            if search_query.find(' ') > 0:
                search_query = search_query[:search_query.find(' ')]
            url = "https://api.instagram.com/v1/tags/" + search_query + "/media/recent?access_token=" + INSTAGRAM_ACCESS_TOKEN + "&count=100"
            r = requests.get(url = url, proxies = proxy)
            r = r.json()
            instagram_list = r['data']
    form = FORM(TABLE(TR(TD(INPUT(_name="search", _placeholder="Enter keywords", _value=search_query), _style="vertical-align: middle;"), TD(TAG['button']('Search Twitter ', IMG(_src="static/images/twitter.png"), _type="submit", _value="twitter", _class="btn btn-xs btn-info", _name="network")), TD(TAG['button']('Search Instagram ', IMG(_src="static/images/instagram.png"), _type="submit", _value="instagram", _class="btn btn-xs btn-danger", _name="network")))), _method="GET")
    t = TABLE(_class="table-striped table-condensed")
    for i in tweet_list:
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
        t.append(TR(TD(IMG(_src=i['user']['profile_image_url']), _style="vertical-align: middle;"), TD(H6(i['user']['name']), A("@"+username, _href="http://twitter.com/"+username))))
        if i.get('retweeted_status', None) is not None:
            tweet = MARKMIN(HTMLParser.HTMLParser().unescape("RT @" + i['retweeted_status']['user']['screen_name'] + ": " + i['retweeted_status']['text']))
        else:    
            tweet = MARKMIN(HTMLParser.HTMLParser().unescape(i['text']))
        t.append(TR(TD(), TD(tweet, DIV(the_image, P(ist_created_at, _class="text-muted small")))))
    for i in instagram_list:
        username = i['user']['username']
        created_at = float(i['created_time'])
        ist_created_at = datetime.fromtimestamp(created_at).strftime('at %H:%M on %a, %b %d, %Y')
        t.append(TR(TD(IMG(_src=i['user']['profile_picture']), _style="vertical-align: middle;"), TD(H6(i['user']['full_name']), A("@"+username, _href="http://instagram.com/"+username))))
        caption = i.get('caption', None)
        if caption is not None:
            caption = MARKMIN(HTMLParser.HTMLParser().unescape(caption['text']))
        else:
            caption = MARKMIN('')
        if i['type'] == 'video':
            image_object = i['images']['low_resolution']
            video_object = i['videos'].get('low_bandwidth', None)
            if video_object is None:
                video_object = i['videos'].get('low_resolution', None)
            if video_object is None:
                video_object = i['videos'].get('standard_resolution', None)
            t.append(TR(TD(), TD(caption, DIV(TAG['video'](_src=video_object['url'], _width=video_object['width'], _height=video_object['height'], _controls="True", _poster=image_object['url']), P(ist_created_at, _class="text-muted small")))))
        elif i['type'] == 'image':
            image_object = i['images']['low_resolution']
            t.append(TR(TD(), TD(caption, DIV(IMG(_src=image_object['url'], _width=image_object['width'], _height=image_object['height']), P(ist_created_at, _class="text-muted small")))))
    return dict(t = t, form = form, search_query = search_query)
    
