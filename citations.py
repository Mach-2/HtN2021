"""
A function to create citations for Books or Ebooks. Different forms of the citation will be created depending on which parameters have arguments passed to them. Each citation is compliant with APA7. 
"""

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
    elif publishing_year == False and book_title == False:
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
        reference = authors_list + " (n.d.). " + book_title + ". " + publisher + "."
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


#### Function for citing a webpage ####

def citing_webpage(publishing_year=False, publishing_month=False, publishing_day=False, title_of_webpage=False,
                   webpage_name=False, url=False, alternate_description = False, **names):
    # Author name should be LastName, first initial, middle initial
    authors_list = author_names(**names)

    # check for required values
    if url is False:
        return "Not enough information to generate a citation. Electronic sources require URL."
    if webpage_name is False: # Check for source before evaluating if source and author are the same.
        return "Not enough information to generate a citation. Please provide a website name."
    # If author and site name are the same, omit the site name from the citation
    if authors_list == webpage_name:
        webpage_name = False
        authors_list += "."

    # Create date
    if publishing_year:
        if publishing_month:
            if publishing_day:
                pubdate = "(" + publishing_year + ", " + publishing_month + " " + publishing_day + ")"
            else:
                pubdate = "(" + publishing_year + ", " + publishing_month + ")"
        else:
            pubdate = "(" + publishing_year + ")"
    else:
        pubdate = "(n.d.)"

    # Begin generating final citation
    if authors_list:
        if title_of_webpage:
            if webpage_name:
                reference = authors_list + " " + pubdate + ". " + title_of_webpage + ". " + webpage_name + ". " + url
            else:  # Webpage is the same as author
                reference = authors_list + " " + pubdate + ". " + title_of_webpage + ". " + url
        else: # title is missing, author present
            if alternate_description:
                reference = authors_list + " " + pubdate + ". [" +alternate_description + "]. " + url
            else:
                return "Not enough information to generate a citation. Please provide a description in liu of a title."
    else: # authors missing
        if title_of_webpage: # missing author
            if webpage_name:
                reference = title_of_webpage + ". " + pubdate + ". " + webpage_name + ". " + url
            else: # webpage is same as author, omit
                reference = title_of_webpage + ". " + pubdate + ". " + url
        else: # author and title missing
            if alternate_description:
                reference = "[" + alternate_description + "]. " + pubdate + ". " + webpage_name + ". " + url
            else:
                return "Not enough information to generate a citation. Please provide a description in liu of a title."
    return reference
    #
    #
    #             # Author, date, and webpage title missing
    # if authors_list is False and pubdate is False and title_of_webpage is False:
    #     if webpage_name:
    #         reference = webpage_name + ". " + url
    #     else:
    #         return "Not enough information to generate a citation"
    # # Author's name and date is missing
    # elif authors_list is False and publishing_year is False:
    #     reference = title_of_webpage + ". " + webpage_name + ". " + url
    # # Authors name and webpage title is missing:
    # elif authors_list is False and title_of_webpage is False:
    #     reference = pubdate + ". " + webpage_name + ". " + url
    # # Date and web page title is missing
    # elif title_of_webpage is False and publishing_year is False:
    #     reference = authors_list + " " + webpage_name + ". " + url
    # # Authors name is missing
    # elif authors_list is False:
    #     reference = pubdate + ". " + title_of_webpage + ". " + webpage_name + ". " + url
    # # Date is missing
    # elif pubdate is False:
    #     reference = authors_list + " " + title_of_webpage + ". " + webpage_name + ". " + url
    # # Title is missing
    # elif title_of_webpage is False:
    #     if alternate_description:
    #         reference = authors_list + " " + pubdate + ". " + alternate_description + webpage_name + ". " + url
    #     else:
    #         return "Not enough information to generate a citation"
    # # Final reference if all info present
    # else:
    #     reference = authors_list + " " + pubdate + ". " + title_of_webpage + ". " + webpage_name + ". " + url
    #
    # # Add optional webpage name and
    #
    # return reference
