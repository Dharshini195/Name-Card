from flask import Flask , render_template
import datetime
app = Flask(__name__)

year = datetime.datetime.now().year

@app.route("/")
def hello():
    return render_template("index.html", current_year = year) #rendering html files-> must be inside templates



if __name__ == '__main__':
    app.run(debug=True)