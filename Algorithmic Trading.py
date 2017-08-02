#Algorithmic Trading with Machine Learning

from tkinter import *
from random import *
from math import *
from time import *
from sklearn import tree
import time
start_time = time.time()
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
##    
##root = Tk()
##s = Canvas(root, width = 1500, height = 1000, background = "black")
##s.pack()


def algo(t):
    
    if len(t) < acc:
        return 0
    
    else:
        features = []
        labels = []

        for i in range(len(t) - acc + 1):
            features.append(t[-1*acc:-1])

            #1 means price went up
            if t[-1] > t[-2]:
                labels.append(1)
            else:
                labels.append(0)
                
        clf = tree.DecisionTreeClassifier()
        clf.fit(features, labels)

        if clf.predict(t[-1*acc+1:])[0] == 1:
            return 1
        else:
            return 0
    
run = 0
avg = 0
pavg = 0
counterR = 0
counterT = 0
acc = 10

for i in range(0,1000):
    Points = []
    CashRecords = []
    SMAPts = []
    SMAPts2 = []
    initP = 0
    initC = 0

    Cash = 100
    Bought = False
    days = 0
    StockPrice = 300
    Points.append(StockPrice)
    CashRecords.append(Cash)
    decision = 0
    
    while days <= 750:
    #stock info

        risk = randint(0,0.1*Points[0])
        change = choice([-1,1])*risk
        
        days += 1
        
        if StockPrice + change < 50:
            break

        StockPrice = round((StockPrice + change),2)

        if days == 1:
            initP = StockPrice
            initC = Cash
            
        #your money
        if Bought == True:
            Cash = round(Cash*StockPrice/Points[days-1],2)
            color = "green"
        else:
            color = "red"

        if days > acc + 1:
            counterT += 1
            if StockPrice >= Points[-2] and  Bought == True or StockPrice < Points[-2] and  Bought == False:
                counterR += 1
##        a = s.create_text(200,100,text = str(Cash),fill = "white",font = "Arial 50")

        Points.append(StockPrice)
        x = days*2+1
        y = 1000-StockPrice
##        s.create_line((days-1)*2+1,1000-Points[days-1],x,y,fill=color)
                      
        CashRecords.append(Cash)
        
        y = 1000-Cash
##        s.create_line((days-1)*2+1,1000-CashRecords[days-1],x,y,fill="blue")

##        s.update()
##        s.delete(a)
        
        if days > acc:
            decision = algo(Points)

        
        if Bought == True:
            if decision == 0:
                Bought = False
        else:
            if decision == 1:
                Bought = True


    avg = (avg * run + Cash) / (run + 1)
    pavg = (pavg * run + (Cash * initP / (StockPrice * initC))) / (run + 1)
##    a = s.create_text(200,100,text = str(Cash),fill = "white",font = "Arial 50")
    run += 1
##    print("Ending Cash " + str(Cash))
##    print("Expected Cash: " + str(round(initC * StockPrice / initP,2)))
##    print("Performance: " + str(round(100 * Cash * initP / (StockPrice * initC),2)) + "%")
##    print("")
    
print("Number of Correct Predictions: " + str(counterR) + " / " + str(counterT))
print("Accuracy: " + str(round(100*counterR/counterT,2)) + "%")
print("Average Yield: " + str(round(avg,2)))
print("Average Performance: " + str(round(100 * pavg,2)) + "%")
print("")
print("--- %s seconds ---" % (round(time.time() - start_time,2)))
