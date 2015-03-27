def index():
    form = FORM(TABLE(TR(TD("Type of disaster: "), TD(SELECT("Earthquake",
                                                             "Floods",
                                                             "Landslides",
                                                             "Fire",
                                                             "Tsunami",
                                                             "Cyclones"))),
                      TR(TD("Location: "),
                         TD(INPUT(_name="lat", _type="number",
                                  _max="90", _min="-90",
                                  _step="0.01", _id="lat")),
                         TD(INPUT(_name="lon", _type="number",
                                  _max="180", _min="-180",
                                  _step="0.01", _id="lon")),
                         ),
                      TR(TD("Get my current coordinates: "),
                         TD(INPUT(_name="current-location", _type="checkbox",
                                  _onclick="fillCoordinates()", _id="check")),
                         ),
                      ),
                INPUT(_name="submit", _type="submit", _value="Report"))
    return dict(form=form)

def get_coordinates():

    import requests
    from bs4 import BeautifulSoup

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

    # Set precision to 2
    latitude = "%.2f" % float(latitude)
    longitude = "%.2f" % float(longitude)

    return json.dumps(dict(country=country,
                           city=city,
                           latitude=latitude,
                           longitude=longitude))
