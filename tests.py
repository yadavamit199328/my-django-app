import requests
import json

url="http://127.0.0.1:8000/"
end="home"
final=requests.get(url+end)
print(final.json())


