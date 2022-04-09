import flask as f

app = f.Flask(__name__, template_folder="static")


@app.route("/")
def index():
    return f.render_template("index.html")


@app.route("/about")
def about():
    return f.render_template("about.html")


@app.route("/results", methods=["POST", "GET"])
def upload():
    # if f.request.method == "POST":
    # Write the code here for result
    image = f.request.form.get('inp')
    return f.render_template("upload.html", Accuracy=10,
                             stages={"Normal": 0, "Mild": 0, "Moderate": 0, "Severe": 0, "Proliferative": 0},
                             answer="Mild",image=image)


app.run(debug=True, port=8080, host="localhost")
