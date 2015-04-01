def index():
    form = FORM(TABLE(TR(TD("User Name: "), TD(INPUT(_name="username"))),
                      TR(TD("Password: "), TD(INPUT(_name="password", _type="password"))),
                      TR(TD(INPUT(_type="submit")))))
    if request.vars:
        import json, requests
        url = "http://127.0.0.1:9000/auth/"
        data = json.dumps(request.vars)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=data, headers=headers)
        print r.text
    return dict(form=form)
