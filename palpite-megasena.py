#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, get, post, view, run, app, default_app, static_file
from palpite import palpite

@get('/')
@view('index.html')
def index_get():
    return dict()

@post('/')
@view('index.html')
def index_post():
    gera_palpite = palpite()
    return dict(jogo=gera_palpite)

@get('/favicon.ico')
@get('/favicon.png')
def favicon():
    return static_file('/static/favicon.png', root='.')

@get('/normalize.css')
def normalizecss():
    return static_file('normalize.css', root='static')

@get('/skeleton.css')
def skeletoncss():
    arq = 'skeleton.css'
    return static_file(arq, root='./static')

app = default_app()
app.run(server='gae',debug=True)
