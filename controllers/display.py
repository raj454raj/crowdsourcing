imp = local_import('imp')
import requests, json, ast

def index():
    form = FORM(TABLE(TR(TD(DIV(_id="dvMap", _style="height: 450px; width:1150px")))))
    url = imp.APP_URL + "organisations/"
    r = requests.get(url, headers=session.headers, proxies=imp.PROXY)
    org_list = json.loads(r.text)
    for i in org_list:
        url = imp.APP_URL + "organisations/" + str(i["id"]) + "/"
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers=headers, proxies=imp.PROXY)
        full = json.loads(r.text)
        i["latitude"] = full["latitude"]
        i["longitude"] = full["longitude"]
        i["address"] = full["address"]
    org_list = ast.literal_eval(json.dumps(org_list))
    return dict(form=form, org_list=org_list)


def get_coordinates():

    # If getting errors with this function make sure the version
    # of the modules required is as specified(requests, bs4)

    try:
        import json # try stdlib (Python 2.6)
    except ImportError:
        try:
            import simplejson as json # try external module
        except:
            import gluon.contrib.simplejson as json # fallback to pure-Python module

    empty_dict = json.dumps(dict(country="",
                                 city="",
                                 latitude="",
                                 longitude=""))

    try:
        # Working with requests version 2.5.1
        import requests
        # Working with bs4 version 4.3.1
        from bs4 import BeautifulSoup
    except ImportError:
        return empty_dict

    # URL to get the public IP
    url = "http://ipecho.net/plain"
    try:
        # This proxy should be removed if working under internet without proxy
        r = requests.get(url, proxies={"http": "proxy.iiit.ac.in:8080"})
        my_ip = str(r.text)
    except:
        return empty_dict

    # URL to get the location corresponding to IP
    url = "http://api.hostip.info/get_html.php?ip=" + my_ip + "&position=true"
    try:
        # This proxy should be removed if working under internet without proxy
        r = requests.get(url, proxies={"http": "proxy.iiit.ac.in:8080"})
        temp_list = r.text.split("\n")
    except:
        return empty_dict

    country = temp_list[0].split(' ')[1]
    city = temp_list[1].split(' ')[1]
    latitude = temp_list[3].split(' ')[1]
    longitude = temp_list[4].split(' ')[1]

    # Set precision to 6
    latitude = "%.6f" % float(latitude)
    longitude = "%.6f" % float(longitude)

    return json.dumps(dict(country=country,
                           city=city,
                           latitude=latitude,
                           longitude=longitude))

def disaster_show():
    temp = json.loads(get_coordinates())
    dis_url = imp.APP_URL + "disasters/"
    headers = dict(session.headers)
    headers["lat"] = temp["latitude"]
    headers["lon"] = temp["longitude"]
    r = session.client.get(dis_url,
                            headers=headers,
                            cookies=session.cookies,
                            proxies=imp.PROXY)
    temp = json.loads(r.text)
    t = TABLE(TR(TH("Created"), TH("Disaster"), TH("Latitude"), TH("Longitude")),
              _class="table")
    for i in temp:
        t.append(TR(TD(imp.getdatetime(i["created"])), TD(imp.mapping[i["dis_type"]]), TD(i["latitude"]), TD(i["longitude"])))
    return dict(t=t)
