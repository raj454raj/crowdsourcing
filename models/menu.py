# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B("DisRes"),
                  _class="brand", _href=URL(c="default", f="index"))
response.title = "DisRes"
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None
#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Report Disaster'), False, URL('report', 'index'), []),
    (T('Get Help!'), False, URL('help', 'index'), []),
    (T('Contact Us'), False, URL('contact', 'index'), []),
    (T('Send Email'), False, URL('default', 'email'), []),
    (T('Register Organisation'), False, URL('register', 'org'), []),
    (T('Register User'), False, URL('register', 'user'), []),
]

if "auth" in locals(): auth.wikimenu() 
