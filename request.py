import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SepalLengthCm':5.1,'SepalWidthCm':2.8,'PetalLengthCm':1.6,'PetalWidthCmm':0.3})

print(r.json())
