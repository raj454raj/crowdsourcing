def index():
    form = FORM(TABLE(TR(TD(DIV(_id="dvMap", _style="height: 450px; width:1150px")))))
    import requests, json, ast
    url = "http://127.0.0.1:9000/organisations/"
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    org_list = json.loads(r.text)
    for i in org_list:
        url = "http://127.0.0.1:9000/organisations/" + str(i["id"]) + "/"
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers=headers)
        full = json.loads(r.text)
        i["latitude"] = full["latitude"]
        i["longitude"] = full["longitude"]
        i["address"] = full["address"]
    org_list = ast.literal_eval(json.dumps(org_list))
    return dict(form=form, org_list=org_list)
