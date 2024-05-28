import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from control_area import ControlArea

class TestControlArea(unittest.TestCase):

    def setUp(self):
        self.control_area = ControlArea()

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_fire_alarm_with_smoke(self, mock_stdout):
        print("Running test_handle_fire_alarm_with_smoke")
        self.control_area.smoke_detected = True
        self.control_area.handle_fire_alarm("yes", "yes")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Smoke detected", output)
        self.assertIn("System activated", output)
        self.assertIn("Calling emergency services", output)
        print("Finished test_handle_fire_alarm_with_smoke")

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_false_alarm(self, mock_stdout):
        print("Running test_handle_false_alarm")
        self.control_area.smoke_detected = True
        self.control_area.handle_fire_alarm("no", "yes")
        output = mock_stdout.getvalue().strip()
        self.assertIn("False alarm", output)
        self.assertIn("False alarm triggered", output)
        print("Finished test_handle_false_alarm")

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_power_failure(self, mock_stdout):
        print("Running test_handle_power_failure")
        self.control_area.power_failure = True
        self.control_area.handle_power_failure()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Power failure detected", output)
        self.assertIn("Waiting 20 seconds to regain power", output)
        self.assertIn("Calling emergency services", output)
        print("Finished test_handle_power_failure")

    @patch('sys.stdout', new_callable=StringIO)
    def test_reset_system(self, mock_stdout):
        print("Running test_reset_system")
        self.control_area.reset_system()
        output = mock_stdout.getvalue().strip()
        self.assertIn("System reset", output)
        print("Finished test_reset_system")

    @patch('sys.stdout', new_callable=StringIO)
    def test_terminate_system(self, mock_stdout):
        print("Running test_terminate_system")
        self.control_area.terminate_system()
        output = mock_stdout.getvalue().strip()
        self.assertIn("System terminated", output)
        print("Finished test_terminate_system")


if __name__ == '__main__':
    unittest.main()
