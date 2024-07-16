from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return 'Hello, World! This is my Python web application.'

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

