from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route('/crucigrama')

def getCrucigrama():
    print("Crucigrama")
    os.system('echo "Crucigrama" | faas-cli invoke crucigrama')
    print("\n")
    return  "Success"
    

@app.route('/tiempo')
def getTiempo():
    print("Tiempo")
    os.system('echo "tiempo" | faas-cli invoke tiempo')
    print("\n")
    return "Success"


@app.route('/uf')    
def getUF():
    print("UF")
    os.system('echo "uf" | faas-cli invoke uf')
    print("\n")
    return "Success"


@app.route('/dolar')    
def getDolar():
    print("Dolar")
    os.system('echo "dolar" | faas-cli invoke dolar')
    print("\n")
    return "Success"

if __name__ == '__main__':
    app.run(debug = True,port=4000)