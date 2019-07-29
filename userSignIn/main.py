import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

class CssiUser(ndb.Model):
    first_name = ndb.StringProperty()
    email = ndb.StringProperty()
    age = ndb.IntegerProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            logout_button = '<a href="%s"> Logout </a>' % logout_url
            existing_user = CssiUser.query().filter(CssiUser.email == email_address).get()
            if existing_user:
                self.response.write('Welcome back to the homepage' + existing_user.first_name + "<br>" + logout_button)
            else:
                self.response.write('''You are a new user, please provide information
                    <form method='post' action='/'>
                        Name: <input type='text' name='first_name'>
                        Age: <input type='text' name='age'>
                        <input type='submit'>
                    </form>
                    <br>
                    %s
                ''' % logout_button)

        else:
            login_url = users.create_login_url('/')
            login_button = '<a href="%s"> Sign In </a>' % login_url
            self.response.write("Please log in!<br>" + login_button)

    def post(self):
        user = users.get_current_user()
        if user:
            cssi_user = CssiUser(
                first_name=self.request.get('first_name'),
                age = int(self.request.get('age')),
                email = user.nickname()
            )
            cssi_user.put()
            self.response.write('Hey thank you for registering! <a href="/"> MainPage </a>')

#initialization code

app = webapp2.WSGIApplication(
    [('/', MainHandler)],
    debug = True
)
