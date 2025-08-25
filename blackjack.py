import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def play_blackjack():
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)
        print(f"\nYour cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score == 0:
            return "Blackjack! You win", player_score, dealer_score
        elif player_score > 21:
            return "You busted! Dealer wins", player_score, dealer_score

        action = input("Type 'hit' or 'stand': ").lower()
        if action == "hit":
            player.append(deal_card())
        else:
            game_over = True

    while calculate_score(dealer) < 17:
        dealer.append(deal_card())

    dealer_score = calculate_score(dealer)
    print(f"\nDealer's cards: {dealer}, final score: {dealer_score}")

    if dealer_score > 21:
        return "Dealer busted! You win", player_score, dealer_score
    elif dealer_score == player_score:
        return "Draw", player_score, dealer_score
    elif player_score > dealer_score:
        return "You win", player_score, dealer_score
    else:
        return "Dealer wins", player_score, dealer_score