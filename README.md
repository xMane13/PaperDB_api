# PaperDB_api
# Sistema de Administración de Publicaciones Académicas

Este proyecto es una API diseñada para gestionar publicaciones académicas, autores, instituciones educativas (escuelas), revistas académicas y relaciones entre estas entidades. Permite registrar, visualizar y gestionar la información relacionada con estos datos.

---

## Características

- Gestión de Autores: Registro, visualización, edición y eliminación de autores.
- Gestión de Papers: Creación de papers asociados a autores y categorizados por revistas e instituciones.
- Gestión de Escuelas: Registro de instituciones educativas relacionadas con publicaciones académicas.
- Gestión de Revistas Académicas: Administración de revistas donde se publican los papers.
- Relaciones Complejas: Soporte para relaciones entre autores, papers, escuelas y revistas.

---

## Estructura de la Base de Datos

La base de datos está compuesta por las siguientes tablas principales:

- Authors: Información básica de los autores.
- Papers: Información sobre los papers creados.
- Schools: Instituciones educativas relacionadas con los autores o los papers.
- Journals: Revistas académicas donde se publican los papers.
- Author_Paper: Relación entre autores y papers.

---

## Esquema de Base de Datos

### Tabla: Authors

Campo            | Tipo         | Restricciones
----------------- | ------------ | --------------
Author_ID         | INT          | PRIMARY KEY
Author_Name       | VARCHAR(20)  | NOT NULL
Author_Last_Name  | VARCHAR(20)  | NOT NULL
Author_Email      | VARCHAR(50)  | NOT NULL
Author_Affiliation| VARCHAR(50)  | NOT NULL

---

### Tabla: Papers

Campo            | Tipo         | Restricciones
----------------- | ------------ | --------------
DOI              | VARCHAR(20)  | PRIMARY KEY
Paper_Title      | VARCHAR(30)  | NOT NULL
Paper_Abstract   | VARCHAR(500) | NOT NULL
Paper_Keywords   | VARCHAR(30)  | NOT NULL
Submission_Date  | VARCHAR(20)  | NOT NULL
Status           | VARCHAR(10)  | NOT NULL
School_IDPK      | VARCHAR(10)  | FOREIGN KEY (School.School_IDPK)
Journal_IDPK     | VARCHAR(20)  | FOREIGN KEY (Journal.Journal_IDPK)

---

### Tabla: Schools

Campo       | Tipo         | Restricciones
------------| ------------ | --------------
School_IDPK | VARCHAR(10)  | PRIMARY KEY
School_Name | VARCHAR(100) | NOT NULL

---

### Tabla: Journals

Campo            | Tipo         | Restricciones
----------------- | ------------ | --------------
Journal_IDPK     | VARCHAR(20)  | PRIMARY KEY
Publisher_Name   | VARCHAR(20)  | NOT NULL
Journal_Name     | VARCHAR(20)  | NOT NULL
Presentation_Type| INT          | NOT NULL

---

### Tabla: Author_Paper

Campo            | Tipo         | Restricciones
----------------- | ------------ | --------------
DOI              | VARCHAR(20)  | FOREIGN KEY (Papers.DOI), PRIMARY KEY
Author_ID        | INT          | FOREIGN KEY (Authors.Author_ID), PRIMARY KEY

---

## Instalación

1. Clonar el repositorio:
   git clone https://github.com/xMane13/PaperDB_api.git
   cd academic-publications-api

3. Crear y activar un entorno virtual:
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows

4. Instalar las dependencias:
   pip install -r requirements.txt

5. Configurar la base de datos:
   - Configura las credenciales de tu base de datos en el archivo .env o en las variables de entorno.

6. Realizar migraciones de la base de datos (si usas Flask-Migrate):
   flask db upgrade

7. Ejecutar la aplicación:
   flask run

---

## Uso

Una vez que la aplicación esté en ejecución, puedes interactuar con la API utilizando herramientas como Postman o cURL.

---

## Endpoints Principales

### Autores

- GET /authors: Obtiene la lista de autores.
- POST /authors: Crea un nuevo autor.
- GET /authors/<id>: Obtiene un autor específico.
- PUT /authors/<id>: Actualiza un autor.
- DELETE /authors/<id>: Elimina un autor.

### Papers

- GET /papers: Obtiene todos los papers.
- POST /papers: Crea un nuevo paper.
- GET /papers/<id>: Obtiene un paper específico.
- PUT /papers/<id>: Actualiza un paper.
- DELETE /papers/<id>: Elimina un paper.

### Escuelas

- GET /schools: Obtiene todas las escuelas.
- POST /schools: Crea una nueva escuela.
- GET /schools/<id>: Obtiene una escuela específica.
- PUT /schools/<id>: Actualiza una escuela.
- DELETE /schools/<id>: Elimina una escuela.

### Revistas

- GET /journals: Obtiene todas las revistas.
- POST /journals: Crea una nueva revista.
- GET /journals/<id>: Obtiene una revista específica.
- PUT /journals/<id>: Actualiza una revista.
- DELETE /journals/<id>: Elimina una revista.

---

## Ejemplo de Configuración .env

FLASK_APP=run.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=mysql+pymysql://usuario:contraseña@localhost:3306/nombre_base_datos
SECRET_KEY=clave_secreta

---

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad:
   git checkout -b mi-nueva-funcionalidad
3. Realiza tus cambios y haz un commit:
   git commit -m "Añadida nueva funcionalidad"
4. Sube los cambios a tu rama:
   git push origin mi-nueva-funcionalidad
5. Crea un Pull Request en el repositorio principal.

---

## Contacto

- Autor: [Manuel Munoz](https://github.com/xMane13)
- Correo: manuel.munoz@yachaytech.edu.ec
