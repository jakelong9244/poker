import random

#Dicts for Reference
suitDeck = {
    "♦":1,
    "♣":2,
    "♥":3,
    "♠":4
    }
valueDeck = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
    }

#Create Deck
def deckCreate(deck):
    suitDeckValues = list(suitDeck.keys())
    valueDeckValues = list(valueDeck.keys())
    for x in range(len(suitDeck)):    
        for y in range(len(valueDeck)):
            deck += [str(suitDeckValues[x] + valueDeckValues[y])]
    random.shuffle(deck)
    return(deck)

#Deal Cards
def dealNewCards(deck):
    hand = [list.pop(deck)]
    hand += [list.pop(deck)]

    return hand, deck

#Deal Cards to Table
def dealTable(deck):
    card = [list.pop(deck)]
    return card, deck

#Sort Hand
def sortHand(hand):
    for x in range(len(hand)):
        for y in range (x+1, len(hand)):
            if suitDeck[hand[x][0]] < suitDeck[hand[x+1][0]]:
                hand.append(hand[x])
                hand.pop(x)
            elif suitDeck[hand[x][0]] == suitDeck[hand[x+1][0]] and valueDeck[hand[x][1:]] < valueDeck[hand[x+1][1:]]:
                hand.append(hand[x])
                hand.pop(x)
            else:
                hand.append(hand[x+1])
                hand.pop(x+1)
    return hand
    
