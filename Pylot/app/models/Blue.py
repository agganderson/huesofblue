
from system.core.model import Model
import re

class Blue(Model):
    def __init__(self):
        super(Blue, self).__init__()


    def is_first_record(self):
        get_user_query = 'SELECT * FROM users ORDER BY id DESC LIMIT 1'
        if self.db.query_db(get_user_query) == []:
            return True
        else:
            return False

    def create_user(self, user_info, concern_info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

         

        if len(user_info['first_name']) < 3:
            errors.append('First name must be longer than 3 character')
        if not user_info['first_name']:
            errors.append('First name cannot be empty')
        if len(user_info['username']) < 3:
            errors.append('User name must be longer than 3 character')
        if not user_info['username']:
            errors.append('User name cannot be empty')
        if len(user_info['username']) < 3:
            errors.append('Last name must be longer than 3 character')
        if not user_info['last_name']:
            errors.append('Last name cannot be empty')
        if len(user_info['zip_code'])!=5:
        	errors.append('Zip code must be 5 characters long')
        if not (user_info['zip_code']).isdigit():
        	errors.append('Zip code can only contain numeric values')     	
        if not user_info['email']:
            errors.append('Email field cannot be empty')
        if not EMAIL_REGEX.match(user_info['email']):
            errors.append('Email not a valid format')
        if not user_info['form_q1']:
            errors.append('Response cannot be empty')
        if not user_info['bio']:
            errors.append('Bio cannot be empty')
        if not user_info['password']:
            errors.append('Password field cannot be empty')
        if not user_info['bio']:
        	errors.append('Bio cannot be empty')
        if len(user_info['password']) < 5:
            errors.append('Password must be longer than 4 characters')
        if not user_info['confirm_password']:
            errors.append('Confirm Password field cannot be empty')
        if user_info['password'] != user_info['confirm_password']:
            errors.append('Passwords do not match')
            print errors
        if errors:
            return {'status': False, 'errors' : errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(user_info['password'])
            query = "INSERT INTO users (form_q1, first_name, last_name, zip_code, email, username, password, bio, mentor, user_level, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'nonadmin', NOW(), NOW())"
            data = [
                user_info['form_q1'], 
                user_info['first_name'], 
                user_info['last_name'], 
                user_info['zip_code'], 
                user_info['email'], 
                user_info['username'], 
                hashed_pw, 
                user_info['bio'], 
                user_info['mentor']  
            ]
            self.db.query_db(query,data)

            get_user = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user)
            print concern_info, "printed"
            concern_query= "INSERT INTO concerns(anxiety, depression, stress, substance_abuse, eating_disorders, relationships, grief, other, users_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data= [
                concern_info['anxiety'],
                concern_info['depression'],
                concern_info['stress'],
                concern_info['substance_abuse'],
                concern_info['eating_disorders'],
                concern_info['relationships'],
                concern_info['grief'],
                concern_info['other'],
                user[0]['id']
            ]
            self.db.query_db(concern_query, data)
            return {'status' : True , 'user' : user[0]}

    def signin(self, user_info):
    	errors=[]
    	if not user_info['username']:
    		errors.append('User name required')

    	if not user_info['password']:
    		errors.append('Password required')

    	if errors:
    		return {'status': False, 'errors': errors}
    	else:
    		select_user_query = "SELECT * FROM users WHERE username = %s LIMIT 1"
    		data = [user_info['username']]
    		user= self.db.query_db(select_user_query, data)

    		if len(user) > 0:
    			if self.bcrypt.check_password_hash(user[0]['password'], user_info['password']):
    				return {'status': True, 'user': user[0]}
    			else:
    				errors.append('Invalid username/password')
    				return {'status': False, 'errors': errors}
    		else:
    			errors.append('Username was not found')
    			return {'status': False, 'errors': errors}

    def get_all_mentors(self):
        return self.db.query_db("SELECT * FROM users WHERE mentor = 'Yes'")

    def get_mentor_by_id(self, id):
        print id, "in sql"
        query = "SELECT * FROM users WHERE id = "+id+" LIMIT 1"
        print query
        print self.db.query_db(query)
 
        return self.db.query_db(query)

    # def get_all_concerns(self,user_info):
    #     query = "SELECT * FROM concerns WHERE users_id = %s"
    #     data = [user_info['id']]
    #     return self.db.query_db(query, data)

    def get_mentor_concerns(self, string):
        query = "SELECT * FROM users LEFT JOIN concerns ON concerns.users_id = users.id WHERE users.mentor='Yes' HAVING " + string
        return self.db.query_db(query)

    def disp_mentored(self):

        select_mentored= "SELECT * FROM users WHERE mentor IS NULL"
        return self.db.query_db(select_mentored)

    def disp_connections(self, user_info):

        query = "SELECT first_name, username FROM users WHERE id IN (SELECT users_id1 FROM connections WHERE users_id = %s)"
        data= [user_info[id]]
        return self.db.query_db(query, data)










