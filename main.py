
"""
# At the command line, only need to run once to install the package via pip:
#
# $ pip install google-generativeai
# """
import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyCg05zNNdc5TRsZy6CvKY8b-26oWzTkjfw")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

convo.send_message("Generate 10 mcqs on the topic Flower with answers with 4 options")
data = convo.last.text
with open("mcq", "w") as f:
  f.write(data)

with open("mcq", "r") as f:
  data = f.readlines()
data = data[2:]
new_data = []
n = 0
l = 6
while l<=len(data)+6:
  new_data.append(data[n:l])
  n=l+1
  l=n+6
mcq = []
for a in range(len(new_data)):
  mcq.append({
    "questions": new_data[a][0].strip(),
    "options": [x.strip() for x in new_data[a] if ":" not in x and ")" in x],
    "answer": new_data[a][len(new_data[a])-1].strip()
  })
with open("mcq.json", "w") as f:
  json.dump(fp=f, obj=mcq, indent=4)