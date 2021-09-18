""" A series of tests to evaluate that the output for different citations formats is as expected"""

import numpy as np
from author_names import *
from citations import *

print("All info present:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing Author middle name:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing Author last name:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing book title:")
print(citing_books(publisher="Four Corners", publishing_year="2021", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing publisher:")
print(citing_books(book_title="HacktheNorth 2021", publishing_year="2021", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing publishing year:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing DOI:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   alternate_description="a very neat project!", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Missing alternate description:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021", fn1="Johann", mn1="Alejandro", ln1="Maldonado"), "\n")

print("Tests for multiple authors:")
print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Madison", mn1="Eleanor", ln1="Chapel",
                   fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                   fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin"), "\n")

print(citing_books(book_title="HacktheNorth 2021", publisher="Four Corners", publishing_year="2021",
                   DOI="https://github.com/Mach-2/HtN2021",
                   alternate_description="a very neat project!", fn1="Madison", mn1="Eleanor", ln1="Chapel",
                   fn2="Johann", mn2="Alejandro", ln2="Maldonado",
                   fn3="Bilal", ln3="Rashid", ln4="Oh", fn4="Sumin",
                   fn5="Hack", mn5="The", ln5="North", fn6="Madison", mn6="Eleanor", ln6="Chapel",
                   fn7="Johann", mn7="Alejandro", ln7="Maldonado",
                   fn8="Bilal", ln8="Rashid", ln9="Oh", fn9="Sumin",
                   fn10="Hack", mn10="The", ln10="North", fn11="Madison", mn11="Eleanor", ln11="Chapel",
                   fn12="Johann", mn12="Alejandro", ln12="Maldonado",
                   fn13="Bilal", ln13="Rashid", ln14="Oh", fn14="Sumin",
                   fn15="Hack", mn15="The", ln15="North", fn16="Madison", mn16="Eleanor", ln16="Chapel",
                   fn17="Johann", mn17="Alejandro", ln17="Maldonado",
                   fn18="Bilal", ln18="Rashid", ln19="Oh", fn19="Sumin",
                   fn20="Hack", mn20="The", ln20="North", ln21="Last", mn21="Middle", fn21="First"), "\n")
