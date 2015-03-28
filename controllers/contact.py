def index():
    form = FORM(TABLE(TR(TD(B("First Name: ")), TD(INPUT(_name="fname", _type="text",_placeholder="First Name",
                                                      requires=IS_NOT_EMPTY()))),
                      TR(TD(B("Last Name: ")), TD(INPUT(_name="lname", _type="text", _placeholder="Last Name"))),
                      TR(TD(B("Email: ")), TD(INPUT(_name="email", _type="email",_placeholder="E-mail",
                                                 requires=IS_NOT_EMPTY()))),
                      TR(TD(B("Phone Number: ")), TD(INPUT(_name="phoneno", _placeholder="Phone Number"))),
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
