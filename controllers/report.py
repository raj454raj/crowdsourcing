def index():
    form = FORM(TABLE(TR(TD("Type of disaster: "), TD(SELECT("Earthquake",
                                                             "Floods",
                                                             "Landslides",
                                                             "Fire",
                                                             "Tsunami",
                                                             "Cyclones",
                                                             _name="type"))),
                      TR(TD("Location: "),
                         TD(INPUT(_name="lat", _type="number",
                                  _max="90", _min="-90",
                                  _step="0.000001", _id="lat",
                                  _placeholder="Latitude"),
                            INPUT(_name="lon", _type="number",
                                  _max="180", _min="-180",
                                  _step="0.000001", _id="lon",
                                  _placeholder="Longitude")),
                         ),
                      TR(TD("Get my current coordinates: "),
                         TD(INPUT(_name="current-location", _type="checkbox",
                                  _onclick="fillCoordinates()", _id="check")),
                         ),
                      TR(TD(), TD(DIV(_id="dvMap", _style="height:300px; width:800px"))),
                      TR(TD("Upload Image: "), TD(INPUT(_name="fileupload", _type="file"))),
                      TR(TD("Observation: "), TD(TEXTAREA(_name="observation"))),
                      TR(INPUT(_name="submit", _type="submit", _value="Report")))
                      )
    # @todo: We need to send the image to REST server
    #        as a HTTP POST request
    return dict(form=form)
