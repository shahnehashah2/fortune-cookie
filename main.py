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
import random

def getRandomFortune():
    fortunes = ["Consider eating more fortune cookies",
                "I see much code in your future",
                "Code or Die",
                "You are on your way to braving the web"]

    return random.choice(fortunes)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'
        luckyNum = str(random.randint(1, 99))
        luckySentence = '<p>Your lucky number is: <strong>{}</strong></p>'.format(luckyNum)
        fortune = getRandomFortune()
        fortuneSentence = '<p>Your fortune is: <strong>{}</strong></p>'.format(fortune)
        tryAgainButton = '<a href="."><button>Another cookie please!</button></a>'
        content = header + luckySentence + fortuneSentence + tryAgainButton
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
