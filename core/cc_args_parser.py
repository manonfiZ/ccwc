import argparse

class CcWCParser:

    def __init__(self) -> None:

        parser = argparse.ArgumentParser()
        parser.add_argument('file' , help='File')
        parser.add_argument('-c', "--bytes", help='Its count number of bytes in the file', action='store_true')
        parser.add_argument('-l', "--lines", help='Outputs the number of lines in a file', action='store_true')
        parser.add_argument('-w', "--words", help='Outputs the number of word in a file', action='store_true')
        parser.add_argument('-m', "--chars", help='Outputs the number of characters in a file', action='store_true')

        self.args = parser.parse_args()    