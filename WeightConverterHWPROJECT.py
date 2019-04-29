'''
author: Hector Montijo
module: WeightConverterHWPROJECT.py
date: 04/23/19
description: This program converts lb in grams,kilograms and ounces
'''


from graphics import *
def main():
    ''' This creates the size of the window and the name'''
    win = GraphWin(" Weight Converter ", 500 ,500)
    win.setBackground("grey")
    
    ''' This creates the title for the Weight Converter'''
    wc= Text(Point(240 , 60),"Weight Converter")
    wc.setSize(26)
    wc.setStyle("bold")
    wc.setFill("black")
    wc.draw(win)
    '''This is the entry the user will enter in pounds to convert'''
    entry1 = Entry(Point (240, 100),30)
    entry1.setFill("white")
    entry1.draw(win)

    wclb = Text(Point(390 ,100) , "lb")
    wclb.setSize(11)
    wclb.setStyle("bold")
    wclb.setFill("black")
    wclb.draw(win)
    
    g = Text(Point(130,170),"Grams")
    g.setSize(10)
    g.setFill("black")
    g.draw(win)
    ''' The pounds (lb) enter in the first entry is converted to grams'''
    entry2 = Entry(Point(240, 195),30)
    entry2.setFill("white")
    entry2.setText('0.0')
    entry2.draw(win)

    kg= Text(Point(140,240),"Kilograms")
    kg.setSize(10)
    kg.setFill("black")
    kg.draw(win)
    ''' The pounds (lb) enter in the first entry is converted into kilograms'''
    entry3 = Entry(Point(240,265), 30)
    entry3.setFill("white")
    entry3.setText('0.0')
    entry3.draw(win)

    o= Text(Point(130,310),"Ounces")
    o.setSize(10)
    o.setFill("black")
    o.draw(win)
    ''' The pounds (lb) enter in the first entry is converted into ounces'''
    entry4 = Entry(Point(240,335), 30)
    entry4.setFill("white")
    entry4.setText('0.0')
    entry4.draw(win)

    
    '''This creates the orange CONVERT button under the Weight Converter window'''
    button1=Rectangle(Point(270,370),Point(375, 410))
    button1.setFill("orange")
    button1.setOutline("black")
    button1.draw(win)

    button = Text(Point(322,390),"Convert")
    button.setSize(12)
    button.setStyle("bold")
    button.setFill("white")
    button.draw(win)
    win.getMouse()
    '''
    After creating the graphics , we create another function , which will convert the pounds
    into grams , kilograms, ounces
    '''
    def weightConvert():
        '''
        Input : enter pounds(lb) to convert into grams,kilograms, ounces
        Process: Converts the lb into grams, kilograms , ounces
        Output: The Grams, kilograms and ounces are converted
        '''
        while True:
            lb = float(entry1.getText())
            
            if lb >= 0:
                gram = lb * 453.59237
                entry2.setText(round(gram,2))
                win.getMouse()
                kilograms = lb * .45359237
                entry3.setText(round(kilograms,2))
                win.getMouse()
                
                ounces = lb * 16
                entry4.setText(round(ounces,2))
                win.getMouse()
                
                

                print("Gram:",(round(gram,2)))
                print("Kilograms:",(round(kilograms,2)))
                print("Ounces:",(round(ounces,2)))
            
        
       
            else:
                entry1.setText("INVAILD INPUT,PLEASE enter a NUMBER under the entry.")
                print("INVAILD INPUT,PLEASE enter a NUMBER under the entry.")
                
                
        
                
                
    weightConvert()
    
main()
       







