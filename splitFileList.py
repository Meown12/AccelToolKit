import os
import argparse


def getString(List):
    outString = ""
    for element in List:
        outString = outString + str(element) + "\n"
    return outString


def main():
    parser = argparse.ArgumentParser(description="File Accumulator")
    parser.add_argument("indir", metavar="ID",
                        help="A directory containing the list of files to be read")
    parser.add_argument("outputFile", default=".", metavar="OD", help="output file template for the results")
    parser.add_argument("fileLength", metavar="n", type=int, default= 1000, help="number of elements per output file")
    args = parser.parse_args()
    inputDir = os.path.abspath(args.indir)
    outFile = os.path.abspath(args.outputFile)
    outFileName, outFileExt = os.path.splitext(outFile)
    outList = []
    i = 0
    j = 0
    for file in os.listdir(inputDir):
        fileName = os.path.join(inputDir, file)
        if (os.path.isfile(fileName) & ((os.path.splitext(fileName)[1] == ".csv") |(os.path.splitext(fileName)[1] == ".gz"))):
            outList.append(fileName)
        if len(outList) >= args.fileLength:
            i = 0
            with open("{}_{}{}".format(outFileName, j, outFileExt), "w") as file:
                file.write(getString(outList))
            del outList[:]
            j = j + 1
        i = i+1
    if len(outList) != 0:
        with open("{}_{}{}".format(outFileName, j, outFileExt), "w") as file:
            file.write(getString(outList))


if __name__ == "__main__":
    main()