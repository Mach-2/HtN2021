def author_names(**names):
    # Set up variables
    authors_list = ''
    num_authors = 0

    # How many authors in citation?
    for key in names:
        if 'ln' in key:
            num_authors += 1

    # One author
    if num_authors == 1:
        ln = "ln1"
        mn = "mn1"
        fn = "fn1"
        if ln in names:
            if fn in names:
                finitial = names[fn][0:1]
                name = names[ln] + ", " + finitial + "."
                if mn in names:
                    minitial = names[mn][0:1]
                    name = names[ln] + ", " + finitial + ". " + minitial + "."
            else:
                name = names[ln] + "."
            authors_list += name
        else:  # There are no names passed as arguments
            return False

    # 2 to twenty authors
    elif 1 < num_authors < 21:
        for auth_index in range(1, num_authors + 1):
            ln = "ln" + str(auth_index)
            mn = "mn" + str(auth_index)
            fn = "fn" + str(auth_index)
            if ln in names:
                if fn in names:
                    finitial = names[fn][0:1]
                    name = names[ln] + ", " + finitial + "."
                    if mn in names:
                        minitial = names[mn][0:1]
                        name = names[ln] + ", " + finitial + ". " + minitial + "."
                else:
                    name = names[ln] + "."
                # If this is the last author, add &
                if auth_index == num_authors:
                    authors_list += "& " + name
                else:
                    authors_list += name + ", "
            else:
                break

    # More than twenty authors
    elif num_authors > 20:
        # Add first 19 names
        for auth_index in range(1, 20):
            ln = "ln" + str(auth_index)
            mn = "mn" + str(auth_index)
            fn = "fn" + str(auth_index)
            if ln in names:
                if fn in names:
                    finitial = names[fn][0:1]
                    name = names[ln] + ", " + finitial + "."
                    if mn in names:
                        minitial = names[mn][0:1]
                        name = names[ln] + ", " + finitial + ". " + minitial + "."
                else:
                    name = names[ln] + "."
                # Add the name to the list
                authors_list += name + ", "
        # Add ellipses
        authors_list += ". . . "
        # Add last author
        ln = "ln" + str(num_authors)
        mn = "mn" + str(num_authors)
        fn = "fn" + str(num_authors)
        if ln in names:
            if fn in names:
                finitial = names[fn][0:1]
                name = names[ln] + ", " + finitial + "."
                if mn in names:
                    minitial = names[mn][0:1]
                    name = names[ln] + ", " + finitial + ". " + minitial + "."
            else:
                name = names[ln] + "."
            # Add the name to the list
            authors_list += name
    else:  # There were no authors names entered
        return False
    return authors_list


# print("Test for no authors:")
# reference = author_names()
# print(reference)
#
# print("Test for one author:")
# reference = author_names(fn1="Madison", mn1="Eleanor", ln1="Chapel")
# print(reference)
#
# print("Test for two authors:")
# reference = author_names(fn1="Madison", mn1="Eleanor", ln1="Chapel",
#                          fn2="Bilal", ln2="Rashid")
#
# print(reference)
#
# print("Test for three to twenty authors:")
# reference = author_names(fn1="Madison", mn1="Eleanor", ln1="Chapel",
#                          fn2="Johann", mn2="Alejandro", ln2="Maldonado",
#                          fn3="Bilal", ln3="Rashid")
#
# print(reference)
#
# reference = author_names(fn1="Madison", mn1="Eleanor", ln1="Chapel",
#                          fn2="Johann", mn2="Alejandro", ln2="Maldonado",
#                          fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin")
#
# print(reference)
#
# # print("Test for more than twenty authors:")
# reference = author_names(fn1="Madison", mn1="Eleanor", ln1="Chapel",
#                          fn2="Johann", mn2="Alejandro", ln2="Maldonado",
#                          fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin",
#                          fn5="Hack", mn5="The", ln5="North", fn6="Madison", mn6="Eleanor", ln6="Chapel",
#                          fn7="Johann", mn7="Alejandro", ln7="Maldonado",
#                          fn8="Bilal", ln8="Rashid", ln9="Oh", fn9="Sumin",
#                          fn10="Hack", mn10="The", ln10="North", fn11="Madison", mn11="Eleanor", ln11="Chapel",
#                          fn12="Johann", mn12="Alejandro", ln12="Maldonado",
#                          fn13="Bilal", ln13="Rashid", ln14="Oh", fn14="Sumin",
#                          fn15="Hack", mn15="The", ln15="North", fn16="Madison", mn16="Eleanor", ln16="Chapel",
#                          fn17="Johann", mn17="Alejandro", ln17="Maldonado",
#                          fn18="Bilal", ln18="Rashid", ln19="Oh", fn19="Sumin",
#                          fn20="Hack", mn20="The", ln20="North", ln21="Last", mn21="Middle", fn21="First")

# print(reference)
#
# # if (authors_last_name):
# #    if authors_first_name:
# #        first_initial = authors_first_name[0:1]
# #        final_author_name = authors_last_name + ", " + first_initial + "."
# #    if authors_middle_name:
# #        middle_initial = authors_middle_name[0:1]
# #        final_author_name = authors_last_name + ", " + first_initial + ". " + middle_initial + "."
# #    else:
# #        final_author_name = authors_last_name + "."
