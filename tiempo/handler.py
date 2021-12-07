import http.client

conn = http.client.HTTPSConnection("api.openweathermap.org")
payload = ''
headers = {}
conn.request("GET", "/data/2.5/weather?q=Santiago&appid=77912a62f0324787f05157dfac0cde3c&units=metric", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))



def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return data.decode("utf-8")
