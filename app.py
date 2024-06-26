from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    ip = request.host.split(':')[0]  # Obtenir l'adresse IP du serveur
    ip_address = request.remote_addr
    return f"<p>Hello, World! This server is running on IP: {ip} and maybe : {ip_address} </p>"

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)