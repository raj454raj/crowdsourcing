imp = local_import('imp')
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
    data["sos_id"] = request.args[0]
    url = imp.APP_URL + "responses/"
    r = session.client.post(url,
                            data=json.dumps(data),
                            headers=session.headers,
                            cookies=session.cookies,
                            proxies=imp.PROXY)
    redirect(URL("default", "index"))
