
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
        session['username'] = status['user']['username']
        session['bio'] = status['user']['bio']
        session['id'] = status['user']['id']
        session['filtered_mentors'] = []
        print session
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

      concern_forms = {
        'concerns' : request.form.getlist('concerns')
      }

      concern_info = {}
      if 'anxiety' in concern_forms['concerns']:
        concern_info['anxiety'] = True
      else:
        concern_info['anxiety'] = False
      
      if 'depression' in concern_forms['concerns']:
        concern_info['depression'] = True
      else:
        concern_info['depression'] = False
      
      if 'stress' in concern_forms['concerns']:
        concern_info['stress'] = True
      else:
        concern_info['stress'] = False
      
      if 'substance_abuse' in concern_forms['concerns']:
        concern_info['substance_abuse'] = True
      else:
        concern_info['substance_abuse'] = False
      
      if 'eating_disorders' in concern_forms['concerns']:
        concern_info['eating_disorders'] = True
      else:
        concern_info['eating_disorders'] = False
      
      if 'relationships' in concern_forms['concerns']:
        concern_info['relationships'] = True
      else:
        concern_info['relationships'] = False 
      
      if 'grief' in concern_forms['concerns']:
        concern_info['grief'] = True
      else:
        concern_info['grief'] = False 
      
      if 'other' in concern_forms['concerns']:
        concern_info['other'] = True
      else:
        concern_info['other'] = False 

      
      
      

      
      # if self.models['Blue'].is_first_record():
      #   user_info['user_level'] = 'admin'
      # else:
      #   user_info['user_level'] = 'user'
      create_status = self.models['Blue'].create_user(user_info, concern_info)
      if create_status['status'] == True:
        return redirect('/login')
      else:
        for message in create_status['errors']:
          flash(message, 'reg_errors')
        return redirect('/user_reg')

  def dash(self):
      user_info = self.models['Blue'].get_all_mentors()      
      concern_info = self.models['Blue'].get_all_concerns(session['id'])
      connection_info = self.models['Blue'].disp_connections(session['id'])
      return self.load_view('dashboard.html', user_info=user_info, m_filter = session['filtered_mentors'], concern_info= concern_info, connection_info=connection_info)

  def filter(self):
    string = ""
    studd = request.form.getlist('issue')
    print studd, "hel"
    checked_concerns= {
    'concerns' : request.form.getlist('issue')
    }

    print checked_concerns, "hel"
    if 'anxiety' in checked_concerns['concerns']:
      if string=="":
        string = "anxiety"
      else:
        string += " AND anxiety"
    if 'depression' in checked_concerns['concerns']:
      if string=="":
        string = "depression"
      else:
        string += " AND depression"
    if 'stress' in checked_concerns['concerns']:
      if string=="":
        string = "stress"
      else:
        string += " AND stress"
    if 'substance_abuse' in checked_concerns['concerns']:
      if string=="":
        string = "substance_abuse"
      else:
        string += " AND substance_abuse"
    if 'eating_disorders' in checked_concerns['concerns']:
      if string=="":
        string = "eating_disorders"
      else:
        string += " AND eating_disorders"
    if 'relationships' in checked_concerns['concerns']:
      if string=="":
        string = "relationships"
      else:
        string += " AND relationships"
    if 'grief' in checked_concerns['concerns']:
      if string=="":
        string = "grief"
      else:
        string += " AND grief"
    if 'other' in checked_concerns['concerns']:
      if string=="":
        string = "other"
      else:
        string += " AND other"      
    filtered_mentors = self.models['Blue'].get_mentor_concerns(string)
    session['filtered_mentors'] = filtered_mentors

    return redirect('/dashboard')

  def profile(self, id):
      print id
      mentor_info = self.models['Blue'].get_mentor_by_id(id)

      return self.load_view('profile.html', mentor_info=mentor_info)

  def connect(self, mentor_id):
      connection = self.models['Blue'].make_connections(session['id'], mentor_id)
      return redirect('/dashboard')   


  def logout(self):
      session.clear()
      return redirect('/login')