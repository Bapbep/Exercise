import random
import time

# 定义卡牌数据结构
cards = [
    {"Name": "Diablo", "Health": 100, "Attack": 90, "Defense": 60},
    {"Name": "Medusa", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Jester", "Health": 120, "Attack": 60, "Defense": 90},
    {"Name": "Troll", "Health": 150, "Attack": 40, "Defense": 94},
    {"Name": "Specter", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Mist", "Health": 100, "Attack": 75, "Defense": 65},
    {"Name": "Savage", "Health": 100, "Attack": 90, "Defense": 50},
    {"Name": "Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    {"Name": "Wimp", "Health": 110, "Attack": 40, "Defense": 85},
    {"Name": "Sorcerer", "Health": 100, "Attack": 70, "Defense": 55}
]

def draw_cards(deck, num_cards):
    return random.sample(deck, num_cards)

def display_cards(deck):
    for i, card in enumerate(deck):
        print(f"{i+1}. {card['Name']} (Health: {card['Health']}, Attack: {card['Attack']}, Defense: {card['Defense']})")

def fight(player_card, opponent_card):
    print(f"Player's {player_card['Name']} attacks Opponent's {opponent_card['Name']}!")
    if player_card['Attack'] > opponent_card['Health']:
        print(f"Opponent's {opponent_card['Name']} is defeated!")
        return True
    else:
        if opponent_card['Defense'] > 0:
            opponent_card['Defense'] -= player_card['Attack']
            if opponent_card['Defense'] < 0:
                opponent_card['Health'] += opponent_card['Defense']
                opponent_card['Defense'] = 0
        else:
            opponent_card['Health'] -= player_card['Attack']
        print(f"Opponent's {opponent_card['Name']} now has Health: {opponent_card['Health']}, Defense: {opponent_card['Defense']}")
        return False

def main():
    print("Welcome to the Card Role-Playing Game!")
    player_deck = draw_cards(cards, 5)
    opponent_deck = draw_cards(cards, 5)

    while player_deck and opponent_deck:
        print("\nPlayer's Deck:")
        display_cards(player_deck)

        opponent_card = random.choice(opponent_deck)
        print(f"\nOpponent's Card: {opponent_card['Name']} (Health: {opponent_card['Health']}, Attack: {opponent_card['Attack']}, Defense: {opponent_card['Defense']})")

        player_choice = int(input("Choose a card to fight with (1-5): ")) - 1
        player_card = player_deck[player_choice]

        if fight(player_card, opponent_card):
            opponent_deck.remove(opponent_card)

        time.sleep(3)
        print("\nNow it's the opponent's turn.")

        if opponent_deck:
            opponent_card = random.choice(opponent_deck)
            print(f"\nOpponent's Card: {opponent_card['Name']} (Health: {opponent_card['Health']}, Attack: {opponent_card['Attack']}, Defense: {opponent_card['Defense']})")

            print("\nPlayer's Deck:")
            display_cards(player_deck)

            player_choice = int(input("Choose a card to defend with (1-5): ")) - 1
            player_card = player_deck[player_choice]

            if fight(opponent_card, player_card):
                player_deck.remove(player_card)

        time.sleep(3)
        print("\nA new round will begin in a few seconds.")

    if not player_deck:
        print("The opponent won!")
    else:
        print("You won!")

if __name__ == "__main__":
    main()
