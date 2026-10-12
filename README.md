# JP Tech Solutions: landing page

Flask landing page for IoT, web, and capstone project services.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Change your contact details

Edit `SITE` in `app.py`, or set environment variables:

- `CONTACT_EMAIL`: your email address
- `MESSENGER_URL`: your Messenger link (optional, hides the button if empty)

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial landing page"
git branch -M main
git remote add origin https://github.com/<your-username>/jp-tech-solutions.git
git push -u origin main
```

## Deploy to Vercel

1. Go to vercel.com, choose **Add New > Project**, and import the GitHub repo.
2. Leave the framework preset on **Flask** (Vercel finds `app.py` automatically).
3. Add `CONTACT_EMAIL` and `MESSENGER_URL` under **Environment Variables**.
4. Click **Deploy**.

Or with the CLI: `npm i -g vercel` then `vercel` inside this folder.

## Structure

```
app.py            Flask app (exposes `app`, which Vercel looks for)
templates/        Jinja templates
public/           CSS and JS, served at the site root
requirements.txt  Python dependencies
```
