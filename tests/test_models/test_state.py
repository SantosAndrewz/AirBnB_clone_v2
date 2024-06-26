#!/usr/bin/python3
"""Unittest module for State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Creating Class for the tests for state"""

    def __init__(self, *args, **kwargs):
        """Initializing the class instances"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Testing for the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
