def org():

    form = FORM(TABLE(TR(TD("Organistion Name: "), TD(INPUT(_name="org_name"))),
                      TR(TD("Email: "), TD(INPUT(_name="email", _type="email"))),
                      TR(TD("Phone Number: "), TD(INPUT(_name="username",
                                                        requires=IS_LENGTH(10)))),
                      TR(TD("Password: "), TD(INPUT(_name="password", _type="password"))),
                      TR(TD("Address: "), TD(INPUT(_name="address"))),
                      TR(TD("Type: "), TD(SELECT(OPTION("Earthquake Specific", _value="EQ"),
                                                 OPTION("Flood Specific", _value="FL"),
                                                 OPTION("Tsunami Specific", _value="TSU"),
                                                 OPTION("Cyclone Specific", _value="CYC"),
                                                 OPTION("Fire Station", _value="FI"),
                                                 OPTION("Police", _value="P"),
                                                 OPTION("Hospital", _value="H"),
                                                 OPTION("NGO(Medical)", _value="NGOM"),
                                                 OPTION("NGO(Rescue)", _value="NGOR"),
                                                 OPTION("NGO(Shelter)", _value="NGOS"),
                                                 OPTION("Blood Bank", _value="BB"),
                                                 OPTION("Miscellaneous", _value="MISC"),
                                                 _name="org_type"))),
                      TR(TD("Location: "),
                         TD(INPUT(_name="latitude", _type="number",
                                  _max="90", _min="-90",
                                  _step="0.000001", _id="lat",
                                  _placeholder="Latitude"),
                            INPUT(_name="longitude", _type="number",
                                  _max="180", _min="-180",
                                  _step="0.000001", _id="lon",
                                  _placeholder="Longitude")),
                         ),
                      TR(TD("Description: "), TD(TEXTAREA(_name="description"))),
                      TR(TD(INPUT(_type="submit", _value="Register")))
                      ))

    if request.vars:

        request_dict = {}
        for i in request.vars:
            if i not in ['username', 'password', 'email']:
                request_dict[i] = request.vars[i]
        request_dict['user'] = {'username': request.vars['username'],
                                'password': request.vars['password'],
                                'email': request.vars['email'],
                                }
        # Send HTTP request to the REST server
        import requests, json
        url = "http://127.0.0.1:9000/organisations/"
        data = json.dumps(request_dict)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=data, headers=headers)

    return dict(form=form)

def user():

    form = FORM(TABLE(TR(TD("Phone Number: "), TD(INPUT(_name="username"))),
                      TR(TD("Email: ", TD(INPUT(_name="email", _type="email")))),
                      TR(TD("Password: ", TD(INPUT(_name="password", _type="password")))),
                      TR(TD(INPUT(_type="submit", _value="Register")))))

    import json, requests
    if request.vars:

        # Send HTTP request to the REST server
        url = "http://127.0.0.1:9000/users/"
        data = json.dumps(request.vars)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=data, headers=headers)
        print r.text
    return dict(form=form)
