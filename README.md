# 🕵️ Website Content Monitor

A minimal, modern, and fully automated web application that acts as a real user to verify if your website content is online and rendering correctly. 

Unlike simple ping monitors that can be tricked by empty templates or 404 pages returning a 200 OK status, this tool uses **Playwright** to launch a real headless browser, render the Javascript, and search the actual screen for specific text you define. 

## ✨ Features
- **Real User Simulation:** Renders the full DOM just like a real browser.
- **Content Verification:** Checks if specific target text exists on the page.
- **Modern UI:** Built with Streamlit featuring a sleek, responsive, mobile-first dark mode design.
- **Custom Scheduling:** Define exact intervals (gaps) and number of visits for monitoring.

## 🚀 How to Run Locally

### Prerequisites
You need to have Python (3.9+) installed on your system.

### 1. Clone the repository
```bash
git clone https://github.com/Aryan1274/Content-Monitor.git
cd Content-Monitor
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment
- **Windows:** `.\venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Install Playwright Browsers
Since the tool needs a real browser engine to check the pages, you must install the playwright chromium binaries:
```bash
playwright install chromium
```

### 6. Start the App
```bash
streamlit run app.py
```
The app will automatically open in your default web browser at `http://localhost:8501`.

## 🛠️ Usage
1. Enter your **Article URL** (e.g., `https://yourwebsite.com/article-1`).
2. Enter your **Target Text** (e.g., a specific heading, title, or sentence that proves the content loaded).
3. Set your desired **Number of Visits** and the **Gap** in seconds between each visit.
4. Click **Start Monitoring** and watch the live status updates!
