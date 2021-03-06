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


jinja_auto = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))




class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1>KARL'S SANDBOX!</h1><br><img src=\"http://www.lowes.com/"
        	"images/LCI/Planning/HowTos/ht_BuildaSandbox_hero_image.jpg\" alt=\"poodle\">")

class SerainaHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_auto.get_template('seraina-app.html')
        self.response.out.write(template.render())


class VideoHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_auto.get_template('test-video.html')
        self.response.out.write(template.render())

        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/serainasbday', SerainaHandler),
    ('/videotest', VideoHandler)
], debug=True)