#Check for Straight Flush
def checkStraightFlush(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0
    suit = 0
    checkForStraight = []
    handValues = []

    for a in range(1,5):
        for b in range(len(hand)):
            if suitDeck[hand[b][0]] == a:
                counter += 1
                suit = hand[b][0]
        if counter >= 5:
            #Old Straight Checker Code
            """for y in range(len(hand)):
                if hand[y][0] == suit:
                    checkForStraight.append(valueDeck[hand[y][1:]])

            if sorted(checkForStraight) == list(range(min(checkForStraight),max(checkForStraight)+1)):
                for z in range(len(hand)):
                    if hand[z][0] == suit:
                        return hand[z]
            else:
                return False

            for y in range(len(hand)):
                if hand[y][0] == suit:
                    handValues.append(valueDeck[hand[y][1:]])"""
            #New Code
            handValues = sorted(handValues,reverse=True)
            counter = 0

            for x in range(len(handValues)-1):
                if counter >= 4:
                    for y in range(len(hand)):
                        if valueDeck[hand[y][1:]] == handValues[x-4]:
                            return hand[y]
                else:
                    if handValues[x] - handValues[x+1] == 1:
                        checkForStraight.append(handValues[x])
                        counter += 1
                    else:
                        checkForStraight = []
                        counter = 0

        else:   
            counter = 0

    return False


#Check for Four of a Kind
def checkFourOfKind(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0

    for x in range(len(hand)):
        for y in range(1, len(hand)):
            if valueDeck[hand[x][1:]] == valueDeck[hand[y][1:]]:
                counter += 1
        if counter == 4:
            return hand[x]
        else:
            counter = 0
    return False

#Check for Full House
def checkFullHouse(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0

    for x in range(len(hand)):
        for y in range(x+1, len(hand)):
            if valueDeck[hand[x][1:]] == valueDeck[hand[y][1:]]:
                counter += 1
        if counter >= 3:
            counter = 0
            for z in range(len(hand)):
                if z != x:                        
                    for y in range(x+1, len(hand)):
                        if valueDeck[hand[z][1:]] == valueDeck[hand[y][1:]]:
                            counter += 1
                    if counter >= 2:
                        return hand[x],hand[z]
                    else:
                        counter = 0            
        else:
            counter = 0
    return False

#Check Flush
def checkFlush(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0
    suit = 0

    for a in range(1,5):
        for b in range(len(hand)):
            if suitDeck[hand[b][0]] == a:
                counter += 1
                suit = hand[b][0]
        if counter >= 5:
            for x in range(len(hand)):
                if hand[x][0] == suit:
                    return hand[x]
        else:   
            counter = 0

    return False

#Check for Straight 
def checkStraight(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0
    handValues = []
    checkForStraight = []

    for y in range(len(hand)):
        handValues.append(valueDeck[hand[y][1:]])
    handValues = sorted(handValues,reverse=True)

    for x in range(len(handValues)-1):
        if counter >= 4:
            for y in range(len(hand)):
                if valueDeck[hand[y][1:]] == handValues[x-4]:
                    return hand[y]
        else:
            if handValues[x] - handValues[x+1] == 1:
                checkForStraight.append(handValues[x])
                counter += 1
            else:
                checkForStraight = []
                counter = 0

    return False

#Check for Three of a Kind
def checkThreeOfKind(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0

    for x in range(len(hand)):
        for y in range(x+1, len(hand)):
            if valueDeck[hand[x][1:]] == valueDeck[hand[y][1:]]:
                counter += 1
        if counter >= 3:
            return hand[x]   
        else:
            counter = 0
    return False

#Check for Two Pair
def checkTwoPair(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    counter = 0

    for x in range(len(hand)):
        for y in range(x+1, len(hand)):
            if valueDeck[hand[x][1:]] == valueDeck[hand[y][1:]]:
                counter += 1
        if counter >= 2:
            return hand[x]   
        else:
            counter = 0
    return False

#Check for Pair
def checkPair(handCards,tableCards):
    hand = sortHand(handCards + tableCards)

    for x in range(len(hand)):
        for y in range(x+1, len(hand)):
            if valueDeck[hand[x][1:]] == valueDeck[hand[y][1:]]:
                return hand[x]

    return False

#Check for High Card
def checkHighCard(handCards,tableCards):
    hand = sortHand(handCards + tableCards)
    highCard = "♦2"

    for x in range(len(hand)):
        if valueDeck[hand[x][1:]] > valueDeck[highCard[1:]]:
            highCard = hand[x]
    return highCard


#Determine Hand Strength
def determineHand(hand,table):
    besthand = checkStraightFlush(hand,table)
    if besthand is False:
        besthand = checkFourOfKind(hand,table)
        if besthand is False:
            besthand = checkFullHouse(hand,table)
            if besthand is False:
                besthand = checkFlush(hand,table)
                if besthand is False:
                    besthand = checkStraight(hand,table)
                    if besthand is False:
                        besthand = checkThreeOfKind(hand,table)
                        if besthand is False:
                            besthand = checkTwoPair(hand,table)
                            if besthand is False:
                                besthand = checkPair(hand,table)
                                if besthand is False:
                                    besthand = checkHighCard(hand,table)
                                    return besthand, "High Card"
                                else:
                                    return besthand, "One Pair"
                            else:
                                return besthand, "Two Pairs"
                        else:
                            return besthand, "Three of a Kind"
                    else:
                        return besthand, "Straight"
                else:
                    return besthand, "Flush"
            else:
                return besthand, "Full House"
        else:
            return besthand, "Four of a Kind"
    else:
        return besthand, "Straight Flush"

#Player Check
def askCheck(checkPlayerBehindCheck):
    checkCheck = ""
    
    if checkPlayerBehindCheck is True:
        while checkCheck != "y" or checkCheck != "n": #Validate Response
            checkCheck = input("Would you like to check?(y/n): ")
            if checkCheck != "y" or checkCheck != "n":
                print("Invalid Response\n")
        if checkCheck.lower() == "y":
            return True
        else:
            return False

    return False

#Player Bet
def askBet():
    betAmount = 0
    checkBet = ""

    while checkBet != "y" or checkBet != "n": #Validate Response
        checkBet = input("Would you like to bet?(y/n): ")
        if checkBet != "y" or checkBet != "n":
            print("Invalid Response\n")

    if checkBet == "y":
        while betAmount == 0 or betAmount.isnumeric() is False: #Validate Response
            betAmount = input("How much would you like to bet: ")
            if betAmount.isnumeric() is False:
                print("Invalid Response\n")
            elif betAmount == 0:
                print("You can't bet nothing.")
        return betAmount
    else:
        return False
    

#Player Call
def askCall(playerMoney,betBehindAmount):
    checkCall = ""

    while checkCall != "y" or checkCall != "n": #Validate Response
        checkCall = input("Would you like to call?(y/n): ")
        if checkCall != "y" or checkCall != "n":
            print("Invalid Response\n")
    
    if checkCall == "y":
        if playerMoney < betBehindAmount:
            print("You don't have enough money to call.")
            return False
        else:
            return betBehindAmount
    else:
        return False

#Player Raise:
def askRaise(playerMoney,betBehindAmount):
    checkRaise = ""

    while checkRaise != "y" or checkRaise != "n": #Validate Response
        checkRaise = input("Would you like to raise?(y/n): ")
        if checkRaise != "y" or checkRaise != "n":
            print("Invalid Response\n")
    
    if checkRaise == "y":
        if playerMoney < betBehindAmount:
            print("You don't have enough money to raise.")
            return False
        else:
            return betBehindAmount
    else:
        return False


#Initialize Betting Variables
checkPlayerBehindCheck = True

#Initialize Player Starting Money
moneyP1 = 10000
moneyP2 = 10000
moneyP3 = 10000
moneyP4 = 10000

#Shuffle Deck
deck = deckCreate([])

#Dealing Cards
handP1, deck = dealNewCards(deck)
handP2, deck = dealNewCards(deck)
handP3, deck = dealNewCards(deck)
handP4, deck = dealNewCards(deck)

#Dealing Flop
table = []
for x in range(3):
    dealtCardAndDeck = dealTable(deck)
    table += dealtCardAndDeck[0]
    deck = dealtCardAndDeck[1]

#Dealing Turn
dealtCardAndDeck = dealTable(deck)
table += dealtCardAndDeck[0]
deck = dealtCardAndDeck[1]

#Dealing River
dealtCardAndDeck = dealTable(deck)
table += dealtCardAndDeck[0]
deck = dealtCardAndDeck[1]

besthand, handtype = determineHand(handP1,table)

