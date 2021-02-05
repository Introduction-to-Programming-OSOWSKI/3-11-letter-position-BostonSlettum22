def letterPos(w,n):
    letter = w[len(w)-1]

    for i in range(0,len(w)+1):
        letter = letter + w[len(w)-1]
    if w == [len(n)-1]:
        return len(w)
    else:
        return w[0]


print(letterPos("dunder","d"))
