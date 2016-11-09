from django.test import TestCase

class DummyTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        self.assertTrue(True)