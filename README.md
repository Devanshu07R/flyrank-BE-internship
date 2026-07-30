# 📚 Week 5 – Polite Web Scraper

A professional and ethical web scraper built with **FastAPI**, **Requests**, and **BeautifulSoup** that collects structured book data from the **Books to Scrape** practice website while respecting web scraping best practices such as `robots.txt`, custom `User-Agent`, and polite rate limiting.

---

## 🚀 Features

- ✅ FastAPI REST API
- ✅ Ethical scraping with `robots.txt`
- ✅ Custom User-Agent identification
- ✅ Polite 1-second request delay
- ✅ HTML parsing using BeautifulSoup
- ✅ Extracts:
  - Book Title
  - Price
  - Rating
  - Availability
- ✅ Cleans and normalizes extracted data
- ✅ Saves structured records to `books.json`
- ✅ Returns structured JSON response

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- lxml

---

## 📂 Project Structure

```text
week5-polite-scraper/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   └── scraper.py
│
├── books.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Devanshu07R/flyrank-BE-internship.git
```

Move to the project directory:

```bash
cd week5-polite-scraper
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

## 📌 API Endpoints

### Root

```http
GET /
```

Returns a welcome message.

---

### Health Check

```http
GET /health
```

Checks whether the API is running.

---

### Scrape Books

```http
GET /scrape
```

Downloads the Books to Scrape homepage, extracts book information, cleans the data, stores it in `books.json`, and returns the structured dataset.

---

## 📄 Example Response

```json
{
  "status": 200,
  "count": 20,
  "books": [
    {
      "title": "A Light in the Attic",
      "price": 51.77,
      "currency": "GBP",
      "availability": true,
      "rating": 3,
      "scraped_at": "2026-07-30T06:20:15"
    }
  ]
}
```

---

## 🔄 Data Pipeline

```text
Website
   │
   ▼
Check robots.txt
   │
   ▼
Polite Delay
   │
   ▼
Download HTML
   │
   ▼
Parse HTML
   │
   ▼
Extract Book Data
   │
   ▼
Clean & Normalize
   │
   ▼
Save books.json
   │
   ▼
Return JSON API
```

---

## 📖 Learning Outcomes

This project demonstrates:

- REST API development with FastAPI
- Ethical web scraping practices
- HTML parsing using BeautifulSoup
- Data extraction using CSS selectors
- Data cleaning and normalization
- JSON serialization
- Building reusable backend data pipelines

---

## 👨‍💻 Author

**Devanshu Dasgupta**

Backend AI Engineering Intern (FlyRank AI)

GitHub: https://github.com/Devanshu07R

LinkedIn: https://www.linkedin.com/in/devanshu-dasgupta/

---

## 📜 License

This project was developed as part of the **FlyRank Backend AI Engineering Internship – Week 5 Assignment** for educational purposes.