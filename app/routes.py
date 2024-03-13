from . import app, db
from .models import Medico
from .models import Paciente
from .models import Consultorio
from .models import Cita
from flask import render_template, request, flash, redirect

#crear ruta para ver los medicos
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes )

@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , citas=citas)

#crear una ruta de medico por id utilazando (get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    #return "id del medico:" + str(id)
    #traer el medico por id utilizando la entidad Medico
    medico = Medico.query.get(id)
    #y meterlo a una lista
    return render_template("medico.html",
                            med = medico )

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html",
                            pac = paciente )

@app.route("/consultorios/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html",
                            con = consultorio)

@app.route("/cita/<int:id>")
def get_cita_by_id(id):
    cita = Cita.query.get(id)
    return render_template("cita.html",
                            cita = cita)



#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST" ] )
def create_medico():
    #mostra el formulario: METODO GET
    if( request.method == "GET" ):
        #EL SUSARIO INGRESO CON EL NAVEGADOR https://localhost.....
        especialidades = [
            "cardiologia",
            "psicologia",
            "dermatologia"
        ]
        return render_template ("medico_forms.html", 
                            especialidades = especialidades)
        #cuado el usuario presiona el boton guardar
        #los datos del formulario
    elif(request.method == "POST"):
        #CUANDO SE PRESIONA GUARDAR 
        #CREAR OBJETO MEDICO
        new_medico = Medico(nombre = request.form["nombre"],
                            apellido = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"]
                            )
        
        db.session.add(new_medico)
        db.session.commit()
        flash("Medico registrado correctamente")
        return redirect("/medicos")
    
@app.route("/medicos/update/<int:id>", methods=["POST","GET"])
def update_medico(id):
    especialidades = ["cardiologia", "psicologia", "dermatologia"]
    medico_update = Medico.query.get(id)
    if(request.method =="GET"):
        return render_template("medico_update.html" , medico_update = medico_update, especialidades = especialidades)
    elif(request.method == "POST"):
        #ACTUALIZAR EL MEDICO EN DATOS DE FORMA
        medico_update.nombre = request.form["nombre"]
        medico_update.apellido = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["ti"]
        medico_update.numero_identificacion = request.form["ni"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]
        db.session.commit()
        return "medico actualizado"
    
@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")

#NUEVA RUTA PARA PACIENTES
@app.route("/pacientes/create" , methods = [ "GET" , "POST"] )
def create_paciente():
    if( request.method == "GET" ):
        tipo_de_sangres = [
            "A+",
            "A-",
            "B+",
            "B-",
            "O+",
            "O-",
            "AB+",
            "AB-"
        ]
        return render_template("pacientes_form.html",
                            tipo_de_sangres = tipo_de_sangres)
    
    elif(request.method == "POST"):
        new_paciente = Paciente(nombre = request.form["nombre"],
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"],
                            altura = request.form["al"],
                            tipo_de_sangres = request.form["rh"]
                            )
        db.session.add(new_paciente)
        db.session.commit()
        return "paciente registrado"
    
#crear ruta para crear nuevo consultorio
@app.route("/consultorios/create" , methods = [ "GET" , "POST"] )
def create_consultorio():
    if( request.method == "GET" ):
        numero = [
            "410",
            "411",
            "413",
            "414",
            "415",
            "320",
            "321",
            "322",
            "323",
            "324"
            
        ]
        return render_template("consultorios_form.html",
                            numero = numero)
    
    elif(request.method == "POST"):
        new_consultorio = Consultorio( numero = request.form["nu"]
                            )
        db.session.add(new_consultorio)
        db.session.commit()
        return "consultorio registrado"

@app.route("/citas/create" , methods = [ "GET" , "POST"] )
def create_cita():
    if(request.method == "GET"):
        pacientes = Paciente.query.all()
        return render_template("citas_form.html" , pacientes=pacientes)
    elif(request.method == "GET"):
        medicos = Medico.query.all()
        return render_template("citas_form.html" , medicos=medicos)
    elif(request.method == "GET"):
        consultorios = Consultorio.query.all()
        return render_template("citas_form.html" , consultorios=consultorios)
    elif(request.method == "POST"):
        new_cita = Cita(fecha = request.form["fecha"],
                        paciente = request.form["pac"],
                        medico = request.form["med"],
                        consultorio = request.form["con"],
                        valor = request.form["val"]
                        )
        db.session.add(new_cita)
        db.session.commit()
        return "cita registrada"
        
        
                            



