import random

def sumHand(L):
    sum = 0
    for i in range(len(L)):
        if (L[i] >= 11 and L[i] <= 13):
            sum += 10
        elif (L[i] >= 2 and L[i] <= 10):
            sum += L[i]
        elif (L[i] == 1):
            if ((sum + 11) > 21):
                sum += 1
            else:
                sum+= 11
    
    return sum

def displayHand(L):
    sum = sumHand(L)
    hand = ""
    for i in range(len(L)):
        if (L[i] == 1):
            hand += "A "
        elif (L[i] == 11):
            hand += "J "
        elif (L[i] == 12):
            hand += "Q "
        elif (L[i] == 13):
            hand += "K "
        elif (L[i] >= 2 or L[i] <= 10):
            hand += str(L[i]) + " "
    
    print(hand + "   " + str(sum))

def dealCard():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card = random.randrange(1,14)
    return card


def getRank(score):
    if (score >= 95):
        return "Ace!"
    elif (score >= 85):
        return "King"
    elif (score >= 75):
        return "Queen"
    elif (score >= 50):
        return "Jack"
    elif (score >= 25):
        return "Commoner"
    else:
        return "Noob"

def welcome():
    print()
    print("Welcome to BlackJack!")
    print()

def main():
    round = 1
    score = 100
    welcome()
    while (round <= 5):
        print("Round " + str(round))
        print("Score: " + str(score))
        bust = False
        card1 = dealCard()
        card2 = dealCard()
        hand = [card1, card2]
        displayHand(hand)
        action = ''
        while (action != 'stand' and bust == False):
            while (action != 'hit' and action != 'stand'):
                action = input("Would you like to \'hit\' or \'stand\': ")
                print()
            if (action == 'stand'):
                score = score - (21 - sumHand(hand))
            elif (action == 'hit'):
                hand.append(dealCard())
                displayHand(hand)
                if (sumHand(hand) > 21):
                    score = score - 21
                    bust = True
                    print("Bust!")
                action = ''
        round += 1
    print("Final score: " + str(score) + ",  Your rank: " + getRank(score))

main()