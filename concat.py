import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="File Concatenator")
parser.add_argument("indir", metavar="ID", help="input directory")
parser.add_argument("file", metavar="F", help="A unique part of the file name of the files to be concatenated ")
parser.add_argument("-hd", nargs='?', const=1, type=int, help="number of headerlines per file")
parser.add_argument("outputFile", default=".", metavar="OD", help="output file path")
args = parser.parse_args()

headerTaken = False

for file in os.listdir(os.path.abspath(args.indir)):
    file = os.path.join(os.path.abspath(args.indir), file)
    if os.path.isfile(file) and args.file in file:
        with open(file) as inFile:
            if not headerTaken:
                with open(args.outputFile, "w+") as outFile:
                    shutil.copyfileobj(inFile, outFile)
                headerTaken = True
            else:
                with open(args.outputFile, "a+") as outFile:
                    for i in range(0,args.hd):
                        inFile.readline()
                    shutil.copyfileobj(inFile, outFile)

