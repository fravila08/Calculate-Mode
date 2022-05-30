from operator import countOf


def calculate_mode(x):
    answer=[]
    compare=0
    myObj=[]
    #print(countOf(x, 4.5))
    for i in x:
        count=countOf(x, i)
        myObj.append([i, count])
    #print(myObj)
    for i in myObj:
        if(compare<=i[1]):
            compare= i[1]
        else:
            continue
    #print(compare)
    for j in myObj:
        if(j[1]== compare):
            answer.append(j[0])
        else:
            continue
    for k in answer:
        if countOf(answer, k)>1:
            answer.remove(k)
    return answer
#print(calculate_mode(["who", "what", "where", "who"]))