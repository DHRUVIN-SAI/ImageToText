                                                         AI-Powered Story Generator for Kids Using Images as Input
A.PROJECT OVERVIEW
PROBLEM STATEMENT SOLUTION: To use object detection tools,NLP Tools,converting .text files to .mp4 to give an modulated audio.
OBJECTIVE:To make an AI-Generated Image to Story for kids in a fun tone.
GOALS:To Generate a story from given image.
TARGET:Most Definitely for children as it involves a fun tone of voice.
B.TECHNOLOGY STACK
IMAGE TO TEXT:YOLO(You Look Only Once) is an image detection software used to identify the messages using pre-trained AI models,Open CV is a library to access the large number of available classes.
TEXT TO STORY: Using Hugging face transformers to generate an Story from it.
STORY TO VOICE:Converting the Story into a .text file and further using python to convert it into an .mp4 file and using some ai software to change the voice into a fun tone.
VERSIONS:YOLOv3-tiny	COCO trainval	test-dev	33.1	5.56 Bn	220 , Hugging Face Transformers 2024
C.SYSTEM REQUIREMENTS
HARDWARE:One CPU is needed to run the Open CV and 3-6 intel cores are needed to run the code
SOFTWARE:Python Idle,Visual Code,Yolo Software,Google Collab
D.INSTALLATION AND SETUP INSTRUCTIONS
1. Cloning the repository(https://github.com/DHRUVIN-SAI/ImageToText.git)
2. Installing dependencies (npm install, pip install, etc.).
3. Database configuration and initialization choco 
4. Running the application (e.g., npm start, python manage.py runserver).
CODE STRUCTURE:

import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


ENDPOINT = "https://your-image-to-story-api.com/generatep"

def generate_story(image_path):
    try:
        
        with open(image_path, "rb") as image_file:
            
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }
            files = {
                "image": image_file
            }

            
            response = requests.post(ENDPOINT, headers=headers, files=files)
        if response.status_code == 100:
            data = response.json()
            return data.get("story", "No story found in the response.")
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "_main_":
   
    image_path = r"C:\Users\sajja\OneDrive\Desktop\image to text\imageofahorse.jpg"  # Replace with actual image file path
    story = generate_story(image_path)
    print("Generated Story:", story)
I.Challenges and solutions
The challenges we have faced are that many of the repositories do not contain the simplest method possible instead it gives a elaborate description using various tools.
These challenges can be addressed only by trail and error only.
II.HOSTING AND DEPLOYMENT
The Hosting and Deployment is done from Github Pages.
The Output is not Achieved.


