def index():
    form = FORM(TABLE(TR(TD("First Name: "), TD(INPUT(_name="fname", _type="text", 
                                                      requires=IS_NOT_EMPTY()))),
                      TR(TD("Last Name: "), TD(INPUT(_name="lname", _type="text"))),
                      TR(TD("Email: "), TD(INPUT(_name="email", _type="email",
                                                 requires=IS_NOT_EMPTY()))),
                      TR(TD("Phone Number: "), TD(INPUT(_name="phoneno"))),
                      TR(TD("Subject: "), TD(INPUT(_name="subject"))),
                      TR(TD("Message: ", TD(TEXTAREA(_name="message",
                                                     requires=IS_NOT_EMPTY())))),
                      _class="table",
                      ),
                INPUT(_type="submit", _value="Submit Response"))
    
    if form.accepts(request, session):
        response.flash = "Form Accepted"
    elif form.errors:
        response.flash = "Form has errors"
    else:
        response.flash = "Please fill the form"
    return dict(form=form)
