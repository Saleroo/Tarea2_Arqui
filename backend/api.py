from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/crucigrama')

def getCrucigrama():
    url = "https://stackoverflow.com/questions/55448792/api-return-link-instead-of-name"
    return  "Se viene su 7 lokooooooooo"


@app.route('/tiempo')
def getTiempo():
    print("HOla")
    return "Success"


@app.route('/clima')    
def getClima():
    return 

if __name__ == '__main__':
    app.run(debug = True,port=4000)