from flask import Flask
# Anytime we run an app on Python, __name__ gets defined for the app and its import
app = Flask(__name__)
# @app.route will call the function follows it
#   whenever the web server receive the request with the url matches the argument
@app.route('/')
def hello_world():
    return 'Hello, World!'
# if statement make sure the script is executed directly from the Python interpreter
#   and not used as an imported module
if __name__ == '__main__':
    # enable debug support will reload the server each time there is a change in code
	app.debug = True
    # app.run runs the local server with our app
	app.run(host = '0.0.0.0', port = 8080)
