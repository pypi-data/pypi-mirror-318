from datetime import date
import unittest
import pytest
import enerplex as ep
import dotenv
from tests import *
from pathlib import Path
import os 
dotenv.load_dotenv()

class TestAuth(unittest.TestCase):

    def test_envs(self):
        env_example = Path(".env.example")
        with open(env_example, "r") as e: 
            keys = [line.split("=")[0] for line in e.readlines()]
            keys = [key for key in keys if key != "\n"]

        for key in keys:
            self.assertIsNotNone(os.environ.get(key), f"{key}={os.environ.get(key)}")
            

    def test_auth_token(self):
        
        token = ep.api._get_auth_token()

        self.assertEqual(token.split(" ")[0], "Bearer")
        self.assertIsNotNone(token.split(" ")[1])