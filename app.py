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