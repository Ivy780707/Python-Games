import random
import sys
# Preprocessing: Create deck of cards
deck = []
suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
for suit in suits:
    for rank in ranks:
        deck.append(rank + '-' + suit)

#洗牌
random.shuffle(deck)

#玩家第一輪的牌
player_cards = [deck.pop(), deck.pop()]
#莊家第一輪的牌
dealer_cards = [deck.pop(), deck.pop()]

#建立分數清單
player_point=[]
for card in player_cards:
    if card.split('-')[0]=='ACE':
        player_point.append(11)
    elif card.split('-')[0]=='JACK':
        player_point.append(10)
    elif card.split('-')[0]=='QUEEN':
        player_point.append(10)
    elif card.split('-')[0]=='KING':
        player_point.append(10)
    else:
        player_point.append(int(card.split('-')[0]))
    player_score=sum(player_point)
#檢查用
#print(player_cards)


dealer_point=[]
for card in dealer_cards:
    if card.split('-')[0]=='ACE':
        dealer_point.append(11)
    elif card.split('-')[0]=='JACK':
        dealer_point.append(10)
    elif card.split('-')[0]=='QUEEN':
        dealer_point.append(10)
    elif card.split('-')[0]=='KING':
        dealer_point.append(10)
    else:
        dealer_point.append(int(card.split('-')[0]))
dealer_score=sum(dealer_point)

#檢查用
#print(player_cards)
#print(dealer_cards)
#dealer_score=sum(dealer_point)


def restart_game():
    deck = []
    suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
    ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + '-' + suit)

#洗牌
    random.shuffle(deck)

#玩家第一輪的牌
    player_cards = [deck.pop(), deck.pop()]
#莊家第一輪的牌
    dealer_cards = [deck.pop(), deck.pop()]

#建立分數清單
    player_point=[]
    for card in player_cards:
        if card.split('-')[0]=='ACE':
            player_point.append(11)
        elif card.split('-')[0]=='JACK':
            player_point.append(10)
        elif card.split('-')[0]=='QUEEN':
            player_point.append(10)
        elif card.split('-')[0]=='KING':
            player_point.append(10)
        else:
            player_point.append(int(card.split('-')[0]))
    #print(player_cards)
    player_score=sum(player_point)

    dealer_point=[]
    for card in dealer_cards:
        if card.split('-')[0]=='ACE':
            dealer_point.append(11)
        elif card.split('-')[0]=='JACK':
            dealer_point.append(10)
        elif card.split('-')[0]=='QUEEN':
            dealer_point.append(10)
        elif card.split('-')[0]=='KING':
            dealer_point.append(10)
        else:
            dealer_point.append(int(card.split('-')[0]))
    dealer_score=sum(dealer_point)
    #進入遊戲
    while player_score<=21 :
        print('Your current value is',player_score)
        print('with the hand:'+ " ".join(str(x) for x in player_cards))
        print()
        answer=input('Hit or stay?(Hit=1,Stay=0):')
        if answer=='1':
            player_cards+=[deck.pop()]
            print('You draw',player_cards[-1])
            if player_cards[-1].split('-')[0]=='ACE':
                player_point.append(11)
            elif player_cards[-1].split('-')[0]=='JACK':
                player_point.append(10)
            elif player_cards[-1].split('-')[0]=='QUEEN':
                player_point.append(10)
            elif player_cards[-1].split('-')[0]=='KING':
                player_point.append(10)
            else:
                player_point.append(int(player_cards[-1].split('-')[0]))
            #print(player_cards)
            #print(player_point)
            player_score=sum(player_point)
            #print(player_score)
            if player_score>21:
                if 11 in player_point:
                    index_of_ace = player_point.index(11)
                    player_point[index_of_ace] = 1
                    player_score=sum(player_point)
                elif 11 not in player_point:
                    print('Your current value is Bust!(>21)')
                    print('with the hand:'+ " ".join(str(x) for x in player_cards))
                    print()
                    print('*** Dealer wins! ***')
                    restart=input('Want to play again?(y/n):')
                    if restart=='n':
                        sys.exit()
                    if restart=='y':
                        restart_game()
                

            #print('Your current value is',player_score)
        elif answer=='0':
            break
    print()
    print("Dealer's current value is",dealer_score)
    print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
    while dealer_score<=21:
        dealer_cards+=[deck.pop()]
        print('Dealer draw',dealer_cards[-1])
        if dealer_cards[-1].split('-')[0]=='ACE':
            dealer_point.append(11)
        elif dealer_cards[-1].split('-')[0]=='JACK':
            dealer_point.append(10)
        elif dealer_cards[-1].split('-')[0]=='QUEEN':
            dealer_point.append(10)
        elif dealer_cards[-1].split('-')[0]=='KING':
            dealer_point.append(10)
        else:
            dealer_point.append(int(dealer_cards[-1].split('-')[0]))
        #print(dealer_cards)
        dealer_score=sum(dealer_point)
        if dealer_score>player_score and dealer_score<=21:
            print("Dealer's current value is",dealer_score)
            print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
            print()
            print('*** Dealer wins! ***')
            restart=input('Want to play again?(y/n):')
            if restart=='n':
                sys.exit()
            elif restart=='y':
                restart_game()
        elif dealer_score>21:
            if 11 in dealer_point:
                index_of_ace = dealer_point.index(11)
                dealer_point[index_of_ace] = 1
                dealer_score=sum(dealer_point)
            elif 11 not in dealer_point:
                print("Dealer's current value is Bust!(>21)")
                print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
                print()
                print('*** You beat the dealer! ***')
                restart=input('Want to play again?(y/n):')
                if restart=='n':
                    sys.exit()
                if restart=='y':
                    restart_game()
        elif dealer_score==21:
            print()
        


