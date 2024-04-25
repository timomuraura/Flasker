from flask import Flask, render_template
app = Flask(__name__)

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


