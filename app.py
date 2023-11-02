import os
import tempfile
from flask import Flask, request, redirect, render_template, url_for
from skimage import io
import base64
from skimage.transform import resize
import numpy as np
import random as rd
from tensorflow.keras.models import load_model
import gdown

# Reemplaza el enlace con el enlace de descarga directa de tu archivo en Google Drive
enlace_google_drive = "https://drive.google.com/uc?id=18WnNN9Qk1oRH2F7d9ojBAsQLcKGiN6ks"
# Especifica el nombre del archivo local
nombre_archivo_local = "modelo_entrenado.h5"

# Realiza la solicitud para descargar el archivo
response = gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)

# Verifica si la descarga fue exitosa (código de estado 200)

model = load_model('modelo_entrenado.h5')

app = Flask(__name__, template_folder="templates/")
palabras = ["Persona", "Hombre", "Mujer","Perro", "Gato","Vaca", "Caballo", "Tigre", "Pasto", "Flor", "Fruta", "Árbol", "Hoja",
          "Raíz", "Flor de Cerezo", "Ciruela", "Sol", "Luna", "Estrella", "Luvia", "Nieve", "Trueno", "Cielo", "Rojo", "Azul",
          "Violeta", "Verde", "Amarillo", "Blanco", "Negro", "Uno", "Dos", "Tres", "Ahora", "Pasado", "Futuro", "Feliz", "Triste",
          "Doloroso", "Padre", "Madre", "Hermano Mayor", "Hermano Menor", "Hermana Mayor", "Hermana menor", "Grande", "Pequeño",
          "Casa", "Dulce", "Delicioso"];
traduccion = {"Persona":["hi","to"], "Hombre": ["o","to","ko"], "Mujer":["o","n","na"],"Perro":["i","nu"], "Gato":["ne","ko"],
             "Vaca":["u", "shi"], "Caballo":["u","ma"], "Tigre":["to","ra"], "Pasto":["ku","sa"], "Flor":["ha","na"], 
             "Fruta":["mi"], "Árbol":["ki"], "Hoja":["ha"],"Raíz":["ne"], "Flor de Cerezo":["sa","ku","ra"], "Ciruela":["u","me"], 
             "Sol": ["ta","i","yo","u"], "Luna":["tsu","ki"], "Estrella":["ho","shi"], "Luvia":["a","me"], "Nieve":["yu","ki"], 
             "Trueno":["ka","mi","na","ri"], "Cielo":["so","ra"], "Rojo":["a","ka"], "Azul":["a","o"], "Violeta":["mu","ra","sa","ki"],
             "Verde": ["mi","do","ri"], "Amarillo":["ki","i","ro"], "Blanco":["shi","ro"], "Negro":["ku","ro"], "Uno":["i","chi"], 
             "Dos":["ni"], "Tres":["sa","n"], "Ahora":["i","ma"], "Pasado":["ka","ko"], "Futuro":["mi","ra","i"], "Feliz":["u","re","shi","i"],
             "Triste":["ka","na","shi","i"], "Doloroso":["i","ta","i"], "Padre":["chi","chi"], "Madre":["ha","ha"], 
             "Hermano Mayor":["a","ni"], "Hermano Menor":["o","to","u","to"], "Hermana Mayor":["a","ne"], "Hermana menor":["i","mo","u","to"], 
             "Grande":["o","o","ki","i"], "Pequeño":["chi","i","sa","i"], "Casa":["i","e"], "Dulce":["a","ma","i"], 
             "Delicioso":["u","ma","i"]}

alpha_mapping = dict()
alpha_mapping[0] = "a"
alpha_mapping[1] = "i"
alpha_mapping[2] = "u"
alpha_mapping[3] = "e"
alpha_mapping[4] = "o"
alpha_mapping[5] = "ka"
alpha_mapping[6] = "ki"
alpha_mapping[7] = "ku"
alpha_mapping[8] = "ke"
alpha_mapping[9] = "ko"
alpha_mapping[10] = "sa"
alpha_mapping[11] = "shi"
alpha_mapping[12] = "su"
alpha_mapping[13] = "se"
alpha_mapping[14] = "so"
alpha_mapping[15] = "ta"
alpha_mapping[16] = "chi"
alpha_mapping[17] = "tsu"
alpha_mapping[18] = "te"
alpha_mapping[19] = "to"
alpha_mapping[20] = "na"
alpha_mapping[21] = "ni"
alpha_mapping[22] = "nu"
alpha_mapping[23] = "ne"
alpha_mapping[24] = "no"
alpha_mapping[25] = "ha"
alpha_mapping[26] = "hi"
alpha_mapping[27] = "fu"
alpha_mapping[28] = "he"
alpha_mapping[29] = "ho"
alpha_mapping[30] = "ma"
alpha_mapping[31] = "mi"
alpha_mapping[32] = "mu"
alpha_mapping[33] = "me"
alpha_mapping[34] = "mo"
alpha_mapping[35] = "ya"
alpha_mapping[36] = "yu"
alpha_mapping[37] = "yo"
alpha_mapping[38] = "ra"
alpha_mapping[39] = "ri"
alpha_mapping[40] = "ru"
alpha_mapping[41] = "re"
alpha_mapping[42] = "ro"
alpha_mapping[43] = "wa"
alpha_mapping[44] = "wi"
alpha_mapping[45] = "we"
alpha_mapping[46] = "wo"
alpha_mapping[47] = "n"

@app.route("/")
def main():
    word = palabras[rd.randint(0,49)]
    size = len(traduccion[word])
    return render_template("index.html", word=word,len=size)
@app.route("/help")
def help():
    return render_template("help.html")

@app.route('/predict', methods=['POST'])
def predict():
    imagenes = []
    indices = []
    l = request.form.get('size')
    word = request.form.get('word')

    for i in range(int(l)):
        img_data = request.form.get('myImage_'+str(i)).replace("data:image/png;base64,", "")
        imagenes.append(img_data)
        with tempfile.NamedTemporaryFile(delete=False, mode="w+b", suffix='.png', dir=str('predicciones')) as fh:
            fh.write(base64.b64decode(img_data))
            tmp_file_path = fh.name
        imagen = io.imread(tmp_file_path)
        imagen = imagen[:, :, 3]
        size = (28, 28)
        image = imagen / 255.0
        im = resize(image, size)
        im = im[:, :, np.newaxis]
        im = im.reshape(1, *im.shape)
        salida = model.predict(im)[0]
        os.remove(tmp_file_path)
        nums = salida*100
        numeros_formateados = [f'{numero:.2f}' for numero in nums]
        maximum = max(numeros_formateados)
        indice = numeros_formateados.index(maximum)
        indices.append(indice)  
    return redirect(url_for('predicciones', index=indices, img_data=imagenes, word=word))

    print("Error occurred")
    return redirect("/", code=302)

@app.route('/predicciones')
def predicciones():
    nums = request.args.getlist('index')
    img_data = request.args.getlist('img_data')
    word = request.args.get('word')
    silabasEsperadas = traduccion[word]
    silabasEscritas = [alpha_mapping[int(n)] for n in nums]
    size = len(silabasEsperadas)
    if img_data is not None:
        return render_template('Prediccion.html', SE=silabasEsperadas, SI = silabasEscritas,l = size,word=word)
    else:
        return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
