from src.backend.core.config import app, db
from src.backend.shared.login import login_usuario
from flask import render_template, jsonify

@app.route('/')
def tela_login():
    return render_template('login.html')