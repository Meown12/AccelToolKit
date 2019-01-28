import os
import argparse
def main():
    parser = argparse.ArgumentParser(description="File Accumulator")
    parser.add_argument("indir", metavar="ID",
                        help="A directory containing the list of files to be read")
    parser.add_argument("outputFile", default=".", metavar="OD", help="output file for the results")

    args = parser.parse_args()
    inputDir = os.path.abspath(args.indir)
    outFileName = os.path.abspath(args.outputFile)

    outString = ""
    for file in os.listdir(inputDir):
        fileName = os.path.join(inputDir, file)
        if (os.path.isfile(fileName) & ((os.path.splitext(fileName)[1] == ".csv") |(os.path.splitext(fileName)[1] == ".gz"))):
            outString = outString + fileName + "\n"

    with open(outFileName, "w") as file:
        file.write(outString)


if __name__ == "__main__":
    main()