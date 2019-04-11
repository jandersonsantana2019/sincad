import pyodbc
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('formulario.html')

@app.route('/resultado',methods = ['POST', 'GET'])
def resultado():
   if request.method == 'POST':
      #result = request.form
      name=request.form['Name']
      email=request.form['Email']
      nasc=request.form['nasc']
      idade=request.form['idade']
      graduacao=request.form['grad']
      genero=request.form['genero']
       
      server = 'DESKTOP-NS1AQM9\SQLEXPRESS'
      database = 'Projetoflaskcerto' 
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database +';trusted_connection=yes;')
      cursor = cnxn.cursor()
      sql = "SELECT email FROM alunofaisp2019 where Username ='" + name + "' and email = '" + email + "'"
      cursor.execute(sql)
      

      row = cursor.fetchone()
      if row != None:
         return "Usuario existente na base"
      else:
        sql1 = "insert into alunofaisp2019(username,email,nasc,idade,grad,genero) Values ('{}','{}','{}','{}','{}','{}')".format(name,email,nasc,idade,graduacao,genero)
        cursor.execute(sql1)
        cursor.commit()
        cursor.close()
        return "Usuario adicionado"



      #return render_template("resultado.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
