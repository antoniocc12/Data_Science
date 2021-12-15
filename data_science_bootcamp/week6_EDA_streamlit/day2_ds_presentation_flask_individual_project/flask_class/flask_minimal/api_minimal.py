from flask import Flask, flash, request, render_template, redirect, url_for
import pandas as pd
import os
import json

UPLOAD_FOLDER = os.sep + "static" + os.sep #estamos apuntando a la carpeta static
#todo esto es obligatorio, para crear un flask debo darle el atributo name
app = Flask(__name__) #Flask es una clase cuyo primer atributo obligatorio seria name.name tiene el nombre del fichero en estee caso o es sinimo de poner _main_
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #los archivos que se vayan a utilizar para subir, es decir la clave va a apuntar a la carpeta static o donde se van a guardar las cosas 
app.secret_key = 'hellohello' #un atributo para interactuar con la API

options = {"Genre_list":["hola", "adios"],
"Platform_list":[1,2,3,4,5,6],
"Publisher_list":['Clara', 'Borja', 'Gabriel']}
#en el archivo UPLOAD está la tipica ruta de una pagina web que se puede usar si lo necesitamos
@app.route("/") #esta es la funcion que se va a llamar por defecto, o la primera que se va a mostrar cuando ponga la direccion de la API
def home():
    return render_template("upload.html", 
                           Genre_list = options["Genre_list"],
                           Platform_list= options["Platform_list"], 
                           Publisher_list= options["Publisher_list"])
  #aqui se recogen todos los valores que ha metido el usuario  
@app.route("/upload_form", methods = ['POST', 'GET'])# cuando yo le doyo enviar al formulario, eso apunta a esta función. El POST es elde enviar
def upload_form():
    if request.method == 'POST':
        genre_res = request.form['Genre']
        platform_res= request.form['Platform']
        publisher_res = request.form['Publisher']
        all_returned = str(genre_res) + str(platform_res) + str(publisher_res)
        return json.dumps({"genre": genre_res, #esta devolviendo un diccionario transformado a json
                            "platform": platform_res,
                            "publisher": publisher_res,
                            "all_returned": all_returned})

if __name__ == '__main__':
    # host='127.0.0.1' --> No permite recibir llamadas desde el exterior
    # host='0.0.0.0' --> Permite recibir llamadas desde el exterior
    # si 0.0.0.0 no funciona externamente desde la IP privada de tu PC
    # es que tu ordenador o del dispositivo desde el que se accede 
    # tiene bloqueada la conexión (antivirus / firewall)
    app.run(host='0.0.0.0',port=os.getenv("PORT", 1991), debug=True)

    # se pone 0000 es que hace que nuestro ordenador sea publico