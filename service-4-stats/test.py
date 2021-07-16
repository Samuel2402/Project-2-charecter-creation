from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

    def test_return_blessing(self):
        character_class = [("Warrior",'Recieve the blessing of Ares: +2 base Attack'), ("Mage",'Recieve the blessing of Athena: +2 base Intellect'), ("Ranger",'Recieve the blessing of Artemis: +2 base Dexterity')]
        for _class in character_class:
            response = self.client.post(url_for('get_blessing'), data=_class[0])
            self.assertEqual(response.data.decode('utf-8'),  _class[1])
            