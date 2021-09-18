import numpy as np
from author_names import *


def citing_books(book_title=False, publisher=False, publishing_year=False,
                 DOI=False, alternate_description=False, **names):
    # Author name should be LastName, first initial, middle initial 
    authors_list = author_names(**names)

    # Begin generating final citation
    # Author, date, and title missing
    if authors_list == False and publishing_year == False and book_title == False:
        if alternate_description:
            reference = "[" + alternate_description + "]. (n.d.), " + publisher
        else:
            return "Not enough information to generate a citation"
    # Date and title are missing    
    elif (publishing_year == False and book_title == False):
        if alternate_description:
            reference = authors_list + ". (n.d.). [" + alternate_description + "]. " + publisher
        else:
            return "Not enough information to generate a citation"
            # Author and date are missing
    elif (authors_list == False and publishing_year == False):
        reference = book_title + ". (n.d.). " + publisher
        # Source is missing
    elif (publisher == False):
        return "Not enough information to generate a citation"
    # Title is missing 
    elif (book_title == False):
        reference = authors_list + ".(" + publishing_year + "). [" + alternate_description + "]. " + publisher
    # Date is missing
    elif (publishing_year == False):
        reference = authors_list+ " (n.d.). " + book_title + ". " + publisher + "."
    # Author is missing
    elif authors_list == False:
        reference = book_title + ". (" + publishing_year + "). " + publisher + "."
    # Final reference if all info present
    else:
        reference = authors_list + " (" + publishing_year + "). " + book_title + ". " + publisher + "."
    # DOI, optional
    if DOI:
        reference = reference + " " + DOI
    return reference

