from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import models

class UserMethodTests(TestCase):
	def setUp(self):
		self.username = 'usertest'
		self.password = password='passsss'
		self.email = 'test@test.test'
		self.user = User.objects.create_user(self.username, self.email, self.password)
		self.c = Client()

	def test_create_user(self):
		self.assertEqual(self.user.username, 'usertest')
		self.assertEqual(self.user.email, 'test@test.test')

	def test_pass_loggingIn_user(self):
		auth = authenticate(username=self.username, password=self.password)
		login = self.c.login(username=self.username, password=self.password)
		self.assertEqual(login and auth is not None, True)

	def test_fail_loggingIn_user(self):
		username = '__NO_USERNAME_IN_DB__'
		password = '__NO_PASSWORD_IN_DB__'
		resultLoggingIn = self.c.login(username=username, password=password)
		self.assertEqual(resultLoggingIn, False)

	# def test_logout_user(self):
	# 	logout = self.c.logout()
	# 	self.assertEqual(logout, True)