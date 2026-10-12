import os
from flask import Flask, render_template

# Static files live in /public so Flask serves them locally
# and Vercel serves them from its CDN in production.
app = Flask(__name__, static_folder="public", static_url_path="")

# ---- Edit these (or set them as Vercel environment variables) ----
SITE = {
    "name": "JP Tech Solutions",
    "email": os.environ.get("CONTACT_EMAIL", "you@example.com"),
    "messenger": os.environ.get("MESSENGER_URL", ""),  # e.g. https://m.me/yourpage
}

SERVICES = [
    {
        "title": "IoT and embedded systems",
        "text": "Microcontroller builds with sensors, relays, and displays, plus the dashboard that shows what the device is doing.",
        "items": ["ESP32 and Arduino projects", "Sensor monitoring and alerts", "Automation and control panels"],
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
    return render_template("index.html", site=SITE, services=SERVICES, steps=STEPS, ideas=IDEAS)


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
