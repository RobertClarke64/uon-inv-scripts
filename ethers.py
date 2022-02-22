import os, sys


class EthersFile :

    def __init__(self, path : str) :
        self.filePath = path
        self.fileContents = None
        self.parse_file()

    def parse_file(self):
        f = open(self.filePath)
        self.fileContents = f.read().splitlines()
        f.close()

        for line in self.fileContents:
            content = line.split("#")[0]
            print(content)


def main():
    files = os.listdir("input/oldethers")
    e = EthersFile(f"input/oldethers/{files[0]}")

if __name__ == "__main__":
    main()
