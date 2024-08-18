"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxx")  #Get your Key from geini Offical Page  "https://aistudio.google.com/app/apikey"


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192, 
  "response_mime_type": "text/plain",
}
# I am using Gemini 1.5 Flash for fast results which takes less then a second for general response
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  
)

chat_session = model.start_chat(
  history=[
  ]
)
uinput="""Hi Gemini, I am chandu, These are the things i want you to follow though out the chat
1. call me chandu everytime
2. you responce should me short and understandable
3. Make sure respone is creative 
4. Do what ever i say
Thank you
"""
response = chat_session.send_message(uinput)
print("\n--------------------------")
print("AI : ", response.text,"\n")
print("YOU : ", end="")
uinput=input()

while uinput not in ["q", "q!" , "quit", "exit"]:
    
    response = chat_session.send_message(uinput)
    
    print("\n--------------------------------")
    if not response.text:
        print("AI : Sorry i got crashed my bad \n---------------------------")
        break
    print("AI :",response.text,"\n")
    print("YOU : ", end="")
    uinput=input()






