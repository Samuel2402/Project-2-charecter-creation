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
        for _ in range(20):
            response = self.client.get(url_for('get_race'))
            self.assertIn(response.data.decode('utf-8'), ["Human", "Mage", "Ranger"])

    