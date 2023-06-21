#paquteria de flask
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#la inicializacion del app 
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key='mysecretkey'
MySQL=MySQL(app)
#declaracion o inicializacion de las rutas y le pertenece a http://localhost:5000
@app.route('/')
def index():
        return render_template('index.html')
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['textArtista']
        Vanio=request.form['txtAnio']
       

        #conectar y ejecutar el insert 
        CS= MySQL.connection.cursor()
        CS.execute('insert into Albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        MySQL.connection.commit()
        
    flash ('El albumfue agregado correctamente')
        
    return redirect(url_for('index'))


@app.route('/eliminar')
def eliminar():
    return "Se elimino de la Base de Datos"


#ejecucion del servidor y asignacion del puerto a trabajar
if __name__ == '__main__':
        app.run(port=5000 ,debug= True)