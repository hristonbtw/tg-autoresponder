import asyncio
import json
from telethon import TelegramClient
from telethon import events
import os
import configparser
import time

cfg = configparser.ConfigParser()
cfg.read("config.ini", encoding="utf-8")

api_id =  #здесь ваш api_id
api_hash = '' #здесь ваш api_hash

time_sleep = cfg['Settings']['Sleep']

client = TelegramClient('account', api_id, api_hash)
client.start()

@client.on(events.NewMessage())
async def normal_handler(message):
	with open(f'./voc/voc.json', 'r', encoding='utf-8') as file:
		voc = json.load(file)
	try:
		time.sleep(int(time_sleep))
		await client.get_dialogs()
		await client.send_message(message.from_id.user_id, voc[message.text.lower()])
	except:
		time.sleep(int(time_sleep))
		await client.get_dialogs()
		await client.send_message(message.from_id.user_id, voc['not_found'])

client.run_until_disconnected()