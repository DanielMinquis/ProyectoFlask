from flask import Blueprint

taskRoute = Blueprint('task', __name__, url_prefix='/task')

#Creacion de rutas en el modulo rutas
@taskRoute.route('/')
def index():
    return 'Index'

@taskRoute.route('/<int:id>')
def show(id:int):       #va a devolver un registro específico de acuerdo al ID 
    return 'Show ' +str(id) #CRUD CREATE READ UPDATE DELETE

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'update '+str(id)