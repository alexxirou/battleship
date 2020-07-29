import math
import os
import random

dirname = os.path.dirname(__file__)
filename1 = os.path.join( dirname, 'grids/grid1.grd')
filename2 = os.path.join( dirname, 'grids/grid2.grd')




def random_shippos_carrier():
    randomlist1 = []
    randomlist2 = []
    reversevar = random.randrange(0, 2)
    """Generate a random var to decide if ship will be vertically or horizontally placed."""

    while len(randomlist1) <= 5:
        """This loop will repeat if the length of the generated random list is too long or too short."""
        randomlist1 = []
        """Emptying list between loops"""
        random1 = random.choice([i for i in  range(11, 99) if i not in [20,30,40,50,60,70,80,90]])
        rounded1 = int(math.ceil(random1 / 10.0)) * 10
        """calculating rounded 10 or the random int."""
        if random1 > rounded1:
            """Generating a range between the random number and the its rounded value."""
            for x in range(rounded1+1, random1, 1):
                randomlist1.append(str(x))
        elif random1 < rounded1:
            for x in range(random1, rounded1-1, 1):
                randomlist1.append(str(x))
    for char in randomlist1:
        """Breaking the list interger into single digits chars to be used for x and y coords."""

        res = list(map(int, char))
        if reversevar == 0:
            res.reverse()
        res = tuple(res)
        randomlist2.append(res)

    return randomlist2

def random_shippos_battleship():
    randomlist1 = []
    randomlist2 = []
    reversevar = random.randrange(0, 2)
    while len(randomlist1) <= 5:
        randomlist1 = []
        random1 = random.choice([i for i in range(11, 99) if i not in [20,30,40,50,60,70,80,90]])
        rounded1 = int(math.ceil(random1 / 10.0)) * 10
        if random1 > rounded1:
            for x in range(rounded1+1, random1, 1):
                randomlist1.append(str(x))
        elif random1 < rounded1:
            for x in range(random1, rounded1-1, 1):
                randomlist1.append(str(x))
    for char in randomlist1:
        """Breaking the list interger into single digits chars to be used for x and y coords."""

        res = list(map(int, char))
        if reversevar == 0:
            res.reverse()
        res = tuple(res)
        randomlist2.append(res)
    return randomlist2


def random_shippos_cruiser_or_sub():
    randomlist1 = []
    randomlist2 = []
    reversevar = random.randrange(0, 2)


    while len(randomlist1) <= 4:
        randomlist1 = []
        random1 = random.choice([i for i in range(11, 99) if i not in [20, 30, 40, 50, 60, 70, 80, 90]])
        rounded1 = int(math.ceil(random1 / 10.0)) * 10

        if random1 > rounded1:
            for x in range(rounded1 + 1, random1, 1):
                randomlist1.append(str(x))
        elif random1 < rounded1:
            for x in range(random1, rounded1 - 1, 1):
                randomlist1.append(str(x))
    for char in randomlist1:
        """Breaking the list interger into single digits chars to be used for x and y coords."""

        res = list(map(int, char))
        if reversevar == 0:
            res.reverse()
        res = tuple(res)
        randomlist2.append(res)

    return randomlist2



def random_shippos_destroyer():
    randomlist1 = []
    randomlist2 = []

    reversevar = random.randrange(0, 2)

    while len(randomlist1) <= 3:
        randomlist1 = []
        random1 = random.choice([i for i in range(11, 99) if i not in [20, 30, 40, 50, 60, 70, 80, 90]])
        rounded1 = int(math.ceil(random1 / 10.0)) * 10

        if random1 > rounded1:
            for x in range(rounded1 + 1, random1, 1):
                randomlist1.append(str(x))
        elif random1 < rounded1:
            for x in range(random1, rounded1 - 1, 1):
                randomlist1.append(str(x))

    for char in randomlist1:
        """Breaking the list interger into single digits to be used for x and y coords."""

        res = list(map(int, char))
        if reversevar == 0:
            res.reverse()
        res = tuple(res)
        randomlist2.append(res)

    return randomlist2

def create_grids(file):
    list1 = random_shippos_carrier()
    list2 = random_shippos_battleship()
    list3 = random_shippos_cruiser_or_sub()
    list4 = random_shippos_cruiser_or_sub()
    list5 = random_shippos_destroyer()

    for t1 in list1:
        for t2 in list2:
            for t3 in list3:
                for t4 in list4:
                    while t1 in list2 or t1 in list3 or t1 in list4 or t1 in list5 or t2 in list3 or t2 in list4 or t2 in list5 or t3 in list4 or t3 in list5 or t4 in list5:
                        list1 = random_shippos_carrier()
                        list2 = random_shippos_battleship()
                        list3 = random_shippos_cruiser_or_sub()
                        list4 = random_shippos_cruiser_or_sub()
                        list5 = random_shippos_destroyer()
                        """Nested loop to check that the lists used for coord do not intersect."""

    Lines= ["10:10 \n"
    "Carrier " +str(list1[0][0])+":"+str(list1[0][1])+" "+str(list1[1][0])+":"+str(list1[1][1])+" "+str(list1[2][0])+":"+str(list1[2][1])+" "+str(list1[3][0])+":"+str(list1[3][1])+" "+str(list1[4][0])+":"+str(list1[4][1]),"\n"
    "Battleship " +str(list2[0][0])+":"+str(list2[0][1])+" "+str(list2[1][0])+":"+str(list2[1][1])+" "+str(list2[2][0])+":"+str(list2[2][1])+" "+str(list2[3][0])+":"+str(list2[3][1]),"\n"
    "Cruiser " +str(list3[0][0])+":"+str(list3[0][1])+" "+ str(list3[1][0])+":"+str(list3[1][1])+" "+str(list3[2][0])+":"+str(list3[2][1]),"\n"
    "Submarine " +str(list4[0][0])+":"+str(list4[0][1])+" "+ str(list4[1][0])+":"+str(list4[1][1])+" "+str(list4[2][0])+":"+str(list4[2][1]),"\n"
    "Destroyer " +str(list5[0][0])+":"+str(list5[0][1])+" "+ str(list5[1][0])+":"+str(list5[1][1]), "\n"]
    """Writing coords for each ship in file"""
    with open(file, 'w') as f:
        f.writelines(Lines)

    #with open(file,'r') as f:
        #print(f.read())




create_grids(filename1)
create_grids(filename2)
