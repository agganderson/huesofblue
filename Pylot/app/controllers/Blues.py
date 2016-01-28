
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
        'username' : request.form['username'],
        'password' : request.form['password']
      }
      status = self.models['Blue'].signin(signin_info)
      if status['status'] == False:
        for message in status['errors']:
          flash(message, 'login_errors')
        return redirect('/login')
      else:
        return redirect('/dashboard')

  def user_reg(self):
      return self.load_view('mentor_reg.html')

  def user_create(self):
      user_info = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'zip_code' : request.form['zip_code'],
        'username' : request.form['username'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
        'form_q1' : request.form['form_q1'],
        'bio' : request.form['bio'],
        'mentor' : request.form['mentor']
      }
      
      concern_info = {
        'concern' : request.form.getlist('concerns')
      }
      print concern_info
      if self.models['Blue'].is_first_record():
        user_info['user_level'] = 'admin'
      else:
        user_info['user_level'] = 'user'
      create_status = self.models['Blue'].create_user(user_info)
      if create_status['status'] == True:
        session['id'] = create_status['user']['id']
        return redirect('/login')
      else:
        for message in create_status['errors']:
          flash(message, 'reg_errors')
        return redirect('/user_reg')

  def dash(self):
      return self.load_view('dashboard.html')

  def logout(self):
      session.clear()
      return redirect('/')