import google.generativeai
from config import GEMINI_API_KEY
import subprocess

# Configure Gemini
google.generativeai.configure(api_key=GEMINI_API_KEY)
model = google.generativeai.GenerativeModel("models/gemini-2.0-pro-exp-02-05")
#gemini-1.5-pro-latest
# Define the prompt
prompt = (
    "You're controlling a Windows computer. Open MS Paint, draw a rectangle in the center and write word 'cool' in the rectangle. "
  
)

# Send prompt to Gemini for processing
response = model.generate_content(prompt)
response_text = response.text.lower()

# Print the Gemini response
print("Gemini says:", response.text)

# Send the response text to the server
proc = subprocess.Popen(
    ["python", "assignment4.py"], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
    text=True
)

# Communicate the prompt to the server
server_response, _ = proc.communicate(response_text)

# Print the server's response (actions performed)
print("Server response:", server_response)
