
import numpy as np


def citing_books(authors_first_name, authors_middle_name, authors_last_name, book_title, publisher, publishing_year,
                 DOI, alternate_description):
    # Author name should be LastName, first initial, middle initial 
    if (authors_last_name):
        if authors_first_name:
            first_initial = authors_first_name[0:1]
            final_author_name = authors_last_name + ", " + first_initial + "."
        if authors_middle_name:
            middle_initial = authors_middle_name[0:1]
            final_author_name = authors_last_name + ", " + first_initial + ". " + middle_initial + "."
        else:
            final_author_name = authors_last_name

    # Begin generating final citation
    # Author, date, and title missing
    if (authors_last_name == np.nan and publishing_year == np.nan and book_title == np.nan):
        if alternate_description:
            reference = "[" + alternate_description + "]. (n.d.), " + publisher
        else:
            return "Not enough information to generate a citation"
    # Date and title are missing    
    elif (publishing_year == np.nan and book_title == np.nan):
        if alternate_description:
            reference = final_author_name + ". (n.d.). [" + alternate_description + "]. " + publisher
        else:
            return "Not enough information to generate a citation"
            # Author and date are missing
    elif (authors_last_name == np.nan and publishing_year == np.nan):
        reference = book_title + ". (n.d.). " + publisher
        # Source is missing
    elif (publisher == np.nan):
        return "Not enough information to generate a citation"
    # Title is missing 
    elif (book_title == np.nan):
        reference = final_author_name + ".(" + publishing_year + "). [" + alternate_description + "]. " + publisher
    # Date is missing
    elif (publishing_year == np.nan):
        reference = final_author_name + ". (n.d.). " + book_title + ". " + publisher + "."
    # Author is missing
    elif (authors_last_name == np.nan):
        reference = book_title + ". (" + publishing_year + "). " + publisher + "."

    # Final reference if all info present
    else:
        reference = final_author_name + " (" + publishing_year + ")." + book_title + ". " + publisher + ". "

    # DOI, optional 
    reference = reference + DOI

    return reference


print(citing_books(authors_first_name="Johann", authors_middle_name="Alejandro", authors_last_name="Maldonado",
                   book_title="bilal", publisher="Pearson", publishing_year="2011", DOI="rashid",
                   alternate_description="rashid"))