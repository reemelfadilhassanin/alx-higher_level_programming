#!/usr/bin/python3
def multiple_returns(sentence):
    length_t = len(sentence)
    if length_t == 0:
        first_char = None
        
    else:
        first_char = sentence[0]
        _tuple = (length_t, first_char)
        return _tuple
