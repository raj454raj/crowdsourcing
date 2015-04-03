def index():
    return dict()

def search():
    """
        At present search for hospitals working
        @todo: Need to complete search for all types of organisations
    """

    get_vars = request.vars
    q = get_vars['q'].lower()
    searchby = get_vars['filter']
    lat = 1000
    lon = 1000
    if get_vars['lat'] and get_vars['lon']:
        lat = float(get_vars['lat'])
        lon = float(get_vars['lon'])

    # @todo: At present complete_data is hardcoded but as the server starts working
    #         this can be taken from server
    complete_data = {"hospitals": [["Hospital1", "phone1", "email1", 10, 20, "address1"],
                                   ["Hospital2", "phone2", "email2", 20, 30, "address2"],
                                   ["Hospital3", "phone3", "email3", 30, 40, "address3"],
                                   ["Himagiri", "phone-hyd", "email4", 17, 78, "Gachibowli"],
                                   ],
                     "firestation": [["FireStation1", "phone1", "email1", 20, 30, "address1"],
                                     ["FireStation2", "phone2", "email2", 30, 40, "address2"],
                                     ["FireStation3", "phone3", "email3", 40, 50, "address3"],
                                     ["FireStation4", "phone4", "email4", 15, 80, "Gachibowli"],
                                     ],
                     "policestation": [["PoliceStation1", "phone1", "email1", 30, 40, "address1"],
                                       ["PoliceStation2", "phone2", "email2", 40, 50, "address2"],
                                       ["PoliceStation3", "phone3", "email3", 50, 60, "address3"],
                                       ["PoliceStation-hyd", "phone4", "email4", 20, 75, "Gachibowli"]
                                       ]
                     }
    # Send HTTP request to the REST server
    import requests, json
    url = "http://127.0.0.1:9000/organisations/"
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    list_organisations = json.loads(r.text)
    complete_data = {}

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

    for i in list_organisations:
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
            # @todo: Complete this - Return address from server
            """
            for j in complete_data[i]:
                if j[5].lower().__contains__(q):
                    searched_list[i].append(j)
            """
        """
        else:
            for j in complete_data[i]:
                if (lat - rad < j[3] and j[3] < lat + rad) and \
                   (lon - rad < j[4] and j[4] < lon + rad):
                    searched_list[i].append(j)
        """

    table = TABLE(TR(TD(B("Organisation Name")),
                     TD(B("Organisation Type")),
                     TD(B("Contact")),
                     ),
                  _class="table",
                  )

    for i in searched_list:
        for j in searched_list[i]:
            table.append(TR(TD(j["org_name"]), TD(i), TD(j["mobile"])))
    return table
