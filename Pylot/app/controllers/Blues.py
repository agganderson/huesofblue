
from system.core.controller import *

class Blues(Controller):
  def __init__(self, action):
       super(Blues, self).__init__(action)
       self.load_model('Blue')

  def index(self):
      return self.load_view('welcome.html')
       
  def login(self):
      return self.load_view('login.html')

  def signin(self):
      signin_info = {
      'username' : request.form['username']
      'password' : request.form['password']
      }
      status = self.models['Blue'].signin(signin_info)

  def mentor_reg(self):
      return self.load_view('mentor_reg.html')

  def mentor_create(self):
      mentor_details = {
        'first_name': request.form['first_name']
        'last_name': request.form['last_name']
        'email': request.form['email']
        'zipcode': request.form['zip_code']
        'username': request.form['username']
        'password': request.form['passwod']
        'confirm_password': request.form['confirm_password']
        'form_q1': request.form['form_q1']
        'form_q2': request.form['form_q1']
        'bio': request.form['bio']
      }
      create_status = self.models['Blue'].create_mentor(mentor_details)
      return redirect('/login')

  def mentored_reg(self):
      return self.load_view('mentored_reg.html')
  
  def mentored_create(self):
      mentored_details = {
        'first_name' : request.form['first_name']
        'last_name' : request.form['last_name']
        'email' : request.form['email']
        'zipcode' : request.form['zip_code']
        'username' : request.form['username']
        'password' : request.form['passwod']
        'confirm_password' : request.form['confirm_password']
        'form_q1' : request.form['form_q1']
        'bio' : request.form['bio']
      }
      create_status = self.models['Blue'].create_mentored(mentored_details)
      return redirect('/login')

  def dash(self):
      return self.load_view('dashboard.html')

  def logout(self):
      session.clear()
      return redirect('/')