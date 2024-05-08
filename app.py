from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



# Create a flask instance - form submission security
app = Flask(__name__)
app.config['SECRET_KEY'] = "My super secret key thats no one supposed to know"

# Create a form Class
class NamerForm(FlaskForm):
    name = StringField("what's your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    #Boolean - true or false                        ##validators
    #DateField                                      #DataRequired
    #DateTimeField -has both                        #Email
    #DecimalField - eg 1.006                        #EqualTo
    #FileField - if uploading a file                #InputRequired
    #Hidden field                                   #IPAddress
    #MultipleField                                  #MacAddress
    #FieldLIst                                      #Length
    #FloatField                                     #NumberRange
    #FormField                                      #Optional
    #integerField                                   #Regexp - regular expression
    #PasswordField                                  #URL
    #RadioField                                     #UUID
    #SelectField                                    #AnyOf
    #SelectMultipleField                            #NoneOf
    #SubmitField
    #StringField
    #TextAreaField


   #Hello world

#@app.route("/")
#def hello_world():
    #return "<p>Hello, World!</p>"

   #user john!!! - Before template rendering

#@app.route('/user/<name>')
#def user(name):
#return "<h1>Hello {}!!!</h1>".format(name)

  #template rendering - index
@app.route('/')
def index():
   first_name = "John"
   stuff = "this is <strong> bold  text </strong> mark up"
   favorite_pizza = ["pepperoni","cheese","Burger","chocolate",4,5]
   return render_template('index.html',
                          first_name=first_name ,stuff = stuff,
                          favorite_pizza = favorite_pizza)
 
  #Template rendering User

@app.route("/user/<name>")
def user(name):
    return  render_template("user.html",user_name=name)

#custom Error pages 
#invalid URL
@app.errorhandler(404)
def page_not_found(e): 
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500) 
def page_not_found(e): 
    return render_template("500.html"), 500

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
  
  # Your code to handle GET or POST requests for the '/name' route
  name = None
  form = NamerForm()

  #Validate Formpr
  if form.validate_on_submit():
    
     # print("validated form")
      name = form.name.data
      #print("name", name)
      form.name.data = ''
      
  return render_template("name.html", 
                               name = name,
                               form = form)
   





