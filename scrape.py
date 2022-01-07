import requests

token = input("Token: ") #discord token
channel = input("Channel ID: ")

option = input("[1] Images\n[2]Gifs\n[3]Videos\n[4] All\n\n-->\t")

headers = {
'Authorization': f'{token}'
}

r = requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?limit=100", headers=headers)

data = r.json()

try:
	keys = data[:]
except Exception:
	print("Wrong ChannelID or Discord Token. (or discord api related errors)")
	exit()

def images(data):
	for key in keys:
		values = key['attachments']
		for value in values:
			print(value['url'], file=open("output.txt", "a")) #outputs to output.txt. If u plan to use this again rename the old output.txt or move it to another folder.

def gifs(data):
	for gif in keys:
		gifs = gif['content']
		if ".gif" in gifs: 
			print(gifs, file=open("output.txt", "a"))

def videos(data):
	for video in keys:
		videos = video['content']
		if ".mp4" in videos: 
			print(videos, file=open("output.txt", "a"))

def options(option):
	if option == '1':
		images(data)
	elif option == '2':
		gifs(data)
	elif option == '3':
		videos(data)
	elif option == '4':
		images(data)
		gifs(data)
		videos(data)
	else:
		exit()

options(option)