#檢查用
#print(player_cards)
#print(dealer_cards)


#進入遊戲
while player_score<=21 :
    print('Your current value is',player_score)
    print('with the hand:'+ " ".join(str(x) for x in player_cards))
    print()
    answer=input('Hit or stay?(Hit=1,Stay=0):')
    if answer=='1':
        player_cards+=[deck.pop()]
        print('You draw',player_cards[-1])
        if player_cards[-1].split('-')[0]=='ACE':
            player_point.append(11)
        elif player_cards[-1].split('-')[0]=='JACK':
            player_point.append(10)
        elif player_cards[-1].split('-')[0]=='QUEEN':
            player_point.append(10)
        elif player_cards[-1].split('-')[0]=='KING':
            player_point.append(10)
        else:
            player_point.append(int(player_cards[-1].split('-')[0]))
        #print(player_cards)
        #print(player_point)
        player_score=sum(player_point)
        #print(player_score)
        if player_score>21:
            if 11 in player_point:
                index_of_ace = player_point.index(11)
                player_point[index_of_ace] = 1
                player_score=sum(player_point)
            elif 11 not in player_point:
                print('Your current value is Bust!(>21)')
                print('with the hand:'+ " ".join(str(x) for x in player_cards))
                print()
                print('*** Dealer wins! ***')
                restart=input('Want to play again?(y/n):')
                if restart=='n':
                    sys.exit()
                if restart=='y':
                    restart_game()
                

        #print('Your current value is',player_score)
    elif answer=='0':
        break
print()
print("Dealer's current value is",dealer_score)
print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
print()

while dealer_score<=21:
    
    dealer_cards+=[deck.pop()]
    print('Dealer draw',dealer_cards[-1])
    dealer_score=sum(dealer_point)
    if dealer_cards[-1].split('-')[0]=='ACE':
        dealer_point.append(11)
    elif dealer_cards[-1].split('-')[0]=='JACK':
        dealer_point.append(10)
    elif dealer_cards[-1].split('-')[0]=='QUEEN':
        dealer_point.append(10)
    elif dealer_cards[-1].split('-')[0]=='KING':
        dealer_point.append(10)
    else:
        dealer_point.append(int(dealer_cards[-1].split('-')[0]))
    #print(dealer_cards)
    dealer_score=sum(dealer_point)
    if dealer_score>player_score and dealer_score<=21:
        print()
        print("Dealer's current value is",dealer_score)
        print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
        print()
        print('*** Dealer wins! ***')
        restart=input('Want to play again?(y/n):')
        if restart=='n':
            sys.exit()
        elif restart=='y':
            restart_game()
    elif dealer_score>21:
        if 11 in dealer_point:
            index_of_ace = dealer_point.index(11)
            dealer_point[index_of_ace] = 1
            dealer_score=sum(dealer_point)
        elif 11 not in dealer_point:
            print()
            print("Dealer's current value is Bust!(>21)")
            print('with the hand:'+ " ".join(str(x) for x in dealer_cards))
            print()
            print('*** You beat the dealer! ***')
            restart=input('Want to play again?(y/n):')
            if restart=='n':
                sys.exit()
            if restart=='y':
                restart_game()
    


    



