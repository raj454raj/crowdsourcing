imp = local_import('imp')

def org():
    form = FORM(TABLE(TR(TD("Organistion Name: "), TD(INPUT(_name="org_name",
                                                            requires=IS_NOT_EMPTY()))),
                      TR(TD("Email: "), TD(INPUT(_name="email", _type="email"))),
                      TR(TD("Phone Number: "), TD(INPUT(_name="username",
                                                        requires=IS_NOT_EMPTY()))),
                      TR(TD("Password: "), TD(INPUT(_name="password", _type="password",
                                                    requires=IS_NOT_EMPTY()))),
                      TR(TD("Address: "), TD(INPUT(_name="address",
                                                   requires=IS_NOT_EMPTY()))),
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
                                  _placeholder="Latitude",
                                  requires=IS_NOT_EMPTY()),
                            INPUT(_name="longitude", _type="number",
                                  _max="180", _min="-180",
                                  _step="0.000001", _id="lon",
                                  _placeholder="Longitude",
                                  requires=IS_NOT_EMPTY())),
                         ),
                      TR(TD(), TD(DIV(_id="dvMap", _style="width:800px;height:300px;"))),
                      TR(TD("Description: "), TD(TEXTAREA(_name="description",
                                                          requires=IS_NOT_EMPTY()))),
                      TR(TD(INPUT(_type="submit", _value="Register")))
                      ))
    if form.accepts(request.post_vars):
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
        url = imp.APP_URL + "organisations/"
        data = json.dumps(request_dict)
        r = requests.post(url,
                          data=data,
                          headers=session.headers,
                          cookies=session.cookies,
                          proxies=imp.PROXY)
    return dict(form=form)

def user():

    form = FORM(TABLE(TR(TD("Phone Number: "), TD(INPUT(_name="username",
                                                        requires=IS_NOT_EMPTY()))),
                      TR(TD("Email: ", TD(INPUT(_name="email", _type="email",
                                                requires=IS_NOT_EMPTY())))),
                      TR(TD("Password: ", TD(INPUT(_name="password", _type="password",
                                                   requires=IS_NOT_EMPTY())))),
                      TR(TD(INPUT(_type="submit", _value="Register")))))

    import json, requests
    if form.accepts(request.post_vars):

        # Send HTTP request to the REST server
        url = imp.APP_URL + "users/"
        data = json.dumps(request.vars)
        r = requests.post(url,
                          data=data,
                          headers=session.headers,
                          cookies=session.cookies,
                          proxies=imp.PROXY)
        print r
        print r.text
    return dict(form=form)
