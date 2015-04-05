import json, requests
def index():
    if session.user is None:
        response.flash = "Please Login!"

    form = FORM(TABLE(TR(TD("User Name: "), TD(INPUT(_name="username"))),
                      TR(TD("Password: "), TD(INPUT(_name="password", _type="password"))),
                      TR(TD(INPUT(_type="submit")))))
    if request.vars:

        session.client = requests.session()
        url = "http://127.0.0.1:9000/auth/"
        data = json.dumps(request.vars)
        headers = {'content-type': 'application/json'}
        r = session.client.post(url, data=data, headers=headers)

        server_response = json.loads(r.text)
        if server_response["status"] == "invalid credentials":
            response.flash = "Invalid Credentials!"
        elif server_response["status"] == "logged in":
            session.user = server_response["user_type"]
            response.flash = "Logged in as " + session.user

            csrftoken = session.client.cookies['csrftoken']
            session.cookies = dict(session.client.cookies)
            session.headers = {'content-type': 'application/json'}
            session.headers['Referer'] = url
            session.headers["X-CSRFToken"] = csrftoken
            print session.cookies
            print session.headers
            redirect(URL(c="default", f="index"))
        else:
            response.flash = "Please Login!"

    return dict(form=form)

def logout():

    url = "http://127.0.0.1:9000/auth/"
    headers = {'content-type': 'application/json'}
    r = requests.delete(url, headers=headers)
    session.user = None
    redirect(URL(c="login", f="index"))

