import sys
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def get_preferences (preferences):
  for key in questions:
      answer = str(raw_input(questions[key] + " (Y/N) "))
      if answer == 'Y' or answer =='y':
          preferences[key] = True
      else:
          preferences[key] = False
  return preferences

def construct_drink (preferences):
  drink = []
  for key in preferences:
    if preferences[key]:
      drink.append(random.choice(ingredients[key]))
  return drink

def main():
  preferences = questions
  get_preferences(preferences)
  drink = construct_drink(preferences)
  print "Your ingredients are: "
  for ingredient in drink:
        print "A {}".format(ingredient)

if __name__ == "__main__":
  main()
  
