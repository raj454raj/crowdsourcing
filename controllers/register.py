def org():

    form = FORM(TABLE(TR(TD("Organistion Name: "), TD(INPUT(_name="name"))),
                      TR(TD("Email: "), TD(INPUT(_name="email", _type="email"))),
                      TR(TD("Phone Number: "), TD(INPUT(_name="username"))),
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
                      TR(TD(INPUT(_type="submit", _value="Register")))
                      ))

    if request.vars:

        types_list = []
        request_dict = {}

        for i in request.vars:
            if request.vars[i] == "on" and len(i) <= 3:
                types_list.append(i)
            else:
                request_dict[i] = request.vars[i]
        request_dict["tags"] = []

        # Send HTTP request to the REST server
        """
        import requests, json
        url = "URL to REST server"
        data = json.dumps(request_dict)
        r = requests.post(url, data)
        """
    return dict(form=form)

def user():
    form = FORM(TABLE(TR(TD("Phone Number: "), TD(INPUT(_name="username"))),
                      TR(TD("Email: ", TD(INPUT(_name="email", _type="email")))),
                      TR(TD("Password: ", TD(INPUT(_name="password", _type="password")))),
                      TR(TD(INPUT(_type="submit", _value="Register")))))
    return dict(form=form)
