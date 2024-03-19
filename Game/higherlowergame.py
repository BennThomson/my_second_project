"""
Welcome to the higher or lower game
"""
import random
from art import logo
from art import vs

data = [
    {
        "name":"Selena Gomez",
        "follower_count": 429,
        "description":"Musician and actress",
        "country":"United States",
    },
    {
        "name":"Instagram",
        "follower_count": 670,
        "description":"Social Media Platform",
        "country":"United states",        
    },
    {
        "name":" Cristiano Ronaldo",
        "follower_count": 624,
        "description":"Classic Footballer",
        "country":"Portugal", 
    },
    {
        "name":"Lionesl Messi",
        "follower_count": 501,
        "description":"Classic Footballer and businessman",
        "country":"Argentina",      
    },
    {
        "name":"Zidan",
        "follower_count": 100,
        "description":"Classic Footballer and magical couch",
        "country":"Australia",
    },
    {
        "name":"Braine Weist",
        "follower_count": 50,
        "description":"British poet and musician",
        "country":"Great Britian",
    },
    {
        "name":"Ariana Grande",
        "follower_count":380,
        "description":"Musician and actress",
        "country":"United States",       
    },
    {
        "name":"Kim Kardashian",
        "follower_count":364 ,
        "description":"Media personality",
        "country":"United States",        
    },
    {
        "name":"Beyoncé",
        "follower_count":319 ,
        "description":"Musician and actress",
        "country":"United States",       
    },
    {
        "name":"Khloé Kardashian",
        "follower_count":310,
        "description":"Media personality",
        "country":"United States",       
    },
    {
        "name":"Nike",
        "follower_count": 306,
        "description":"Sportswear multinational",
        "country":"United States",        
    },
    {
        "name":"Kendall Jenner",
        "follower_count": 294,
        "description":"Media personality",
        "country":"United States",        
    },
    {
        "name":"Justin Bieber",
        "follower_count": 293 ,
        "description":"Musician",
        "country":"Canada",       
    },
    {
        "name":"National Geographic",
        "follower_count": 284 ,
        "description":"magazine",
        "country":"United States",        
    },
    {
        "name":"Taylor Swift",
        "follower_count": 283 ,
        "description":"Musician",
        "country":"United states"        
    },
    {
        "name":"Virat Kohli",
        "follower_count": 266 ,
        "description":"Cricketer",
        "country":"India"        
    },
    {
        "name":"Jennifer Lopez",
        "follower_count": 253,
        "description":"Musician and actress",
        "country":"United States"        
    }
]
print("Welcome to the Higher or lower game!")
print(logo)
score = 0
times_of_playing = 1
def play_game():
    while True:
        global score
        global times_of_playing
        if score > 0:
            print(f"your score is {score}")
        if times_of_playing == 1:
            random_person = data[random.randint(0,len(data) - 1)]
        print(f"compare A:{random_person["name"]},{random_person["description"]},from {random_person["country"]}")
        print(vs)
        random_person_2 = data[random.randint(0,len(data) - 1)]
        while random_person_2 == random_person:
            random_person_2 = data[random.randint(0,len(data) - 1)]
        print(f"compare B:{random_person_2["name"]},{random_person_2["description"]},from {random_person_2["country"]}")

        choice = input("Which one has more followers on instagram: A or B?: ").lower()
        winner = [k for k in sorted([random_person,random_person_2], key = lambda item : item["follower_count"],reverse=True)]
        if choice == "a":
            if random_person["follower_count"] == winner[0]["follower_count"]:
                random_person = random_person_2
                times_of_playing += 1
                score += 1
            else:
                print(f"You guessed it wrong\nYour score:{score}")
                break
        else:
            if random_person_2["follower_count"] == winner[0]["follower_count"]:
                score += 1
                times_of_playing += 1
            else:
                print(f"You guessed it wrong\nYour score:{score}")
                break
while input("you wanna play this game? (Y) for yes (N) for no:").lower() == "y":
    play_game()
else:
    print("Next time, try your luck")
