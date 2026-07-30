# 📚 Week 5 – Polite Web Scraper

> A professional and ethical web scraper built with **FastAPI**, **Requests**, and **BeautifulSoup** that extracts structured book data while respecting web scraping best practices such as `robots.txt`, custom `User-Agent`, and polite rate limiting.

---

## 📸 API Preview

> Add a screenshot of your Swagger UI here after running the project.

![Swagger UI](images/Screenshot%202026-07-30%20064937.png)

---

## 🚀 Features

- ✅ FastAPI REST API
- ✅ Ethical web scraping with `robots.txt`
- ✅ Custom `User-Agent` identification
- ✅ 1-second polite request delay
- ✅ HTML parsing using BeautifulSoup
- ✅ Extracts:
  - Book Title
  - Price
  - Rating
  - Availability
- ✅ Cleans and normalizes extracted data
- ✅ Saves structured records into `books.json`
- ✅ Returns structured JSON responses

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
├── README.md
└── images/
    └── swagger-ui.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Devanshu07R/flyrank-BE-internship.git
```

### Navigate to the project

```bash
cd week5-polite-scraper
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

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

Checks whether the API is running successfully.

---

### Scrape Books

```http
GET /scrape
```

Downloads the Books to Scrape homepage, extracts book information, cleans the dataset, stores it in `books.json`, and returns the structured JSON response.

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
Books to Scrape Website
          │
          ▼
   Check robots.txt
          │
          ▼
 Custom User-Agent
          │
          ▼
  Polite Request Delay
          │
          ▼
    Download HTML
          │
          ▼
 Parse with BeautifulSoup
          │
          ▼
 Extract Book Information
          │
          ▼
 Clean & Normalize Data
          │
          ▼
   Save to books.json
          │
          ▼
 Return Structured JSON
```

---

## 📖 Learning Outcomes

This project demonstrates:

- Building REST APIs with FastAPI
- Ethical web scraping practices
- Working with HTTP requests
- HTML parsing using BeautifulSoup
- CSS selector-based data extraction
- Data cleaning and normalization
- JSON serialization
- Building reusable backend data pipelines

---

## 🎯 Assignment Objectives Achieved

- ✅ Respect website `robots.txt`
- ✅ Use a custom `User-Agent`
- ✅ Implement polite scraping with rate limiting
- ✅ Extract structured information from HTML
- ✅ Clean and normalize extracted data
- ✅ Save structured data locally
- ✅ Expose functionality through a REST API

---

## 🚀 Future Improvements

- Support scraping multiple pages automatically
- Accept dynamic URLs as query parameters
- Store data in SQLite/PostgreSQL
- Export to CSV and Excel
- Add structured logging
- Schedule automated scraping jobs
- Integrate with a Vector Database for Retrieval-Augmented Generation (RAG)

---

## 👨‍💻 Author

**Devanshu Dasgupta**

Backend AI Engineering Intern @ FlyRank AI

- GitHub: https://github.com/Devanshu07R
- LinkedIn: https://www.linkedin.com/in/devanshu-dasgupta/

---

## 📜 License

This project was developed as part of the **FlyRank Backend AI Engineering Internship – Week 5 Assignment** for educational purposes.
