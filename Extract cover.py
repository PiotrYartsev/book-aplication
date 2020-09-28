# -*- coding: utf-8 -*-

import shutil
import os


import PyPDF2


def bookmark_dict(bookmark_list):
    result = {}
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call
            result.update(bookmark_dict(item))
        else:
            result[reader.getDestinationPageNumber(item)] = item.title

    return result


reader = PyPDF2.PdfFileReader("/home/piotr/Desktop/Books/Programming/Python 2019 Pack/Data Structures and Algorithms with Python/PDF/handsondatastructuresandalgorithmswithpython.pdf")

print(bookmark_dict(reader.getOutlines())[0])