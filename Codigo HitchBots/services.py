CLIENT_ID = "2fc4bd056400cb7"
CLIENT_SECRET = "5815e94d0fdf6fdbd4e48f057e6f380bee28cf8e"
MICROSOFT_KEY = "013753f69550425dadb04f38e5308a0c"

def download_image(url):
	import urllib

	image = open("image.jpg", "wb")
	image.write( urllib.urlopen( url ).read() )
	image.close()

def upload_image():
	from imgurpython import ImgurClient
	
	client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
	# response = client.upload_from_path(path)
	response = client.upload_from_path("nueva_image.jpg")
	return response["link"]

def add_emoji(faces):
	from PIL import Image

	background = Image.open("image.jpg")
	foreground = Image.open("emojis/emoji.png")

	for face in faces:
		foreground_resize = foreground.resize(  (face["width"], face["height"]) )
		background.paste( foreground_resize, (face["left"], face["top"]), foreground_resize)
		# background.paste(foreground,(face["left"], face["top"]), foreground)
	# background.show()
	background.save("nueva_image.jpg")

# API de reconocimiento facial
def get_faces(url):
	import requests
	import json
	
	res = requests.post("https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect",
		params = {"returnFaceId": "true", "returnFaceLandmarks": "false"},
		data =  json.dumps( {"url" : url }  ) ,
		headers = { "Content-Type": "application/json", "Ocp-Apim-Subscription-Key" : MICROSOFT_KEY }
		)

	faces = []
	if res.status_code == 200:
		# return [ face["faceRectangle"] for face in json.loads( res.text ) ]
		for face in json.loads( res.text ):
			faces.append( face["faceRectangle"])

	print faces
	return faces

# Computer Vision api

def create_new_image(url):
	# print create_new_image("https://scontent.xx.fbcdn.net/v/t34.0-12/16128206_215236158939081_1753194069_n.png?_nc_ad=z-m&oh=70f54f930dcb98ec40a780ac7be6d30d&oe=587E768C")
	# url = "https://scontent-ort2-1.xx.fbcdn.net/v/t34.18173-12/30429272_1889611021072054_1497483623_n.png?_nc_cat=0&_nc_ad=z-m&_nc_cid=0&oh=386ac3bf74262a29d2703f2aa3a5e780&oe=5ADC7099"
	download_image(url)
	faces = get_faces(url)
	add_emoji(faces)
	return upload_image()

