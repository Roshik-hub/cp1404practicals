from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_value = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_value)
        return f"<h2>{celsius_value}°C is {fahrenheit:.2f}°F</h2>"
    except ValueError:
        return "<h2>Please enter a valid number.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
