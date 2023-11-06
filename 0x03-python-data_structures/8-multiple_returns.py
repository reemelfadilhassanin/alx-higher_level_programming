#!/usr/bin/python3
def multiple_returns(sentence):
    length_t = len(sentence)
    if length_t == 0:
        first_char = None
        tup = (length_t, first_char)
        return tup
    else:
        first_char = sentence[0]
        tup = (length_t, first_char)
        return tup
