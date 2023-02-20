import requests
from flask import Flask
from New_surver import password
import json
url = "http://localhost:5000/students/jinho"

password = {'jinho': '123123', 'jinwook': '123123', 'jinwoo': '123123'}
site_post_request = requests.post(url, json = password)
print(password)
