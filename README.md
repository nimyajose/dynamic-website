# dynamic-website
This is a dynamic website using python django

## 🌟 Features

- Dynamic homepage banner (admin editable)
- Event carousel with SwiperJS
- Event detail pages
- About Us section with editable image and content
- Functional area cards (Cultural Programs, Charity Events, etc.)
- Responsive design (mobile-friendly)
- Contact Us and Footer with address, links, and social media
- Django admin for all content updates
- Default fallback images if not provided
- Styled using Bootstrap 5 & FontAwesome

---

## 🚀 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap, SwiperJS
- **Database**: SQLite (default, can switch to PostgreSQL)
- **Version Control**: Git + GitHub

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/nimyajose/dynamic-website.git
   cd dynamic-website
   
Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate  # macOS/Linux

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Start the development server:
python manage.py runserver
