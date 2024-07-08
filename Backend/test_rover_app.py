import unittest
import json
from App import app

class RoverAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.x = None
        self.y = None
        self.facing = None
        self.rover = None  # Initialize rover instance

    def tearDown(self):
        self.x = None
        self.y = None
        self.facing = None
        self.rover = None  # Reset rover instance after each test case

    def test_place_command_success(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'PLACE 0,0,NORTH'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Rover placed successfully', data['message'])
            self.rover = None  # Reset rover state after each request

    def test_place_command_invalid_format(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'PLACE 0,0'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_place_command_out_of_bounds(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'PLACE 5,5,NORTH'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_place_command_invalid_direction(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'PLACE 0,0,NORTHWEST'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_move_command_success(self):
        with self.app:
            self.app.post('/command', json={'command': 'PLACE 0,0,NORTH'})
            response = self.app.post('/command', json={'command': 'MOVE'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Rover moved successfully', data['message'])
            self.rover = None  # Reset rover state after each request

    def test_move_command_not_placed(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'MOVE'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_move_command_fall_off_table(self):
        with self.app:
            self.app.post('/command', json={'command': 'PLACE 4,4,EAST'})
            response = self.app.post('/command', json={'command': 'MOVE'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_left_command_success(self):
        with self.app:
            self.app.post('/command', json={'command': 'PLACE 0,0,NORTH'})
            response = self.app.post('/command', json={'command': 'LEFT'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Rover turned LEFT successfully', data['message'])
            self.rover = None  # Reset rover state after each request

    def test_right_command_success(self):
        with self.app:
            self.app.post('/command', json={'command': 'PLACE 0,0,NORTH'})
            response = self.app.post('/command', json={'command': 'RIGHT'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Rover turned RIGHT successfully', data['message'])
            self.rover = None  # Reset rover state after each request

    def test_report_command_success(self):
        with self.app:
            self.app.post('/command', json={'command': 'PLACE 1,2,EAST'})
            response = self.app.post('/command', json={'command': 'REPORT'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['x'], 1)
            self.assertEqual(data['y'], 2)
            self.assertEqual(data['facing'], 'EAST')
            self.rover = None  # Reset rover state after each request

if __name__ == '__main__':
    unittest.main()

