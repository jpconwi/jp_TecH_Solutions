import os
from flask import Flask, render_template

# Static files live in /public so Flask serves them locally
# and Vercel serves them from its CDN in production.
app = Flask(__name__, static_folder="public", static_url_path="")

# ---- Edit these (or set them as Vercel environment variables) ----
SITE = {
    "name": "JP Tech Solutions",
    "messenger": os.environ.get("MESSENGER_URL", "https://m.me/61592641898901"),
}

SERVICES = [
    {
        "title": "IoT and embedded systems",
        "text": "Microcontroller builds with sensors, relays, and displays, plus the dashboard that shows what the device is doing.",
        "items": ["ESP32 and Arduino projects", "Sensor monitoring and alerts", "Automation and control panels"],
    },
    {
        "title": "Robotics",
        "text": "Small robots built around real tasks: following a path, avoiding obstacles, picking things up, or being driven from a phone.",
        "items": ["Line followers and obstacle-avoiding cars", "Servo robotic arms", "Wi-Fi and Bluetooth remote control"],
    },
    {
        "title": "Web development",
        "text": "Websites and web apps for small businesses and organizations, built to load fast and be easy to update.",
        "items": ["Landing pages and business sites", "Wix and WordPress", "Custom Python (Flask) apps"],
    },
    {
        "title": "Capstone projects",
        "text": "A full system for your thesis, built around a real problem, with the documentation you need to defend it.",
        "items": ["Title and scope planning", "Hardware, software, or both", "Manuscript help and defense prep"],
    },
]

STEPS = [
    ("Pick the problem", "We choose a title your panel will take seriously and that fits your budget and deadline."),
    ("Design the system", "Block diagram, parts list, database, and screens, agreed before anything is built."),
    ("Build and test", "You get working builds early, so you can see progress and give feedback."),
    ("Document and rehearse", "Diagrams, user manual, and a walkthrough so you can explain every part yourself."),
]

ROBOTS = [
    {
        "name": "Line-following delivery cart",
        "text": "Follows a taped path between two stations and stops when something blocks it. A common fit for logistics or smart-factory themes.",
        "parts": "Arduino Uno, IR sensor array, L298N driver, 4 gear motors, ultrasonic sensor",
        "time": "3 to 4 weeks",
    },
    {
        "name": "Obstacle-avoiding rover with phone control",
        "text": "Drives itself around obstacles, or switches to manual mode from a phone over Bluetooth. Good for first-time robot builders.",
        "parts": "ESP32, HC-SR04 sensors, motor driver, servo, battery pack",
        "time": "2 to 3 weeks",
    },
    {
        "name": "Servo robotic arm (4 axis)",
        "text": "Picks small light items and drops them in a bin, controlled by sliders on a web page. Sized for a desk demo, not a factory.",
        "parts": "ESP32, 4 to 5 servos, 3D-printed or acrylic frame, 5V 3A supply",
        "time": "4 to 6 weeks",
    },
    {
        "name": "Disinfection or watering robot",
        "text": "A wheeled base with a pump and spray nozzle that runs a set route and reports tank level to a dashboard.",
        "parts": "ESP32, relay, mini pump, level sensor, motor driver, chassis",
        "time": "4 to 5 weeks",
    },
]

SITES = [
    {
        "name": "Resort or homestay booking site",
        "text": "Room photos, rates, an availability calendar, and a booking form that sends requests to your Messenger.",
        "tags": ["Mobile first", "Booking form", "Photo gallery"],
        "tone": "sea",
    },
    {
        "name": "Local store with online ordering",
        "text": "Product list with prices, a simple cart, and orders sent to you to confirm. No payment gateway needed to start.",
        "tags": ["Product catalog", "Order form", "Easy to update"],
        "tone": "amber",
    },
    {
        "name": "School or organization portal",
        "text": "Announcements, downloadable forms, a staff directory, and an admin page so you can post updates yourself.",
        "tags": ["Admin login", "Announcements", "Flask and database"],
        "tone": "teal",
    },
    {
        "name": "Capstone web system",
        "text": "Inventory, attendance, or records system with user roles, search, and printable reports for your defense.",
        "tags": ["User roles", "Reports", "Documentation"],
        "tone": "ink",
    },
]

IDEAS = [
    "RFID attendance system",
    "Water level and refill monitor",
    "Plant moisture and irrigation controller",
    "Coin-operated charging or timer station",
    "Room temperature and power logger",
    "Online booking or inventory system",
]


@app.route("/")
def home():
    return render_template("index.html", site=SITE, services=SERVICES, steps=STEPS, ideas=IDEAS, robots=ROBOTS, sites=SITES)


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
