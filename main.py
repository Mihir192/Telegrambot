import requests
import pandas as pd

url = 'https://github.com/Mihir192/Hackerranks_code/releases/download/Telegram/mj1.tsv'

df = pd.read_csv(url, sep="\t")

base_url = "https://api.telegram.org/bot5420118404:AAHW_qjUMNLMxbcB0FKwjSXgDVFD7sjFAR0"



def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  print(data)

  for result in data["result"]:
    send_msg(result)
  
  if data["result"]:
    return data["result"][-1]["update_id"] + 1



def auto_answer(message):
  answer = df.loc[df['Question'].str.lower() == message.lower()]  

  if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer
  else:
      return "Sorry, I could not understand you !!! I am still learning and try to get better in answering."



def send_msg(message):
  text = message["message"]["text"]
  message_id = message["message"]["message_id"]
  answer = auto_answer(text)

  parameters = {
      "chat_id" : "-1001579801607",
      "text" : answer,
      "reply_to_message_id" : message_id
  }

  resp = requests.get(base_url + "/sendMessage", data = parameters)
  print(resp.text)

offset = 0

while True:  
  offset = read_msg(offset)


