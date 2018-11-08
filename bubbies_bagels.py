# Natalie Prahst
# Module #3 Individual Assignment

# Bagel-ordering GUI in which a customer can put together
# an order comprised of bagels and toppings, and a price
# and wait-time for their order is calculated.

from graphics import *

def main():
    
    # draw interface base
    window = GraphWin("Bubbie's Bagels", 300, 500)
    window.setCoords(0.0, 0.0, 3.0, 5.0)
    window.setBackground("turquoise")

    titleBanner = Rectangle(Point(0, 4.7), Point(3, 5))
    titleBanner.setFill("PaleTurquoise")
    titleBanner.setOutline("PaleTurquoise")
    titleBanner.draw(window)
    
    title = Text(Point(1.5, 4.85), "BUBBIE'S BAGELS")
    title.setStyle("bold")
    title.draw(window)

    # STARTUP SCREEN
    welcomeMsg = Text(Point(1.5, 3.8), "WELCOME")
    welcomeMsg.setStyle("bold")
    welcomeMsg.setSize(18)
    welcomeMsg.draw(window)
    
    startupMsg = Text(Point(1.5, 1.5), "Click anywhere\nto begin your order!")
    startupMsg.setSize(13)
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
    welcomeMsg.undraw()

    # display "order in progress" banner
    orderBanner = Rectangle(Point(0, 4.5), Point(3, 4.7))
    orderBanner.setFill("PaleTurquoise1")
    orderBanner.setOutline("PaleTurquoise1")
    orderBanner.draw(window)
    
    orderTitle = Text(Point(1.5, 4.6), "Order in progress")
    orderTitle.setStyle("bold")
    orderTitle.setSize(9)
    orderTitle.draw(window)


    # ORDER STEP 1: bagel selection
    stepMsg = Text(Point(1.5, 4), "Step 1: Select your bagels")
    stepMsg.setStyle("bold")
    stepMsg.draw(window)

    promptPlain = Text(Point(1.25, 3.5), "Plain ($1.75 ea): ")
    promptPlain.draw(window)
    
    promptWhole = Text(Point(1, 3), "Whole grain ($1.75 ea): ")
    promptWhole.draw(window)
    
    promptEverything = Text(Point(1.1, 2.5), "Everything ($1.85 ea): ")
    promptEverything.draw(window)

    entryPlain = Entry(Point(2.2, 3.5), 3)
    entryPlain.setFill("PaleTurquoise")
    entryPlain.setStyle("bold")
    entryPlain.setText("0")
    entryPlain.draw(window)

    entryWhole = Entry(Point(2.2, 3), 3)
    entryWhole.setFill("PaleTurquoise")
    entryWhole.setStyle("bold")
    entryWhole.setText("0")
    entryWhole.draw(window)

    entryEverything = Entry(Point(2.2, 2.5), 3)
    entryEverything.setFill("PaleTurquoise")
    entryEverything.setStyle("bold")
    entryEverything.setText("0")
    entryEverything.draw(window)

    # next page button
    nextButton = Rectangle(Point(0.8, 0.3), Point(2.2, 0.7))
    nextButton.setFill("PaleTurquoise1")
    nextButton.setOutline("PaleTurquoise1")
    nextButton.draw(window)
    
    nextMsg = Text(Point(1.5, 0.5), "Next >>>")
    nextMsg.setStyle("bold")
    nextMsg.draw(window)

    # wait for click before moving to step 2 of order
    click = window.getMouse()
    getNextClick(click, window)

    # extract bagel info from entries
    numOfPlain = int(eval(entryPlain.getText()))
    numOfEverything = int(eval(entryEverything.getText()))
    numOfWhole = int(eval(entryWhole.getText()))
    totalNumOfBagels = numOfPlain + numOfEverything + numOfWhole
    
    # undraw step 1 objects
    promptPlain.undraw()
    promptWhole.undraw()
    promptEverything.undraw()
    entryPlain.undraw()
    entryWhole.undraw()
    entryEverything.undraw()


    # ORDER STEP 2: toppings selection
    # free options are butter, cream cheese, onions, lettuce, and tomatoes
    stepMsg.setText("Step 2: Select your FREE toppings")

    # display prompts
    promptCreamCheese = Text(Point(1, 3.6), "Cream cheese: ")
    promptCreamCheese.draw(window)

    promptOnions = Text(Point(1.25, 3.2), "Onions: ")
    promptOnions.draw(window)

    promptLettuce = Text(Point(1.25, 2.8), "Lettuce: ")
    promptLettuce.draw(window)

    promptTomato = Text(Point(1.25, 2.4), "Tomato: ")
    promptTomato.draw(window)

    promptButter = Text(Point(1.26, 2.0), "Butter: ")
    promptButter.draw(window)

    # display entry spots for each topping
    entryCreamCheese = Entry(Point(2, 3.6), 3)
    entryCreamCheese.setFill("PaleTurquoise")
    entryCreamCheese.setStyle("bold")
    entryCreamCheese.setText("0")
    entryCreamCheese.draw(window)

    entryOnions = Entry(Point(2, 3.2), 3)
    entryOnions.setFill("PaleTurquoise")
    entryOnions.setStyle("bold")
    entryOnions.setText("0")
    entryOnions.draw(window)

    entryLettuce = Entry(Point(2, 2.8), 3)
    entryLettuce.setFill("PaleTurquoise")
    entryLettuce.setStyle("bold")
    entryLettuce.setText("0")
    entryLettuce.draw(window)

    entryTomato = Entry(Point(2, 2.4), 3)
    entryTomato.setFill("PaleTurquoise")
    entryTomato.setStyle("bold")
    entryTomato.setText("0")
    entryTomato.draw(window)

    entryButter = Entry(Point(2, 2.0), 3)
    entryButter.setFill("PaleTurquoise")
    entryButter.setStyle("bold")
    entryButter.setText("0")
    entryButter.draw(window)

    # wait for click before moving to step 3 of order
    click = window.getMouse()
    getNextClick(click, window)

    # extract toppings info before moving to next step
    numOfCreamCheese = int(eval(entryCreamCheese.getText()))
    numOfOnions = int(eval(entryOnions.getText()))
    numOfLettuce = int(eval(entryLettuce.getText()))
    numOfTomato = int(eval(entryTomato.getText()))
    numOfButter = int(eval(entryButter.getText()))

    # undraw topping options
    entryCreamCheese.undraw()
    entryOnions.undraw()
    entryLettuce.undraw()
    entryButter.undraw()
    entryTomato.undraw()
    promptCreamCheese.undraw()
    promptOnions.undraw()
    promptLettuce.undraw()
    promptTomato.undraw()
    promptButter.undraw()


    # ORDER STEP 3: ADD-ONS
    # give customer optional add-on of lox (smoked salmon)
    stepMsg.setText("Step 3: Optional Add-on")

    promptLox1 = Text(Point(1.5, 3.3),
                      "Would you like to add\nsmoked salmon to your order?")
    promptLox1.draw(window)

    promptLox2 = Text(Point(1.5, 2.9), "About 0.1 lbs. is good for one bagel.")
    promptLox2.setSize(9)
    promptLox2.setStyle("italic")
    promptLox2.draw(window)
              
    promptLox3 = Text(Point(1.2, 2.2), "Lox ($9.50/lb.): ")
    promptLox3.draw(window)
    
    entryLox = Entry(Point(2.2, 2.2), 4)
    entryLox.setFill("PaleTurquoise")
    entryLox.setStyle("bold")
    entryLox.setText("0")
    entryLox.draw(window)

    # wait for click before moving to step 4 of order
    click = window.getMouse()
    getNextClick(click, window)

    # extract lox info
    amountOfLox = float(eval(entryLox.getText()))

    # undraw step 3 objects before moving onto Step 4
    promptLox1.undraw()
    promptLox2.undraw()
    promptLox3.undraw()
    entryLox.undraw()

    
    # ORDER STEP 4: ORDER SUMMARY
    orderTitle.setText("Review your order")
    stepMsg.setText("Step 4: Order Summary")

    # first, calculate prices of bagels and smoked salmon
    bagelTotal = calculateBagelTotal(numOfPlain, numOfWhole, numOfEverything)
    loxTotal = calculateLoxTotal(amountOfLox)

    # calculate totals
    subTotal = calculateSubTotal(bagelTotal, loxTotal)
    tax = calculateTax(subTotal)
    grandTotal = calculateGrandTotal(subTotal, tax)

    # display totals
    subTotalMsg = Text(Point(1.3, 3), "Subtotal: $"+"{0:.2f}".format(subTotal))
    taxMsg = Text(Point(1.1, 2.7), "Tax: $"+"{0:.2f}".format(tax))
    grandTotalMsg = Text(Point(1.3, 2.2), "Grand total: $"+"{0:.2f}".format(grandTotal))
    grandTotalMsg.setStyle("bold")

    subTotalMsg.draw(window)
    taxMsg.draw(window)
    grandTotalMsg.draw(window)

    nextMsg.setText("Place Order")

    window.getMouse()
    getNextClick(click, window)

    # undraw Step 4 objects before moving to step 5
    subTotalMsg.undraw()
    taxMsg.undraw()
    grandTotalMsg.undraw()

    # ORDER STEP 5: Closing message
    nextMsg.setText("Close")
    orderTitle.setText("Order complete")
    stepMsg.setText("Bagels are on their way!")

    if (totalNumOfBagels > 24):
        orderInfoMsg = "Your order will be ready for\npickup in about 30 minutes."
    else:
        orderInfoMsg = "Your order will be ready for\npickup in about 15 minutes."
    orderInfo = Text(Point(1.5, 1.7), orderInfoMsg)
    orderInfo.draw(window)

    # open faced bagel image
    leftHalfOuter = Circle(Point(1, 3), 0.4)
    leftHalfOuter.setFill("sandybrown")
    leftHalfInner = Circle(Point(1, 3), 0.13)
    leftHalfInner.setFill("turquoise")
    
    leftHalfOuter.draw(window)
    leftHalfInner.draw(window)

    rightHalfOuter = Circle(Point(2, 3), 0.4)
    rightHalfOuter.setFill("sandybrown")

    rightHalfInner = Circle(Point(2, 3), 0.13)
    rightHalfInner.setFill("turquoise")

    creamCheeseOuter = Circle(Point(2, 3), 0.36)
    creamCheeseOuter.setFill("white")

    creamCheeseInner = Circle(Point(2, 3), 0.16)
    creamCheeseInner.setFill("sandybrown")

    rightHalfOuter.draw(window)
    creamCheeseOuter.draw(window)
    creamCheeseInner.draw(window)
    rightHalfInner.draw(window)


    # EXIT WINDOW
    window.getMouse()
    getNextClick(click, window)
    window.close()


