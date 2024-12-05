from . import ma
from .models import Authors, Papers, AuthorPaper, School, Journal

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Authors
        include_relationships = True
        load_instance = True

from . import ma
from .models import Papers

class PaperSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Papers
        include_relationships = True  # Incluye relaciones definidas en el modelo
        load_instance = False  # Cambiar a False para devolver un diccionario

    journal_idpk = ma.String(required=True)  # Define el campo como requerido
    school_idpk = ma.String(required=True)


class AuthorPaperSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorPaper

class SchoolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = School

class JournalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Journal
