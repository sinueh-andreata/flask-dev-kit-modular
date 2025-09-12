from flask import Flask
from .config import app, db

# importação das tabelas do banco de dados
from src.backend.core.config import app, db

# importação das rotas/endpoints/APIs
from src.backend.modulos.usuarios.usuario import *
from src.backend.modulos.admin.admin import *
from src.backend.modulos.rotas_html.rotas_html import *