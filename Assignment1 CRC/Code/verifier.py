from generator_function import generator

def verifier (rec_message,key):
    remainder, trans_message = generator(rec_message,key)

    if remainder == '0':
        return "message is correct"
    else:
        return "message is not correct"

