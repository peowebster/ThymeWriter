import random

def makeplan (wordcount, daycount, plantype):
    chunk = wordcount // daycount
    days = []
    spare = wordcount % daycount

    for i in range(daycount):
        days.append(chunk)

    if(plantype == "random"):
        for i in range(daycount):
            modify = random.randint(-(chunk-1), chunk - 1)
            days[i] -= modify
            spare += modify
    elif(plantype == "ascending"):
        increment = (chunk - (chunk // 10)) // daycount
        for i in range(daycount):
            days[i] += increment * i
            spare -= increment * i
    elif(plantype == "descending"):
        increment = (chunk - (chunk // 10)) // daycount
        for i in range(daycount):
            days[i] -= increment * i
            spare += increment * i
    elif(plantype != "steady"):
        print("plan type not recgonised")
        return -1


    while spare != 0:
        for i in range(daycount):
            if spare > 0:
                days[i] += 1
                spare -= 1
            elif spare < 0:
                days[i] -= 1
                spare += 1
    
    print(days)
    return days

makeplan(10000, 10, "random")
makeplan(10000, 10, "ascending")
makeplan(10000, 10, "descending")
makeplan(10000, 10, "steady")
makeplan(10000, 10, "folga wooga imoga womp")