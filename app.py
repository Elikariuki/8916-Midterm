from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

# Define Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "grade": self.grade, "email": self.email}

# Create tables within app context
with app.app_context():
    db.create_all()

# CRUD operations for Student
class StudentList(Resource):
    def get(self):
        students = Student.query.all()
        return jsonify([student.to_dict() for student in students])

    def post(self):
        data = request.get_json()
        new_student = Student(
            name=data['name'],
            grade=data['grade'],
            email=data['email']
        )
        db.session.add(new_student)
        db.session.commit()
        return jsonify(new_student.to_dict()), 201

class StudentResource(Resource):
    def get(self, id):
        student = Student.query.get_or_404(id)
        return jsonify(student.to_dict())

    def put(self, id):
        student = Student.query.get_or_404(id)
        data = request.get_json()
        student.name = data['name']
        student.grade = data['grade']
        student.email = data['email']
        db.session.commit()
        return jsonify(student.to_dict())

    def delete(self, id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted"})

# API route definitions
api.add_resource(StudentList, '/students')
api.add_resource(StudentResource, '/students/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
