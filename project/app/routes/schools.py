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


# Obtener una escuela específica
@school_bp.route('/<string:school_idpk>', methods=['GET'])
def get_school(school_idpk):
    school = School.query.get(school_idpk)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    return jsonify({
        "school_idpk": school.school_idpk,
        "school_name": school.school_name
    })

# Actualizar una escuela específica
@school_bp.route('/<string:school_idpk>', methods=['PUT'])
def update_school(school_idpk):
    school = School.query.get(school_idpk)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    data = request.json
    school.school_name = data.get('school_name', school.school_name)
    db.session.commit()
    return jsonify({'message': 'School updated successfully'})

# Eliminar una escuela específica
@school_bp.route('/<string:school_idpk>', methods=['DELETE'])
def delete_school(school_idpk):
    school = School.query.get(school_idpk)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    db.session.delete(school)
    db.session.commit()
    return jsonify({'message': 'School deleted successfully'})