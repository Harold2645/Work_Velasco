from flask import Flask,redirect,render_template,request
from flaskext.mysql import MySQL
from datetime import datetime
from Deportistas import deportistas

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'trabajo_velasco'
mysql.init_app(app)
misDeportistas = deportistas(mysql)

@app.route('/')
def index():
    resultado = misDeportistas.consultar()
    return render_template('index.html',res=resultado)

@app.route('/agregardeportista')
def agregardeportista():
    return render_template('registrar.html')

@app.route("/guardardeportistas", methods=['POST'])
def guardardeportistas():
    id = request.form['documento']
    nombre = request.form['nombre']
    estatura = request.form['estatura']
    peso = request.form['peso']
    nacimiento = request.form['nacimiento']
    ahora = datetime.now()
    creado = ahora.strftime("%Y%m%d%H%M%S")
    misDeportistas.agregar([id,nombre,estatura,peso,nacimiento,creado])
    operaciones = "Agregado"
    ahora = datetime.now()
    Fecha_o = ahora.strftime("%Y%m%d%H%M%S")
    acc = [id,operaciones,Fecha_o]
    misDeportistas.accion(acc)
    return redirect('/')

@app.route('/borrarardeportista/<documento>')
def borrardeportista(documento):
    misDeportistas.borrar(documento)
    operaciones = "Borrar"
    ahora = datetime.now()
    Fecha_o = ahora.strftime("%Y%m%d%H%M%S")
    acc = [documento,operaciones,Fecha_o]
    misDeportistas.accion(acc)
    return redirect('/')

@app.route('/editardeportista/<documento>')
def editardeportista(documento):
        deportista = misDeportistas.buscar(documento)
        return render_template("editar.html",dep=deportista[0])
    
@app.route('/actualizardeportista',methods=['POST'])
def actualizadeportista():
    documento = request.form['documento']
    nombre = request.form['nombre']
    estatura = request.form['estatura']
    peso = request.form['peso']
    nacimiento = request.form['nacimiento']
    dep = [documento,nombre,estatura,peso,nacimiento]
    misDeportistas.modificar(dep)
    operaciones = "Editar"
    ahora = datetime.now()
    Fecha_o = ahora.strftime("%Y%m%d%H%M%S")
    acc = [documento,operaciones,Fecha_o]
    misDeportistas.accion(acc)
    return redirect("/")



if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=2645)