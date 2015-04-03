def index():
    form = FORM(TABLE(TR(TD("Aid-type: "), TD(SELECT(OPTION("Rescue"),
                                                     OPTION("Shelter"),
                                                     OPTION("Medical"),
                                                     _name="aidtype"))),
                      TR(TD("Response message: "), TD(TEXTAREA(_name="response"))),
                      TR(INPUT(_type="submit"))))
    return dict(form=form)
