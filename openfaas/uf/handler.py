import http.client

conn = http.client.HTTPSConnection("mindicador.cl")
payload = ''
headers = {}
conn.request("GET", "/api/uf", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return data.decode("utf-8")
