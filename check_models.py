import google.generativeai as genai

# -----------------------------------------------------------------
# PASTE YOUR SAME GOOGLE API KEY HERE
# -----------------------------------------------------------------
MY_GOOGLE_API_KEY = "AIzaSyDj3pMMwkX2wCEtkXIGBPEV99kkHNNzuAM"


try:
    # Configure the client with your API key
    genai.configure(api_key=MY_GOOGLE_API_KEY)

    print("--- Finding Available Models for your API Key ---")

    # List all available models
    for m in genai.list_models():
        # We only care about models that can be used for text generation
        if 'generateContent' in m.supported_generation_methods:
            print(f"Found model: {m.name}")

    print("-------------------------------------------------")
    print("\nACTION: Copy one of the model names listed above (e.g., 'models/gemini-pro')")
    print("and paste it into your 'generate_gemini.py' file.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please double-check that your Google API key is pasted correctly.")