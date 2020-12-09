#### This module is used to: ###
1. Extract students Python source code from IGINIOUS exams
2. Convert Python source code to XML files by using pyRegurgitator

#### USAGE ####
1. pyRegurgitator only works with Python 3.4.
2. To extract Python source code from INGINIOUS exams and convert these files to XML using the follow commandline:

`python extractPythonCode.py INPUT_DIR OUTPUT_DIR`

INPUT_DIR: directory containning data downloaded from INGINIOUS
OUTPUT_DIA: directory containning output XML files

Note: we can edit the extractPythonCode.py script to indicate the score of each group.
Currently, high score group includes submission having scores > 50; low score group having score > 0 and <= 50
