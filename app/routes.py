from . import app, db
from .models import Medico
from .models import Paciente
from .models import Consultorio
from .models import Cita
from flask import render_template, request

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
        #EL SUSARIO INGRESO CON EL NAVEGADOR HTTPLOCALHOST
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
        return "medico registrado"
        
                            



