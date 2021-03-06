from urllib import response
from flask import Flask

import unittest

from routes import signup_post

class TestSignin(unittest.TestCase) : 
    """
    doc string
    """
    def setUp(self):
        """
        doc string
        """
        self.app = signup_post()
        self.appctx = self.app.app_context()
        self.appctx.push()
    
    def tearDown(self):
        """
        doc string
        """
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        """
        doc string
        """
        assert self.app is not None
        assert signup_post == self.app

    def test_home_page_redirect(self):
        """
        doc string
        """
        response = self.client.get('/signup', follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/login'

    def test_resgistration_form(self):
        """
        doc string
        """
        response = self.client.get('/signup')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="username"' in html
        assert 'name="email"' in html
        assert 'name="password"' in html
        assert 'name="fullname"' in html
