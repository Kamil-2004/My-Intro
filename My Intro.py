logo = """


88                                                
88                ,d                              
88                88                              
88  8b,dPPYba,  MM88MMM  8b,dPPYba,   ,adPPYba,   
88  88P'   `"8a   88     88P'   "Y8  a8"     "8a  
88  88       88   88     88          8b       d8  
88  88       88   88,    88          "8a,   ,a8"  
88  88       88   "Y888  88           `"YbbdP"'   

"""
print(logo)

import random

# Define a class to handle the introduction
class MyIntro:
    def __init__(self, name, age, city, country, education, interests, goals, skills):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.education = education
        self.interests = interests
        self.goals = goals
        self.skills = skills

    def display_intro(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am {self.age} years old and I live in {self.city}, {self.country}.")
        print(f"I am currently pursuing {self.education}.")
        print("My interests include:")
        for interest in self.interests:
            print(f"- {interest}")
        print("My goals are:")
        for goal in self.goals:
            print(f"- {goal}")
        print("Here are some of my skills:")
        for skill in self.skills:
            print(f"- {skill}")

# Create an instance of MyIntro with your information
my_intro = MyIntro(
    name="Muhammad Kamil",
    age=20,
    city="Islamabad",
    country="Pakistan",
    education="the Python course from Atomcamp",
    interests=["Learning different programming languages"],
    goals=["Want to become a Programmer"],
    skills=["German Language", "Python", "Power BI", "R Programming"]
)

# Display the introduction
my_intro.display_intro()
