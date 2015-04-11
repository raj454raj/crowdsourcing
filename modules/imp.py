APP_URL = "http://disres.pythonanywhere.com/"
PROXY = {"http": "proxy.iiit.ac.in:8080"}
mapping = {"EQ": "Earthquake",
           "FI": "Fire",
           "FL": "Flood",
           "TSU": "Tsunami",
           "CYC": "Cyclone",
           "LS": "Landslide",
           }

def getdatetime(x):
    import datetime
    return str(datetime.datetime.strptime(x.replace("T", " ").replace("Z", ""), "%Y-%m-%d %H:%M:%S.%f")).split(".")[0]
