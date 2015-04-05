import os, subprocess, json
def index():
    tweet_list = []
    if request.vars:
        output = os.popen("python applications/crowdsourcing/controllers/twitter.py "+request.vars['search']).readlines()
        tweet_list = json.loads(output[0].strip())
    form = FORM(TABLE(TR(TD("Search: "), TD(INPUT(_name="search")))))
    #os.system('python applications/crowdsourcing/controllers/twitter.py')
    
    t = TABLE(_class="table")
    
    count = 0
    for i in tweet_list:
        t.append(TR(TD(i[0]), TD(i[1])))
        count = count + 1
        if count > 50:
            break
    
    return dict(t = t, form = form)
