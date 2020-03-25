# BlackJack or 21 game



import random


def play_game():


    print("David's Game of Blackjack.")

    print("Blackjack in 5 games.")

    # variables

    five_games = 0

    house_score = 0

    player_score = 0



    while five_games < 5:


        print("Game " + str(five_games + 1) + ". I am now dealing the cards")


        house_cards = []


        player_cards = []



        while len(house_cards) != 2:

            house_cards.append(random.randint(1, 11))

            if len(house_cards) == 2:

                print("The House has X &", house_cards[1])




        while len(player_cards) != 2:

            player_cards.append(random.randint(1, 11))

            if len(player_cards) == 2:

                print("You have ", player_cards)




        if sum(house_cards) == 21:


            house_score += 1

            print("The house has 21 and wins!")

        elif sum(house_cards) > 21:


            player_score += 1

            print("The house has over 21 and is busted!")




        while sum(player_cards) < 21:

            action_taken = str(input("Do you want to stay or hit?  "))

            if action_taken == "hit":

                player_cards.append(random.randint(1, 11))

                print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)

            else:

                print("The house has a total of " + str(sum(house_cards)) + " with ", house_cards)

                print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)

                if sum(house_cards) > sum(player_cards):


                    house_score += 1

                    print("The House wins!")

                else:


                    player_score += 1

                    print("You win!")

                    break



        if sum(player_cards) > 21:


            house_score += 1

            print("You BUSTED! House wins.")

        elif sum(player_cards) == 21:


            player_score += 1

            print("You have BLACKJACK! You Win! 21")




        print("Current Best of 5: ")

        print("The House: " + str(house_score) + " games" + " - to - You: " + str(player_score) + " games")

        print("This is Blackjack: Best of Five!")

        five_games += 1





play_game()








