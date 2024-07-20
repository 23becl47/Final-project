
import unittest
from app import app
from models import db_session

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db_session.query(Employee).delete()
        db_session.commit()

    def test_create_employee(self):
        data = {'name': 'John Doe', 'age': 30, 'department': 'Sales'}
        response = self.app.post('/employees', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'Employee created successfully'})

    def test_get_employees(self):
        employee1 = Employee(name='John Doe', age=30, department='Sales')
        employee2 = Employee(name='Jane Doe', age=25, department='Marketing')
        db_session.add_all([employee1, employee2])
        db_session.commit()
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_employee(self):
        employee = Employee(name='John Doe', age=30, department='Sales')
        db_session.add(employee)
        db_session.commit()
        response = self.app.get('/employees/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1, 'name': 'John Doe', 'age': 30, 'department': 'Sales'})

    def test_update_employee(self):
        employee = Employee(name='John Doe', age=30, department='Sales')
        db_session.add(employee)
        db_session.commit()
        data = {'name': 'Jane Doe', 'age': 25, 'department': 'Marketing'}
        response = self.app.put('/employees/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Employee updated successfully'})

    def test_delete_employee(self):
        employee = Employee(name='John Doe', age=30, department='Sales')
        db_session.add(employee)
        db_session.commit()
        response = self.app.delete('/employees/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Employee deleted successfully'})

if __name__ == '__main__':
    unittest.main()