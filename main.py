import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")


print("AI Story Generator")
print("Every Choice Creates a New Story")

character_name = input("What is the character's name : ")
story_type = input ("Choose a story type :")
location = input ("Choose the location : ")
age = input ("Enter the character's age : ")
goal = input ("What is the character's goal ?")
ending = input ("What type of ending do you want ?")

print("\n---- YOUR STORY CHOICES ----")
print("Story type :" , story_type)
print("Location :" , location)
print("Character's age :" , age)
print("Character's goal :" , goal)
print("Ending :" , ending)

story_data = {"name" : character_name , "type" : story_type , "location" : location , "age" : age , "goal" : goal , "ending" : ending}

def creat_prompt(story_data) :
    prompt = f"""
You are a creative story writer.

Write a story based on the following choices

The main character's name is {story_data["name"]}.
Create a complete {story_data["type"]} story.
The story takes place in {story_data["location"]}.
The main character is {story_data["age"]} years old.
The character's goal is {story_data["goal"]}.
The story should have a {story_data["ending"]} ending.

Write a short story of about 250-350 words,divided into 5-7 paragraphs.
Include a clear beginning , main events , and ending.
Make the story engaging and creative .
"""

    return prompt

story_prompt = creat_prompt(story_data)
print("\n---- GENERATED PROMPT ----")
print(story_prompt)

response = model.generate_content(story_prompt)

print("\n---- YOUR GENERATED STORY ----")
print(response.text)