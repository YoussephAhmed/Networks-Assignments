from alter import alter
from generator_function import generator
from verifier import verifier
import sys

def read_lines(filename):
    in_file = open(filename, "r")
    lines = in_file.readlines()
    message = lines[0]
    key = lines[1]
    in_file.close()
    return message, key


def main():

    args = len(sys.argv)
    file_name = sys.argv[1]
    message, key = read_lines(file_name)
    remainder,trans_message = generator(message, key)
    out_file = open('generator_Output.txt',"w")
    out_file.write(trans_message)
    out_file.write('\n')
    out_file.write(key)
    out_file.close()
    message_new, key  = read_lines('generator_output.txt')

    if(args > 4):
        message_new = alter(message_new, int (sys.argv[3]))

    out_file = open('message_output.txt', "w")
    out_file.write(verifier(message_new, key))
    out_file.close()


if __name__ == "__main__":
    main()
