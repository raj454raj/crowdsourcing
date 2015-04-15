import json, requests
imp = local_import('imp')

def index():
    if session.user is None:
        response.flash = "Please Login!"

    form = FORM(TABLE(TR(TD("User Name: "), TD(INPUT(_name="username",
                                                     requires=IS_NOT_EMPTY()))),
                      TR(TD("Password: "), TD(INPUT(_name="password", _type="password",
                                                    requires=IS_NOT_EMPTY()))),
                      TR(TD(INPUT(_type="submit")))))

    if form.accepts(request.post_vars):

        session.client = requests.session()
        url = imp.APP_URL + "auth/"
        data = json.dumps(request.vars)
        headers = {'content-type': 'application/json'}
        r = session.client.post(url,
                                data=data,
                                headers=headers,
                                cookies=session.cookies,
                                proxies=imp.PROXY)
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
            redirect(URL(c="default", f="index"))
        else:
            response.flash = "Please Login!"

    return dict(form=form)

def logout():

    url = imp.APP_URL  + "auth/"
    r = requests.delete(url,
                        headers=session.headers,
                        cookies=session.cookies,
                        proxies=imp.PROXY)
    session.user = None
    redirect(URL(c="login", f="index"))
