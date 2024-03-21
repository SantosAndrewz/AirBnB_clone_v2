#!/usr/bin/python3
"""Unittests for Place Class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Creating class for tests for Place"""

    def __init__(self, *args, **kwargs):
        """initializing the test instances"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Testing for the city_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Testing for the user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Testing for the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Testing for the description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Testing for room numbers """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Testing for bathroom numbers """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Testing for maximum guuests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Testting for the price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Testing for latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Testing for latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Testing for amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
