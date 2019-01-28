import shutil
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="File Accumulator")
    parser.add_argument("indir", metavar="ID",
                        help="A directory containing the list of files to be read")
    parser.add_argument("outputDirs", default=".", metavar="OD", help="dir template for the results")
    parser.add_argument("dirSize", metavar="n", type=int, default=1000, help="number of elements per output file")
    args = parser.parse_args()
    inputDir = os.path.abspath(args.indir)
    outDirTemp = os.path.abspath(args.outputDirs)
    length = (args.dirSize)

    count = 0
    fileCount = 0
    for file in os.listdir(inputDir):

        fileName = os.path.join(inputDir, file)
        if (os.path.isfile(fileName)) & (os.path.splitext(fileName)[1] == ".tsv"):
            fileCount += 1
            dir = "{}_{}".format(os.path.abspath(outDirTemp), count)
            try:
                os.mkdir(dir)
            except OSError:
                pass
            if fileName in os.listdir(dir):
                print("file skipped " + fileName)
                continue

            print(fileName + " -> "+dir)
            shutil.copy(fileName, dir)
            if fileCount >= length:
                count += 1
                fileCount = 0


if __name__ == "__main__":
    main()