# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to DisRes!!!")
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())



def email():
    form = FORM(TABLE(TR(TD('Username:'), TD(INPUT(_name='name', requires=IS_NOT_EMPTY()))),
                      TR(TD('Password:'), TD(INPUT(_name='password', _type='password', requires=IS_NOT_EMPTY()))), 
                      TR(TD('Send To:'), TD(INPUT(_name='sendto', requires=IS_NOT_EMPTY()))),
                      TR(TD('Subject:'), TD(INPUT(_name='Subject', requires=IS_NOT_EMPTY()))),
                      TR(TD('Message:'), TD(TEXTAREA(_name='Message', requires=IS_NOT_EMPTY()))),
                      TR(INPUT(_type='submit', _value='SEND')),
                      ))

    if form.accepts(request,session):
        email = str(request.vars['name']) + "@students.iiit.ac.in"
        password = str(request.vars['password'])
        from gluon.tools import Mail
        mail = Mail()
        mail.settings.server = "students.iiit.ac.in:25"
        mail.settings.sender = email
        mail.settings.login = str(request.vars['name']) + ":" + password
        mail.send(to=[str(request.vars['sendto'])],
                  subject=str(request.vars['Subject']),
                  # If reply_to is omitted, then mail.settings.sender is used
                  message=str(request.vars['Message']))
        response.flash = 'Message sent'
    elif form.errors:
        response.flash = 'Error Occured'
    else:
        response.flash = 'Please fill the form'
    return dict(form=form)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
