import requests

datas = [20, 10, 65, 30, 20, 10, 80]

for data in datas:
    response = requests.get("http://localhost:8000/signal?data=" + str(data))
    print(response)