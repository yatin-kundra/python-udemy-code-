# dictionary containing info
# compare a value of the key from the dictionaries and then remove the previous  entity form the dictionarie and
# compare this one with the next random
# if the ans is right keep playing , else you lose
#              we got 2 people
                    # now we gota compare and ask user if heigh or low  -->()
                        # if user is right then continue
# do you want to play again


import random
from game_data import data

a = {}
b = {}
def game():
    n = len(data)
   ################################## #rand = random.choice(data)
   ################################## #a["name", "description", "country"] = data[r]["name"]["description"]["country"]

        # person 1
    game_continue = True


    score = 0

    while  game_continue :


        r = random.randint(0, n)
        a = data[r]
        for key in a:
            print(key + ":", data[r][key])
        print(
            "\n\n*****************************************************************************************************************\n\n")
        # person 2
        r = random.randint(0, n)
        b = data[r]
        for key1 in b:
            print(key1 + ":", data[r][key1])

                ##### **** have to remove a and b  at each play form data


        user = input("heigh(h) or low(l): ").lower()


        if user == "h" and a["follower_count"] < b["follower_count"]:
            game_continue = True
            score = score +1

        elif user == "l" and a["follower_count"] > b["follower_count"]:
            game_continue = True
            score = score +1


        elif user == "h" and a["follower_count"] > b["follower_count"]:
            game_continue = False

        elif user == "l" and a["follower_count"] < b["follower_count"]:
            game_continue = False

        elif a["follower_count"] < b["follower_count"]:
            score = score + 1

        else:
            print("error !!!!")
    print(score)



        # print()

    #################################### # r = random.randint(0,n)
    #################################### # b["name", "description", "country"] = data[r]["name"]["description"]["country"]
    #################################### # print(b)
game()
