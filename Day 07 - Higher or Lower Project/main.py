from art import logo, vs
from game_data import data
import random

print(logo)

random_word=random.choice(data)
second_random_word=random.choice(data)

while second_random_word == random_word:
    second_random_word = random.choice(data)

score=0
game=True
show_score = False


def compare_follower(a_follower_count, b_second_follower_count, c_user_answer):
    if follower_count > second_follower_count:
        return user_answer == 'A'
    else:
        return user_answer == 'B'


while game:
    name = random_word['name']
    follower_count = random_word['follower_count']
    description = random_word['description']
    country = random_word['country']

    second_name = second_random_word['name']
    second_follower_count = second_random_word['follower_count']
    second_description = second_random_word['description']
    second_country = second_random_word['country']

    if show_score:
        print(f"You're right! Current score: {score}\n")


    print(f"Compare A: {name}, {description}, {country}")
    print(vs)
    print(f"Compare B: {second_name}, {second_description}, {second_country}")
    user_answer=input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare_follower(follower_count, second_follower_count, user_answer)

    print("\n" * 20)
    print(logo)

    if result:
        score += 1
        show_score = True
        random_word = second_random_word

        second_random_word = random.choice(data)
        while second_random_word == random_word:
            second_random_word = random.choice(data)

    else:
        print(f"Sorry, that's wrong. Final score:{score}")
        game=False





