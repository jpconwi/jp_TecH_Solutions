# JP Tech Solutions: landing page

Flask landing page for IoT, robotics, web, and capstone project services.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Change your contact details

The contact button links to Messenger (https://m.me/61592641898901). To change it, edit `SITE` in `app.py` or set the `MESSENGER_URL` environment variable.

Robot and website examples live in `ROBOTS` and `SITES` in `app.py`.

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
3. Optional: set `MESSENGER_URL` under **Environment Variables** to override the default link.
4. Click **Deploy**.

Or with the CLI: `npm i -g vercel` then `vercel` inside this folder.

## Structure

```
app.py            Flask app (exposes `app`, which Vercel looks for)
templates/        Jinja templates
public/           CSS and JS, served at the site root
requirements.txt  Python dependencies
```
