#!/usr/bin/env python

import sys, os

# path = sys.stdin.read()
# path = path.strip()
# files = os.listdir(path)
#
# subSequence = "GTGC"
# for file in files:
#     file = path + "/" + file
#     file = open(file)
#     for line in file.read().split("\n"):
#         match_string = ""
#         k = 0
#         for char in line:
#             if char == subSequence[k]:
#                 match_string = match_string + char
#                 k = k + 1
#                 if match_string == subSequence:
#                     print('%s\t%s' % (subSequence, 1))
#                     match_string = ""
#                     k = 0
#             else:
#                 k = 0
#                 match_string = ""
#                 if char == subSequence[k]:
#                     match_string = match_string + char
#                     k = k + 1
#                     if match_string == subSequence:
#                         print('%s\t%s' % (subSequence, 1))
#                         match_string = ""
#                         k = 0

subSequence = sys.argv[1]
inputFile = os.environ['mapreduce_map_input_file']


for file in sys.stdin:
    file = file.strip()
    for line in file.split("\n"):
        match_string = ""
        k = 0
        for char in line:
            if char == subSequence[k]:
                match_string = match_string + char
                k = k + 1
                if match_string == subSequence:
                    print('%s\t%s\t%s' % (inputFile, subSequence, 1))
                    match_string = ""
                    k = 0
            else:
                k = 0
                match_string = ""
                if char == subSequence[k]:
                    match_string = match_string + char
                    k = k + 1
                    if match_string == subSequence:
                        print('%s\t%s' % (subSequence, 1))
                        match_string = ""
                        k = 0
