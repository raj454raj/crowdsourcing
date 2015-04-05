def index():
    form = FORM(TABLE(TR(TD("Aid-type: "), TD(SELECT(OPTION("Rescue", _value="R"),
                                                     OPTION("Shelter", _value="S"),
                                                     OPTION("Medical", _value="M"),
                                                     _name="aid_type"))),
                      TR(TD("Response message: "), TD(TEXTAREA(_name="response"))),
                      TR(INPUT(_type="submit"))),
                _action=URL(c="response", f="respond", args=[request.args[0]]))

    return dict(form=form)

def respond():
    import requests, json
    data = dict(request.vars)
    data["sos"] = request.args[0]
    url = "http://127.0.0.1:9000/responses/"
    headers = {'content-type': 'application/json'}
    r = session.client.post(url, data=json.dumps(data), headers=session.headers, cookies=session.cookies)
    redirect(URL("default", "index"))


