"""
A function to create citations for Books or Ebooks. Different forms of the citation will be created depending on which parameters have arguments passed to them. Each citation is compliant with APA7. 
"""

def citing_books(authors_first_name=False, authors_middle_name=False, authors_last_name=False, book_title=False, publisher=False, publishing_year=False,
                 DOI=False, alternate_description=False):
    # Author name should be LastName, first initial, middle initial 
    if (authors_last_name):
        if authors_first_name:
            first_initial = authors_first_name[0:1]
            final_author_name = authors_last_name + ", " + first_initial + "."
        if authors_middle_name:
            middle_initial = authors_middle_name[0:1]
            final_author_name = authors_last_name + ", " + first_initial + ". " + middle_initial + "."
        else:
            final_author_name = authors_last_name+ "."

    # Begin generating final citation
    # Author, date, and title missing
    if authors_last_name == False and publishing_year == False and book_title == False:
        if alternate_description:
            reference = "[" + alternate_description + "]. (n.d.), " + publisher
        else:
            return "Not enough information to generate a citation"
    # Date and title are missing    
    elif (publishing_year == False and book_title == False):
        if alternate_description:
            reference = final_author_name + ". (n.d.). [" + alternate_description + "]. " + publisher
        else:
            return "Not enough information to generate a citation"
            # Author and date are missing
    elif (authors_last_name == False and publishing_year == False):
        reference = book_title + ". (n.d.). " + publisher
        # Source is missing
    elif (publisher == False):
        return "Not enough information to generate a citation"
    # Title is missing 
    elif (book_title == False):
        reference = final_author_name + ".(" + publishing_year + "). [" + alternate_description + "]. " + publisher
    # Date is missing
    elif (publishing_year == False):
        reference = final_author_name + ". (n.d.). " + book_title + ". " + publisher + "."
    # Author is missing
    elif (authors_last_name == False):
        reference = book_title + ". (" + publishing_year + "). " + publisher + "."

    # Final reference if all info present
    else:
        reference = final_author_name + " (" + publishing_year + ")." + book_title + ". " + publisher + "."

    # DOI, optional
    if DOI:
        reference = reference + " " + DOI

    return reference

