def index():
    form = FORM(TABLE(TR(TD("Type of disaster: "), TD(SELECT("Earthquake",
                                                             "Floods",
                                                             "Landslides",
                                                            "Fire",
                                                            "Tsunami",
                                                            "Cyclones"))),
                      TR(TD("Location: "),
                         TD(INPUT(_name="lat", _type="number", _step="0.01", _max="90", _min="-90")),
                         TD(INPUT(_name="lon", _type="number", _step="0.01", _max="180", _min="-180")),
                         ),
                      ),
                INPUT(_name="submit", _type="submit", _value="Report"))
    return dict(form=form)
