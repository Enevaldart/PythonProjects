from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ''
    return (
       """   <form action="" method="get">
                celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert">
              </form>"""
       + "fahrenheit: "
       + fahrenheit
    )
#@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
      fahrenheit = float(celsius) * 9 / 5 + 32
      fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
      return str(fahrenheit)
    except ValueError:
      return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)