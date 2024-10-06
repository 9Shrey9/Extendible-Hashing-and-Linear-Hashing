
# Extendible Hashing and Linear Hashing

This project implements Extendible Hashing and Linear Hashing algorithms using Flask (Python) for the backend and React (JavaScript) for the frontend.

## Features

- **Extendible Hashing**: Dynamically adjusts the hash table size based on key distribution.
- **Linear Hashing**: Expands the hash table in a more controlled manner without doubling size every time.
- **REST API (Flask)**: Insert, delete, and search key-value pairs.
- **React Frontend**: Displays the hash table and allows interactions (insert, delete, search).
- **Real-time Updates**: Frontend reflects backend changes in real-time.
- **Operation Logging**: Tracks all operations performed on hash tables.

---

## Requirements

### Backend
- **Python**: 3.9+
- **Flask**: 3.0+ 
  
### Frontend
- **Node.js**: 14.17+ (or newer)
- **React**: 17.0+

---

## Installation & Setup

Follow these instructions to set up the backend and frontend components of the project.

### 1. Clone the Repository (if applicable)

```bash
git clone -b master https://github.com/9Shrey9/Extendible-Hashing-and-Linear-Hashing.git
cd Extendible-Hashing-and-Linear-Hashing
```

### 2. Backend Setup (Flask)
Create a Virtual Environment (Optional but Recommended):

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install Python Dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask Backend:

```bash
python app.py
```

The Flask server will start at http://localhost:5000.

### 3. Frontend Setup (React)
Open a New Terminal for the Frontend (while the backend is running).

Navigate to the Frontend Directory:

```bash
cd frontend
```

Install Node.js Dependencies:

```bash
npm install
```

Run the React Application:

```bash
npm start
```

The React development server will start at http://localhost:3000. If the project doesn't launch due to permission issues, you can fix it with:

```bash
chmod +x node_modules/.bin/react-scripts
```

## Usage
Open your web browser and navigate to http://localhost:3000.

Use the interface to:
- **Insert**: Add key-value pairs to the hash table.
- **Delete**: Remove key-value pairs.
- **Search**: Find entries in the hash table.

The backend will process your operations in real-time, and the frontend will display the updated hash tables accordingly.

## Project Structure
```bash
project/
├── app/                     # Flask backend
│   ├── __init__.py
│   ├── models/               # Hashing algorithms
│   │   ├── __init__.py
│   │   ├── extendible_hashing.py
│   │   └── linear_hashing.py
│   ├── routes.py             # API routes for insert, delete, search
│   └── app.py                # Flask entry point
├── frontend/                 # React frontend
│   ├── package.json          # Node dependencies
│   ├── package-lock.json     # Exact dependency versions
│   ├── public/
│   │   └── index.html        # Base HTML file for React
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── App.js
│   │   │   ├── InsertDeleteSearch.js
│   │   │   └── App.css
│   │   ├── index.js          # Entry point for React
│   │   ├── index.css         # Global CSS for React
│   └── .gitignore            # Files ignored by version control
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── .gitignore                # Global gitignore for the project
```

## Important Notes
- **Virtual Environment (venv)**: It is recommended to use a virtual environment for the Python backend to avoid conflicting package versions. You can deactivate it using `deactivate` once done.
- **React Permissions**: If `npm start` fails due to permission errors, use `chmod +x node_modules/.bin/react-scripts` to resolve the issue.
- **Frontend and Backend Communication**: Ensure both backend (Flask) and frontend (React) are running simultaneously on their respective ports (http://localhost:5000 for Flask and http://localhost:3000 for React). The frontend will communicate with the Flask API.

## Logging & Debugging
Backend operations are logged by default. Check the console or logs to track insert, delete, and search operations.
If you face issues, check the network activity in your browser's developer tools to ensure API requests are being sent and received correctly.

## Troubleshooting

### Common Issues:
- **Backend Fails to Start**:
    - Ensure Flask is installed and your Python version is 3.9+.
    - Check if another process is using port 5000, which Flask uses by default.
- **Frontend Fails to Start**:
    - Make sure Node.js and npm are installed correctly.
    - Run `npm install` to ensure all dependencies are installed.
- **React Doesn't Load Properly**:
    - Clear your browser cache or disable any ad-blocking extensions that might interfere with the frontend.
