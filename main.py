#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
import time
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign_out</a>)' %
                (user.nickname(), users.create_logout_url('/logout')))
            entry = jinja_environment.get_template("templates/homepage.html")
            self.response.write(entry.render(self.request.POST))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)
        template_vars = {"timeofday": time.asctime()}
        template = jinja_environment.get_template("templates/homepage.html")
        self.response.write(template.render(template_vars))



class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>Signed Out</body></html>')


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/login.html")
        self.response.write(template.render())

class EnglishHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/englishpageoptions.html")
        self.response.write(template.render())

class MathHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/mathpageoptions.html")
        self.response.write(template.render())

class ScienceHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/sciencepageoptions.html")
        self.response.write(template.render())

class SocialScienceHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/socialscienceoptions.html")
        self.response.write(template.render())

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/logout', LogoutHandler),
    ('/login', LoginHandler),
    ('/english', EnglishHandler),
    ('/math', MathHandler),
    ('/science', ScienceHandler),
    ('/socialscience', SocialScienceHandler)
], debug=True)
