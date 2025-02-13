import sys
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
import os

app = Flask(__name__)
limiter = Limiter(app)

hashed_password = generate_password_hash("1234")
# pensei em usar o flasklimter para limitar as tentativas de login

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Limita a tentativa de login
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and check_password_hash(hashed_password, password):
        return "Acesso concedido"
    return "Acesso negado", 401

if __name__ == '__main__':
    is_debug = False

    # Verifica o argumento da linha de comando para determinar o modo
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        is_debug = True
        
    app.run(debug=is_debug)  # Se is_debug for True, ativa o modo de debug, senão usa o modo de produção