# waits until user clicks within the space of the "Next >>>" button
def getNextClick(click, window):
        while (click.getX() < 0.8 or click.getX() > 2.2
           or click.getY() < 0.3 or click.getY() > 0.7):
            click = window.getMouse()


# returns the total cost of the bagels
def calculateBagelTotal(numOfPlain, numOfWhole, numOfEverything):
    # intialize individual bagel prices
    plainPrice = 1.75
    wholePrice = 1.75
    everythingPrice = 1.85

    # calculate total price of all bagels
    bagelTotal = ((numOfPlain*plainPrice) + (numOfWhole*wholePrice)
                  + (numOfEverything*everythingPrice))
    return bagelTotal


# returns the sub total (before tax) of bagels and lox
def calculateSubTotal(bagelTotal, loxTotal):
    subTotal = bagelTotal + loxTotal
    return subTotal

    
# returns grand total by adding taxes to the subtotal   
def calculateGrandTotal(subTotal, tax):
    grandTotal = subTotal + tax
    return grandTotal


# intializes tax rate and applies it to subtotal, returns tax amount
def calculateTax(subTotal):
    taxRate = 0.075
    tax = taxRate * subTotal
    return tax


# returns total cost of the smoked salmon
def calculateLoxTotal(amountOfLox):
    # intialize lox price per poind
    loxPrice = 9.50

    # calculate total price
    loxTotal = loxPrice * amountOfLox
    return loxTotal


main()
