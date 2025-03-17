from flask import Flask, render_template, Response
import utils

app = Flask(__name__)

cur_location = [1, "BEHIND YOU!"]
locations = [(1, "Science Building"), (2, "Engineering Building"), (3, "SRAC")]
locations_data = {
    "1": {
        "name": "Science Building",
        "description": "The Science Building houses state-of-the-art labs and lecture halls for biology, chemistry, and physics."
    },
    "2": {
        "name": "Engineering Building",
        "description": "The Engineering Building features cutting-edge technology and collaborative spaces for engineering students."
    },
    "3": {
        "name": "SRAC",
        "description": "This state-of-the-art facility houses everything you need to begin or maintain your fitness goals. The SRAC offers cycling classes, a rock-climbing wall, join a pick-up game, or just hang out by the recreation pool. SRAC offers you a way to pursue a host of physical activities right on campus. You might even discover a lifelong pastime or hobby."
    }
}

@app.route("/", methods=["GET"])
#TODO: Modify to dynamically change map marker depending on goal location
def home():
    return render_template("index.html")

@app.route("/location_map/", methods=["GET"])
def location_map():
    cur_location_coords = [37.33568932985038, -121.88507532212499]  # Example: MLK Library
    current = 'MLK Library'
    return render_template("map.html", cur_location=cur_location, cur_location_coords=cur_location_coords)

@app.route("/locations/", methods=["GET"])
def locations_page():
    return render_template("locations.html", cur_location=cur_location, locations=locations)

@app.route("/locations/<id>", methods=["GET"])
def locations_individual(id):
    location = locations_data.get(id)
    if not location:
        return "Location not found", 404
    return render_template("locations_individual.html", id=id, name=location["name"],
        description=location["description"])

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html", working=True, cur_location=cur_location, locations=locations)

@app.route("/video_feed")
def video_feed():
    return Response(utils.gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run("0.0.0.0", 80)