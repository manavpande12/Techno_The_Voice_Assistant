import requests
import io
from PIL import Image
from SpeakGet.Talk import speak, get_user_input
import os


with open('API/HuggingFaceApi.txt','r') as file:
    apikey = file.read().strip()

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"{apikey}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def Generate_Images(prompt):

    # Create the "images" directory if it doesn't exist
    image_dir = "images"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Check the number of images in the directory
    image_count = len([name for name in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, name))])

    if image_count >= 25:
        while True:
            speak("Do you want to delete all generated images? Please say yes or no.")
            response = get_user_input().lower()

            if "yes" in response:
                for filename in os.listdir(image_dir):
                    os.remove(os.path.join(image_dir, filename))
                speak("All generated images deleted.")
                break

            elif "no" in response:
                speak("Okay.")
                break

            else:
                speak("I didn't understand.")

    prompt = prompt.lower()
    prompt +=" A stunning, highly detailed 4K ULTRA HD IMAGE , with a dreamy atmosphere, vibrant colors, and intricate textures that evoke a sense of wonder and beauty."
    speak("Generating Image...")
    speak("It may take some time. I'll let you know when it's ready.")


    image_bytes = query({
        "inputs": prompt,
    })

    # Generate a prompt name as filename
    prompt=prompt.replace("A stunning, highly detailed 4K ULTRA HD IMAGE , with a dreamy atmosphere, vibrant colors, and intricate textures that evoke a sense of wonder and beauty.","")
    prompt=prompt.upper()
    filename = f"{prompt}.PNG"
    image_path = os.path.join(image_dir, filename)

    # Save the generated image
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    speak("Image generated.")

    # Opening the generated image using the default image viewer
    image = Image.open(io.BytesIO(image_bytes))
    image.show()





