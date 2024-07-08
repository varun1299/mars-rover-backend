import unittest
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

    def test_report_command_not_placed(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'REPORT'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_invalid_command(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'INVALID_COMMAND'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_missing_command(self):
        with self.app:
            response = self.app.post('/command', json={})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request
    
    def test_right_command_not_placed(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'RIGHT'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

    def test_left_command_not_placed(self):
        with self.app:
            response = self.app.post('/command', json={'command': 'LEFT'})
            self.assertEqual(response.status_code, 400)
            self.rover = None  # Reset rover state after each request

if __name__ == '__main__':
    unittest.main()

