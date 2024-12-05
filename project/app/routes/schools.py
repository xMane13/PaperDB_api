from flask import Blueprint, request, jsonify
from ..models import School
from ..schemas import SchoolSchema
from .. import db

school_bp = Blueprint('schools', __name__)

# Ruta para crear una escuela
@school_bp.route('/', methods=['POST'])
def create_school():
    """
    Crea una nueva escuela en la base de datos.
    """
    data = request.json
    new_school = School(
        school_idpk=data['school_idpk'],
        school_name=data['school_name']
    )
    db.session.add(new_school)
    db.session.commit()
    return jsonify({'message': 'School created successfully'}), 201

# Obtener todas las escuelas
@school_bp.route('/', methods=['GET'])
def get_schools():
    schools = School.query.all()
    schema = SchoolSchema(many=True)
    return jsonify(schema.dump(schools))
