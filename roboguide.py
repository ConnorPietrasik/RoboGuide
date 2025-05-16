from flask import Flask, render_template, Response, request
import utils

app = Flask(__name__)

with open("current_location", "r") as f:
    cur_location = int(f.read())

#Future idea: switch to database and add easy admin features
locations = [
    {
        "name": "Science Building",
        "description": "The Science Building houses state-of-the-art labs and lecture halls for biology, chemistry, and physics.",
        "coords": [37.33470305151793, -121.8847259065248]
    },
    {
        "name": "Engineering Building",
        "description": "The Engineering Building features cutting-edge technology and collaborative spaces for engineering students.",
        "coords": [37.336856988289135, -121.88115320429411]
    },
    {
        "name": "SRAC",
        "description": "This state-of-the-art facility houses everything you need to begin or maintain your fitness goals. The SRAC offers cycling classes, a rock-climbing wall, join a pick-up game, or just hang out by the recreation pool. SRAC offers you a way to pursue a host of physical activities right on campus. You might even discover a lifelong pastime or hobby.",
        "coords": [37.33465881488258, -121.87934233827066]
    },
    {
        "name": "MLK Library",
        "description": "The King Library is a unique partnership between the City of San José and San José State University that blends the function of a university library - with study spaces, research resources for students and faculty - with that of the city's core library branch - with amenities, collections, resources, and exhibitions open to the public. This eight-story, 475,000 square feet center for learning, collaboration and community is one of the nation's largest and few joint city-university library facilities.",
        "coords": [37.335555901073555, -121.88501377366686]
    },
    {
        "name": "Washington Square Hall",
        "description": "Washington Square Hall houses several departments of the College of Humanities and the Arts the College of Health and Human Sciences.",
        "coords": [37.33421592974226, -121.8842537353073]
    },
    {
        "name": "Yoshihiro Uchida Hall",
        "description": "Yoshihiro Uchida Hall houses several departments of the College of Health and Human Sciences.",
        "coords": [37.33364525493663, -121.88383264206446]
    },
    {
        "name": "West Parking Garage",
        "description": "If you're paying for parking, this is your best bet for Duncan Hall or Science Building classes!",
        "coords": [37.332363727882786, -121.88302547970933]
    },
    {
        "name": "Duncan Hall",
        "description": "Duncan Hall houses several departments of the College of Science.",
        "coords": [37.33270496033551, -121.88203842683816]
    },
    {
        "name": "Interdisciplinary Science Building",
        "description": "The Interdisciplinary Science Building houses several departments of the College of Science.",
        "coords": [37.33300527509904, -121.88304353818101]
    },
    {
        "name": "Spartan Memorial",
        "description": "The Spartan Memorial Chapel houses the Native American Indigenous Student Success Center (NAISSC).",
        "coords": [37.33421023506526, -121.88332433546836]
    },
    {
        "name": "South Parking Garage",
        "description": "Fights with North Parking Garage for size; a decent enough place to park",
        "coords": [37.33306771150045, -121.88086713879345]
    },
    {
        "name": "MacQuarrie Hall",
        "description": "MacQuarrie Hall houses several departments of the College of Health and Human Sciences, College of Humanities and the Arts, and the College of Science.",
        "coords": [37.3335153298765, -121.88178657084558]
    },
    {
        "name": "Sweeney Hall",
        "description": "Sweeney Hall houses several departments of the Connie L. Lurie College of Education and the College of Health and Human Sciences.",
        "coords": [37.33390134305714, -121.88096313272109]
    },
    {
        "name": "Spartan Complex",
        "description": "Spartan Complex houses several departments of the College of Health and Human Sciences and the College of Humanities and the Arts.",
        "coords": [37.33415662797781, -121.88264772568954]
    },
    {
        "name": "Spartan Complex East",
        "description": "They really hated the west one, so they decided to split and this one lost the pure identity",
        "coords": [37.334517046109006, -121.88180819431422]
    },
    {
        "name": "Student Wellness Center",
        "description": "The Student Wellness Center is home to counseling, medical, and Well-being needs at SJSU. Visit your doctor, talk to your counselor, fill prescriptions, relax in the Wellness Lounge, and more!",
        "coords": [37.33482879506837, -121.88135365452284]
    },
    {
        "name": "Faculty Office Building",
        "description": "A building full of offices for faculty. Also alleged to include the Department of Philosophy",
        "coords": [37.33463755091976, -121.88259104666291]
    },
    {
        "name": "Dwight Bentel Hall",
        "description": "Dwight Bentel Hall is home to several departments of the College of Humanities and the Arts.",
        "coords": [37.3350320478762, -121.8826381417955]
    },
    {
        "name": "Tower Hall",
        "description": "Tower Hall is the centerpiece of San Jose Staté University. Built in 1910 to replace a previous building damaged in the earthquake of 1906, Tower Hall is the oldest structure on campus. State architects Sellon & Hemmings designed the building in the Spanish Revival style with influences from Gothic, Renaissance Revival, and Modern, reflecting the rich diversity found in San José. The building is still used as a lecture hall and serves as the office of the presidential administration. The buildings that connected with Tower Hall to create the quadrangle were demolished in 1964 after it was determined that the structures were not earthquake safe.",
        "coords": [37.335249039590664, -121.88324034957327]
    },
    {
        "name": "Central Classroom Building",
        "description": "The Central Classroom Building is home to several departments in the College of Health and Human Sciences.",
        "coords": [37.335618462059685, -121.88188932912858]
    },
    {
        "name": "Clark Hall",
        "description": "Robert D. Clark Hall (university president 1964-1969) houses the following divisions and departments of the following colleges:\nCollege of Humanities and the Arts\nCollege of Social Sciences\nInformation Technology customer service lab, on the ground floor\nSJSU Cares: student basic needs assistance, located on the ground floor\nTitle IX and Equal Opportunity Office, on the ground floor\nUndocuSpartan Student Resource Center, on the ground floor\nOffice of the President\nDivision of Academic Affairs/Office of the Provost\nDivision of Administration and Finance\nDivision of Research and Innovation\nDivision of Student Affairs\nDivision of University Advancement",
        "coords": [37.336169510013505, -121.88249101870139]
    },
    {
        "name": "Computer Center",
        "description": "The Computer Center building houses Information Technology infrastructure and offices. This building is not accessible to the general public and campus community.",
        "coords": [37.335932182721606, -121.8833043520188]
    },
    {
        "name": "Hugh Gillis Hall",
        "description": "Hugh Gillis Hall houses several departments of the College of Humanities and the Arts and the College of Social Sciences.",
        "coords": [37.336046113489324, -121.8845073339862]
    },
    {
        "name": "Dudley Moorhead Hall",
        "description": "Dudley Moorhead Hall houses several departments of the College of Social Sciences.",
        "coords": [37.33629776023458, -121.88399234988667]
    },
    {
        "name": "Administration Building",
        "description": "The Administration Building houses the following departments, and more\nAccessible Education Center\nCareer Center\nCollege of Graduate Studies\nOffice of Diversity, Equity and Inclusion\nStudent Conduct and Ethical Development\nUniversity Personnel",
        "coords": [37.336754134393125, -121.88282290680168]
    },
    {
        "name": "Industrial Studies",
        "description": "The Industrial Studies building houses several departments of the College of Health and Human Sciences, the College of Humanities and the Arts, and the College of Social Sciences.",
        "coords": [37.33757708125822, -121.88061035734562]
    },
    {
        "name": "Diaz Compean Student Union",
        "description": "The Diaz Compean Student Union at San José State University is the central hub for student life on campus. With event venues, individual and group study and collaboration space, food and retail amenities, a bowling and billiards center, the Student Union hosts year-round vibrancy for students, employees and campus visitors alike.\nThe Student Union is named in honor of South Bay residents and friends of the university Ramiro Compean and Lupe Diaz Compean and was completed in 2016.",
        "coords": [37.3365573673207, -121.88062890034209]
    },
    {
        "name": "Music Building",
        "description": "The Music Building is home to several departments of the College of Humanities and the Arts.",
        "coords": [37.33561671510048, -121.8808654067697]
    },
    {
        "name": "Art and Design Building",
        "description": "The Art and Design Building is home to several departments of the College of Humanities and the Arts.",
        "coords": [37.33598767892253, -121.87981089268409]
    },
    {
        "name": "Provident Credit Union Events Center",
        "description": "The Provident Credit Union Event Center at San José State University hosts major events including Convocation, Commencement, sports games and matches, concerts, conferences and more.\nReservations of the Event Center for events are made through the facilities reservation process.",
        "coords": [37.33537845281764, -121.87989055022291]
    },
    {
        "name": "Health Building",
        "description": "The Health Building is home to several departments in the College of Health and Human Sciences.",
        "coords": [37.335665617782546, -121.87909253940686]
    },
    {
        "name": "Campus Village 2",
        "description": "Campus Village 2 is a residence hall managed by University Housing Services.",
        "coords": [37.33478747466643, -121.87856220558672]
    },
    {
        "name": "Washburn Hall",
        "description": "Washburn Hall is a residence hall managed by University Housing Services.",
        "coords": [37.333647415444524, -121.87933981487973]
    },
    {
        "name": "Dining Commons",
        "description": "The Dining Commons is the main dining hall with a range of food options open to all students, faculty and staff. Enter across from Washburn Hall or from Joe West Hall.",
        "coords": [37.33406061350736, -121.8784977208977]
    },
    {
        "name": "Joe West Hall",
        "description": "Joe West Hall is a residence hall managed by University Housing Services. ",
        "coords": [37.334253639560764, -121.87805770782599]
    },
    {
        "name": "Associated Students Childhood Development Center",
        "description": "The Associated Students Childhood Development Center is a non-profit early education and care program for children ages 4 months through 5 years and serves up to 90 children.",
        "coords": [37.3329789771788, -121.87775782339658]
    },
    {
        "name": "North Parking Garage",
        "description": "A pretty decent garage, but honestly I'd recommend coming 10 mins early and street parking for free",
        "coords": [37.339313571571175, -121.88075548674985]
    },
    {
        "name": "Business Tower",
        "description": "The Boccardo Business Tower is home to the Lucas College and Graduate School of Business.",
        "coords": [37.33704987631422, -121.87890115926356]
    },
    {
        "name": "Boccardo Business Classroom Building",
        "description": "The Boccardo Business Classroom Building is home to the Lucas College and Graduate School of Business.",
        "coords": [37.33665177435571, -121.87863563413408]
    },
    {
        "name": "Central Plant",
        "description": "The Central Plant is a co-generating plant that augments San José State University\'s power supply from the power grid and provides power redundancy to the campus in the event of utility failure in the area. The Central Plant helps SJSU maintain progress towards sustainable energy production and self-sufficiency.",
        "coords": [37.33609683915032, -121.87844666248884]
    },
    {
        "name": "Campus Village C",
        "description": "Campus Village C is a residence hall managed by University Housing Services. ",
        "coords": [37.33537669834516, -121.87823694787265]
    },
    {
        "name": "Campus Village B",
        "description": "Campus Village B is a residence hall managed by University Housing Services. ",
        "coords": [37.33499651475334, -121.87747009153779]
    },
    {
        "name": "Campus Village A",
        "description": "Campus Village A is a residence hall managed by University Housing Services with availability for students and employees.",
        "coords": [37.334490795861356, -121.87751971165358]
    }
]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/location_map/", methods=["GET"])
def location_map():
    return render_template("map.html", cur_location=cur_location, locations=locations)

@app.route("/locations/", methods=["GET"])
def locations_page():
    return render_template("locations.html", cur_location=cur_location, locations=locations)

@app.route("/locations/<id>", methods=["GET"])
def locations_individual(id):
    location = locations[int(id)]
    if not location:
        return "Location not found", 404
    return render_template("locations_individual.html", id=id, name=location["name"],
        description=location["description"])

@app.route("/locations/current", methods=["POST"])
def set_current_location():
    global cur_location 
    cur_location = int(request.form["id"])
    with open("current_location", "w") as f:
        f.write(str(cur_location))
    return location_map()

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html", working=True, cur_location=cur_location, locations=locations)

@app.route("/video_feed")
def video_feed():
    return Response(utils.gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run("0.0.0.0", 80)