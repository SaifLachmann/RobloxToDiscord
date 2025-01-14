from fastapi import FastAPI
import os
import requests
Discord_Webhook = os.environ.get('Discord_Webhook')
Website_Api = os.environ.get('Website_Api')

def SendMessageToDiscord(Msg):
    Message = {
        "content": = "",
        "username" = "Nix Cafe Activity Logger",
        "embeds" = {
            "description" = Msg,
            "type"= "rich",
	    "color"= tonumber(0x3bfff8),
    }
	    
    requests.post(Discord_Webhook, data=Message)

app = FastAPI()

@app.get("/discord")
async def read_items(Key: str, Message: str):
    if Key == Website_Api:
      SendMessageToDiscord(Message)
      return "Success"
    else:
        return "Incorrect key"
