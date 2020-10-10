import shutil
import os
import os
from string import digits
import subprocess
import PyPDF2 
import textract
import warnings
from tqdm import tqdm
from Orgenise import *
from settings import *
from Image_pre_processing import *
import TAGS
import settings
from INFO import *
from __main__ import *
import time



init2()

Orgenise()

Image_pre_processing()

Make_tags()

INFO()