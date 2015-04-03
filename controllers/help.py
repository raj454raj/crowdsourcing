def index():
    return dict()

def search():

    get_vars = request.vars
    q = get_vars['q'].lower()
    searchby = get_vars['filter']
    lat = 1000
    lon = 1000
    if get_vars['lat'] and get_vars['lon']:
        lat = float(get_vars['lat'])
        lon = float(get_vars['lon'])

    # Send HTTP request to the REST server
    import requests, json
    url = "http://127.0.0.1:9000/organisations/"
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    list_organisations = json.loads(r.text)

    complete_data = {}
    temp_list = []

    for i in list_organisations:
        url = "http://127.0.0.1:9000/organisations/" + str(i["id"]) + "/"
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers=headers)
        temp_list.append(json.loads(r.text))

    type_dict = {"EQ": "Earthquake Specific",
                 "FL": "Flood Specific",
                 "TSU": "Tsunami Specific",
                 "CYC": "Cyclone Specific",
                 "FI": "Fire Station",
                 "P": "Police",
                 "H": "Hospital",
                 "NGOM": "NGO(Medical)",
                 "NGOR": "NGO(Rescue)",
                 "NGOS": "NGO(Shelter)",
                 "BB": "Blood Bank",
                 "V": "Volunteer",
                 "MISC": "Miscellaneous"}

    for i in temp_list:
        try:
            complete_data[type_dict[i["org_type"]]].append(i)
        except KeyError:
            complete_data[type_dict[i["org_type"]]] = [i]

    searched_list = {"Earthquake Specific": [],
                     "Flood Specific": [],
                     "Tsunami Specific": [],
                     "Cyclone Specific": [],
                     "Fire Station": [],
                     "Police": [],
                     "Hospital": [],
                     "NGO(Medical)": [],
                     "NGO(Rescue)": [],
                     "NGO(Shelter)": [],
                     "Blood Bank": [],
                     "Volunteer": [],
                     "Miscellaneous": []}

    rad = 5                                 # Radius for searching by coordinates lat+-rad and lon+-rad

    for i in complete_data:
        if searchby == "name":
            for j in complete_data[i]:
                if j["org_name"].lower().__contains__(q):
                    searched_list[i].append(j)
        elif searchby == "type":
            if i.lower().__contains__(q):
                searched_list[i].extend(complete_data[i])
        elif searchby == "address":
            for j in complete_data[i]:
                if j["address"].lower().__contains__(q):
                    searched_list[i].append(j)
        else:
            for j in complete_data[i]:
                if (lat - rad < float(j["latitude"]) and float(j["latitude"]) < lat + rad) and \
                   (lon - rad < float(j["longitude"]) and float(j["longitude"]) < lon + rad):
                    searched_list[i].append(j)

    table = TABLE(TR(TD(B("Organisation Name")),
                     TD(B("Organisation Type")),
                     TD(B("Contact")),
                     ),
                  _class="table",
                  )

    for i in searched_list:
        for j in searched_list[i]:
            table.append(TR(TD(j["org_name"]), TD(i), TD(j["user"]["username"])))
    return table
