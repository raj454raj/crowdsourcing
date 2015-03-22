def index():
    return dict()

def search():
    """
        At present search for hospitals working
        @todo: Need to complete search for all types of organisations
    """
    get_vars = request.vars
    q = get_vars['q'].lower()

    # @todo: Make this list dynamic with link to hospital contacts
    full_list = [["Hospital1", "phone1"],
                 ["Hospital2", "phone2"],
                 ["Hospital3", "phone3"],
                 ]
    searched_list = {'hospitals': []}

    for i in full_list:
        if i[0].lower().__contains__(q):
            searched_list['hospitals'].append(i)

    table = TABLE(TR(TD(B("Hospitals")),
                     TD(B("Contact details"))
                     ),
                  _class="table",
                  )

    for i in searched_list.values():
        for j in i:
            table.append(TR(TD(j[0]), TD(j[1])))
    return table
