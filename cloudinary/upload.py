import cloudinary
import cloudinary.uploader
import cloudinary.api

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings()

cloudinary.config(
	cloud_name = 'dz9yrk0yr',
	api_key = '197636939128215',
	api_secret = '48GMRflrCHUfdXi4z5KMous4cxU', 
	secure = 'true'
)


def upload_image(filename):
	d = cloudinary.uploader.upload(filename)
	url = d['secure_url']
	print url

upload_image('lul.jpg')