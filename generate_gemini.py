import google.generativeai as genai
import os

import google.generativeai as genai
import os

MY_GOOGLE_API_KEY = "AIzaSyDj3pMMwkX2wCEtkXIGBPEV99kkHNNzuAM"

prompt_text = input("Enter your prompt for the AI: ")

try:
    # Configure the client with your API key
    genai.configure(api_key=MY_GOOGLE_API_KEY)

    print(f"\nSending prompt: '{prompt_text}'")
    print("Waiting for the AI to respond...")

    # Initialize the model
    # I fixed the model name to the one that should work
    model = genai.GenerativeModel('models/gemini-2.5-flash')

    # This is the main API call
    response = model.generate_content(prompt_text)

    # Get the AI's text response
    generated_text = response.text

    print("\n--- AI Response ---")
    print(generated_text)
    print("-------------------")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Did you forget to add your Google API key?")