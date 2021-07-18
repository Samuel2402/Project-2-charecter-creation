from flask import Flask
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class Testhome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://race_api:5001/get_race', text='Human')
            mocker.get('http://class_api:5002/get_class', text='Warrior')
            mocker.post('http://stats_api:5003/get_blessing', text='Recieve the blessing of Ares: +2 base Attack')
            mocker.post('http://stats_api:5003/get_stats', text="Attack:   6   |   Intelligence:  4   |   Dexterity: + 4")
            mocker.get('http://stats_api:5003/get_points', text="6")  
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Human', response.data)
            self.assertIn(b'Warrior', response.data)
            self.assertIn(b'Character Blessing: Recieve the blessing of Ares: +2 base Attack', response.data)
            self.assertIn(b"Attack:   6   |   Intelligence:  4   |   Dexterity: + 4", response.data)
            self.assertIn(b"6", response.data)
            
    # def test_read_home(self):
    #     response = self.client.get(url_for('home'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Character Generator', response.data)
