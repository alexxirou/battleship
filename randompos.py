import math
import os
import random

dirname = os.path.dirname(__file__)
filename1 = os.path.join( dirname, 'grid1.grd')
filename2 = os.path.join( dirname, 'grid2.grd')




def random_shippos(lengthoflist,n):
    randomlist1 = []
    randomlist2 = []
    reversevar = random.randrange(0, n)
    """Generate a random var to decide if ship will be vertically or horizontally placed."""

    while len(randomlist1) <= lengthoflist:
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

        randomlist2.append(res)

    return randomlist2


def create_grids(file):
    list1 = random_shippos(5,2)
    list2 = random_shippos(4,2)
    list3 = random_shippos(3,2)
    list4 = random_shippos(3,2)
    list5 = random_shippos(3,2)

    for t1 in list1:
        for t2 in list2:
            while t1 in list2:
                #print("list1",list1)
                #print("lis2",list2)
                list2 = random_shippos(4,2)

    for t1 in list1:
        for t2 in list2:
            for t3 in list3:
                while t1 in list3 or t2 in list3:
                    #print("list3",list3)
                    list3 = random_shippos(3,2)         
    
    for t1 in list1:
        for t2 in list2:
            for t3 in list3:
                for t4 in list4:
                    while t1 in list4 or t2 in list4 or t3 in list4:
                        #print("list4",list4)
                        list4 = random_shippos(3,2)   

    for t1 in list1:
        for t2 in list2:
            for t3 in list3:
                for t4 in list4:
                    for t5 in list5:
                        while t1 in list5 or t2 in list5 or t3 in list5 or t4 in list5:
                            #print("list5", list5)
                            list5 = random_shippos(3,2)   


    Lines= ["10:10 \n"
    "Carrier " +str(list1[0][0])+":"+str(list1[0][1])+" "+str(list1[1][0])+":"+str(list1[1][1])+" "+str(list1[2][0])+":"+str(list1[2][1])+" "+str(list1[3][0])+":"+str(list1[3][1])+" "+str(list1[4][0])+":"+str(list1[4][1]),"\n"
    "Battleship " +str(list2[0][0])+":"+str(list2[0][1])+" "+str(list2[1][0])+":"+str(list2[1][1])+" "+str(list2[2][0])+":"+str(list2[2][1])+" "+str(list2[3][0])+":"+str(list2[3][1]),"\n"
    "Cruiser " +str(list3[0][0])+":"+str(list3[0][1])+" "+ str(list3[1][0])+":"+str(list3[1][1])+" "+str(list3[2][0])+":"+str(list3[2][1]),"\n"
    "Submarine " +str(list4[0][0])+":"+str(list4[0][1])+" "+ str(list4[1][0])+":"+str(list4[1][1])+" "+str(list4[2][0])+":"+str(list4[2][1]),"\n"
    "Destroyer " +str(list5[0][0])+":"+str(list5[0][1])+" "+ str(list5[1][0])+":"+str(list5[1][1]), "\n"]
    """Writing coords for each ship in file"""
    with open(file, 'w') as f:
        f.writelines(Lines)

    #with open(file,'r') as f: #debug
     #   print(f.read())




create_grids(filename1)
create_grids(filename2)
