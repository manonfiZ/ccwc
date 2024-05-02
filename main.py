from core.cc_word_counter import CcWC
from core.cc_args_parser import CcWCParser

def main ( ) :
    parser = CcWCParser()
    args = parser.args

    ccwc = CcWC(args.file)
    output = "\t{} "

    output += str(args.file)   if ".txt"  in  str(args.file) else " "

    try :
        if args.bytes:
            output= output.format(ccwc.count_bytes())
        elif args.words:
            output=output.format(ccwc.count_words())
        elif args.lines:
            output=  output.format(ccwc.count_lines())
        elif args.chars:
            output=  output.format(ccwc.count_chars())
        else:
            output =  output.format(str(ccwc.count_bytes()) + " " + str(ccwc.count_lines() )+ " " + str(ccwc.count_words()))

        print(output)

    except FileNotFoundError:
        print ("No such file or directory : {}".format(args.file))

if __name__ == '__main__' :
    main()
