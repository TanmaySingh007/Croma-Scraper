# Project Setup and Running Guide

This guide explains how to set up and run both the backend (Flask) and frontend (Vue.js) for this project.

---

## 1. Backend (Python Flask)

**Requirements:**
- Python 3.x
- (Recommended) Virtual environment

**Steps:**
1. Open a terminal and navigate to the backend directory:
   ```powershell
   cd project/backend
   ```
2. (Optional) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```powershell
   python app.py
   ```
   The backend should now be running, usually at http://127.0.0.1:5000/

---

## 2. Frontend (Vue.js)

**Requirements:**
- Node.js (v14+ recommended)
- npm (comes with Node.js)

**Steps:**
1. Open a new terminal window and navigate to the frontend directory:
   ```powershell
   cd project/frontend
   ```
2. Install dependencies:
   ```powershell
   npm install
   ```
3. Start the development server:
   ```powershell
   npm run serve
   ```
   The frontend should now be running, usually at http://localhost:8080/

---

## 3. Accessing the App

- **Frontend:** Open [http://localhost:8080/](http://localhost:8080/) in your browser.
- **Backend:** The frontend will make API requests to the backend at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (or as configured).

---

## Windows PowerShell Quick Commands

Here are the exact commands to run both backend and frontend in Windows PowerShell:

### Backend
```powershell
cd project/backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Frontend (in a new PowerShell window)
```powershell
cd project/frontend
npm install
npm run serve
```

---

## Troubleshooting

- If you get errors about missing packages, double-check you ran the install commands in both backend and frontend.
- Make sure both servers are running in separate terminals.
- If ports are busy, you may need to change them in the config or scripts.