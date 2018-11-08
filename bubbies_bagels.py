# Natalie Prahst
# Module #3 Individual Assignment

# Bagel-ordering GUI in which a customer can put together
# an order comprised of bagels and toppings, and a price
# and wait-time for their order is calculated.

from graphics import *

def main():
    # draw interface
    window = GraphWin("Bubbie's Bagels", 300, 500)
    window.setCoords(0.0, 0.0, 3.0, 5.0)
    window.setBackground("turquoise")

    titleBanner = Rectangle(Point(0, 4.7), Point(3, 5))
    titleBanner.setFill("PaleTurquoise")
    titleBanner.draw(window)
    
    title = Text(Point(1.5, 4.85), "BUBBIE'S BAGELS")
    title.setStyle("bold")
    title.draw(window)

    # startup screen
    startupMsg = Text(Point(1.5, 1.5), "Click anywhere to begin your order!")
    startupMsg.setSize(10)
    startupMsg.setStyle("bold")
    startupMsg.draw(window)

    bagelOuter = Circle(Point(1.5, 2.7), 0.8)
    bagelOuter.setFill("sandybrown")
    bagelOuter.draw(window)

    bagelInner = Circle(Point(1.5, 2.7), 0.3)
    bagelInner.setFill("turquoise")
    bagelInner.draw(window)

    window.getMouse()
    startupMsg.undraw()
    bagelOuter.undraw()
    bagelInner.undraw()

    # display "order in progress" banner
    orderBanner = Rectangle(Point(0, 4.5), Point(3, 4.7))
    orderBanner.setFill("PaleTurquoise1")
    orderBanner.draw(window)
    
    orderTitle = Text(Point(1.5, 4.6), "Order in progress")
    orderTitle.setStyle("bold")
    orderTitle.setSize(9)
    orderTitle.draw(window)

    # ORDER STEP 1: bagel selection
    selectMsg = Text(Point(1.5, 4), "Step 1: Select your bagels")
    selectMsg.setStyle("bold")
    selectMsg.draw(window)

    promptPlain = Text(Point(1.25, 3.5), "Plain ($1.75 ea): ")
    promptPlain.draw(window)
    
    promptWhole = Text(Point(1, 3), "Whole grain ($1.75 ea): ")
    promptWhole.draw(window)
    
    promptEverything = Text(Point(1.1, 2.5), "Everything ($1.85 ea): ")
    promptEverything.draw(window)

    entryPlain = Entry(Point(2.2, 3.5), 3)
    entryPlain.setFill("PaleTurquoise")
    entryPlain.setStyle("bold")
    entryPlain.draw(window)

    entryWhole = Entry(Point(2.2, 3), 3)
    entryWhole.setFill("PaleTurquoise")
    entryWhole.setStyle("bold")
    entryWhole.draw(window)

    entryEverything = Entry(Point(2.2, 2.5), 3)
    entryEverything.setFill("PaleTurquoise")
    entryEverything.setStyle("bold")
    entryEverything.draw(window)

    # next page button
    nextButton = Rectangle(Point(1, 0.3), Point(2, 0.7))
    nextButton.setFill("PaleTurquoise1")
    nextButton.draw(window)
    
    nextMsg = Text(Point(1.5, 0.5), "Next >>>")
    nextMsg.setStyle("bold")
    nextMsg.draw(window)

    # wait for click before moving to step 2 of order
    click = window.getMouse()
    getNextClick(click, window)

    # undraw step 1 objects
    promptPlain.undraw()
    promptWhole.undraw()
    promptEverything.undraw()
    entryPlain.undraw()
    entryWhole.undraw()
    entryEverything.undraw()

    # ORDER STEP 2: toppings selection
    # free options are butter, cream cheese, onions, lettuce, and tomatoes
    selectMsg.setText("Step 2: Select your toppings")
    


    
    
    # ORDER STEP 3: ORDER SUMMARY


    window.getMouse()
    window.close()

def getNextClick(click, window):
    # waits until user clicks within the space of the next button
    while (click.getX() < 1 or click.getX() > 2
           or click.getY() < 0.3 or click.getY() > 0.7):
        click = window.getMouse()

main()
