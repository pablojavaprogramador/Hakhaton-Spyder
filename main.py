from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.post("/analisis-pyme")
def execute_analisis_pyme_spider():
    os.system('python go_spider_pyme.py')
    return {"Status": "El Spyder PYME ha sido lanzando"}


@app.post("/analisis-pyme-inegi")
def execute_analisis_pyme_inegi_spider():
    os.system('python go_spider_inegi.py')
    return {"Status": "Corriendo Analisis de la pyme en datos publicos de inegi"}

@app.post("/analisis-pyme-likendin")
def execute_analisis_pyme_likendin_spider():
    os.system('python go_spider_linkendin.py')
    return {"Status": "Corriendo Analisis de la pyme en datos publicos de linkendin "}

@app.post("/analisis-pyme-googlemaps")
def execute_googlemaps_spider():
    os.system('python go_spider_googlemaps.py')
    return {"Status": "Corriendo Analisis de la pyme en datos publicos de google maps "}

@app.post("/analisis-pyme-siemempresa")
def execute_infobae_spider():
    os.system('go_spider_siemempresa.py')
    return {"Status": "Corriendo Analisis de la pyme en datos publicos de siem empresas"}

