
from system.core.controller import *

class Blues(Controller):
    def __init__(self, action):
        super(Blues, self).__init__(action)
        self.load_model('Blue')
    def index(self):
        return self.load_view('welcome.html')
    def login(self):
        return self.load_view('login.html')
