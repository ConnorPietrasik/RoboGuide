from flask import Flask, render_template

app = Flask(__name__)

cur_location = [0, "BEHIND YOU!"]
locations = [[1, "Science Building"], [2, "Engineering Building"], [3, "SRAC"]]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", cur_location=cur_location)

@app.route("/locations/", methods=["GET"])
def locations_page():
    return render_template("locations.html", cur_location=cur_location, locations=locations)

#TODO: Add lookup for description and name
@app.route("/locations/<id>", methods=["GET"])
def locations_individual(id):
    return render_template("locations_individual.html", id=id, name="SRAC", description="This state-of-the-art facility houses everything you need to begin or maintain your fitness goals. The SRAC offers cycling classes, a rock-climbing wall, join a pick-up game, or just hang out by the recreation pool. SRAC offers you a way to pursue a host of physical activities right on campus. You might even discover a lifelong pastime or hobby.")

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html", working=True, cur_location=cur_location, locations=locations)

if __name__ == "__main__":
    app.run("0.0.0.0", 80)