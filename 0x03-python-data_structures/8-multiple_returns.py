def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        first_char = None
    else:
        first_char = sentence[0]
        tup = (leng, first_char)
    return tup
