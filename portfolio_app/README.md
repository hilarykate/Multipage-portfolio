# Portfolio App

A Streamlit-based personal portfolio that showcases `Hilary Kate`'s profile, skills, projects, and contact form.

## Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install Streamlit (required):

```bash
pip install streamlit
```

3. Run the portfolio locally:

```bash
streamlit run Home.py
```

## What You'll Find (Features & Functionality)

- Global
	- Built with Streamlit for fast static + interactive pages.
	- Custom CSS for a dark, glassmorphism-style theme, animated hero title, and responsive navigation cards.
- Home (`Home.py`)
	- Hero section with animated title, subtitle, and CTA button linking to Contact.
	- Four navigation cards linking to `About`, `Skills`, `Projects`, and `Contact` pages.
	- Custom footer and social link area.
- About (`pages/1_Aboutme.py`)
	- Profile image and short biography.
	- Personal information block (location, education, languages, interests, hobbies).
- Skills (`pages/2_Skills.py`)
	- Technical skills displayed with progress bars (Python, JavaScript, Node.js, SQL, HTML/CSS, Git).
- Projects (`pages/3_Project.py`)
	- Project showcase containers with image placeholders and titles for each project/certification.
	- `Load More Projects` button that shows a placeholder info message (can be expanded to load extra items).
- Contact (`pages/4_Contact.py`)
	- Contact information (location, email, phone, social links).
	- A contact form implemented with Streamlit `st.form` (name, email, subject, message) and client-side validation.
	- Form currently displays success/error messages; SMTP sending is referenced but not enabled by default.

## Project Structure

- `Home.py` — main Streamlit app and site layout
- `pages/1_Aboutme.py` — About page
- `pages/2_Skills.py` — Skills page
- `pages/3_Project.py` — Projects page
- `pages/4_Contact.py` — Contact page and contact form
- `images/` — images used across pages (profile, project images, screenshots)

## Dependencies

- Streamlit (tested): install with `pip install streamlit`
- Optional: add a `requirements.txt` with pinned versions for reproducibility.

## Customization & Notes

- Theme & Styling: The look-and-feel is driven by embedded CSS in `Home.py`. Edit the CSS block at the top of `Home.py` to change colors, font sizes, animations, or layout.
- Navigation: Cards use local anchor links (Streamlit routing). Adjust card labels and targets in `Home.py`.
- Contact Form: `pages/4_Contact.py` contains placeholder comments where SMTP logic can be added. If you want emails sent from the form, implement secure server-side sending (e.g., use environment variables for credentials and `smtplib` with SSL/TLS), or integrate services like SendGrid.

## Deployment

- Deploy the app to Streamlit Community Cloud, Heroku, or any container host that supports Python/Streamlit.
- For Streamlit Cloud, add `requirements.txt` and follow their repo-based deployment flow.

## Screenshots

Add screenshots to `images/` and reference them here, for example `images/demo.png`.

## License & Contact

- Add a `LICENSE` (e.g., MIT) if you want to open-source the project.
- Contact details and social links live in `pages/4_Contact.py`.