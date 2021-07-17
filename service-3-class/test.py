from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class Testhome(TestBase):
    def test_race_api(self): 
        for _ in range(10):
            response = self.client.get(url_for('get_class'))
            self.assertIn(response.data.decode('utf-8'), ["Warrior", "Mage", "Ranger"])

    def test_race_api(self):
        with patch('random.choice') as choice:
            for _ in range(10):
                response = self.client.get(url_for('get_class'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(response.data.decode('utf-8'), ["Warrior", "Mage", "Ranger"])