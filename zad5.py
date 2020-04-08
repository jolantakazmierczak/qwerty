
def proste(y1 ,x1 ,b1, y2 ,x2 ,b2):
    a1= (y1-b1)/x1
    a2= (y2-b2)/x2
    if (a1 == a2):
        print("rownolegle")
    elif (a1 * a2 == -1):
        print("prostopadle")
    else:
         print("zadna opcja")

proste(4,2,2,10,9,1)





