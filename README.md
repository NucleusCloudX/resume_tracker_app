Below is a comprehensive `README.md` file that includes all the details in one place:

---

```markdown
# Resume Matcher Application

A professional, end-to-end resume matcher application that compares a candidate's resume with a job description using keyword-based matching. This project uses a Flask backend, a Next.js frontend, MySQL for data storage, and AWS SES for sending emails. Containers are orchestrated using Docker and Docker Compose.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [File Structure](#file-structure)
- [Setup & Deployment](#setup--deployment)
- [Database Setup](#database-setup)
- [AWS SES Setup](#aws-ses-setup)
- [Configuration & File Changes](#configuration--file-changes)
- [Packages Installed on AWS Ubuntu Instance](#packages-installed-on-aws-ubuntu-instance)
- [Additional Notes](#additional-notes)

## Project Overview

This application allows users to:
- **Upload a Resume** (PDF/DOCX)
- **Submit a Job Description**
- **Perform Keyword-based Matching** between the resume and job description
- **Receive an Email** with their match score via AWS SES

The system consists of a **Flask backend** for API logic and a **Next.js frontend** for a modern user interface.

## Technologies Used

- **Backend:** Flask, Flask-SQLAlchemy, PyPDF2, docx2txt, boto3
- **Frontend:** Next.js (React), Tailwind CSS, Axios
- **Database:** MySQL
- **Deployment:** Docker & Docker Compose
- **Cloud Services:** AWS SES for sending emails, (optionally AWS EC2, RDS, and S3)

## Prerequisites

Before deploying on an AWS Ubuntu instance, ensure you have installed:
- **Docker Engine** ([Installation Guide](https://docs.docker.com/engine/install/ubuntu/))
- **Docker Compose** ([Installation Guide](https://docs.docker.com/compose/install/))
- **Git:** 
  ```bash
  sudo apt update && sudo apt install git -y
  ```
- **Node.js and npm:** 
  ```bash
  sudo apt install nodejs npm -y
  ```

## File Structure

```
resume_matcher/
│── backend/                  
│   │── app.py              # Main Flask Application (API endpoints)
│   │── config.py           # Configuration (DB URI, AWS SES settings)
│   │── models.py           # SQLAlchemy models for User, Resume, JobDescription
│   │── utils.py            # Resume parsing & matching logic (using PyPDF2, docx2txt)
│   │── email_service.py    # AWS SES email integration
│   │── db_init.py          # Script to initialize the database
│   │── requirements.txt    # Python dependencies
│   │── Dockerfile          # Docker configuration for backend
│
│── frontend/                  
│   │── pages/              # Next.js pages (index.js, upload.js, etc.)
│   │── components/         # React components (Navbar.js, Footer.js)
│   │── services/           # API helper (api.js)
│   │── styles/             # CSS files (globals.css)
│   │── package.json        # Node.js dependencies & scripts
│   │── Dockerfile          # Docker configuration for frontend
│
│── static/                 # Assets (images, e.g., logo.png, upload_icon.png)
│── docker-compose.yml      # Docker Compose orchestration for all services
│── README.md               # This file
```

## Setup & Deployment

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/resume-matcher.git
   cd resume-matcher
   ```

2. **Configure Environment Variables:**

   - **Backend:**  
     Edit `backend/config.py` and update the following:
     - `SQLALCHEMY_DATABASE_URI` — Adjust credentials and host if necessary.
     - `AWS_SES_REGION` — Set to your SES region (e.g., "us-east-1").
     - `AWS_SES_SENDER` — Use your verified sender email from AWS SES.

   - **Docker Compose:**  
     The `docker-compose.yml` file defines environment variables. Ensure the credentials and connection strings are set correctly for your environment.

3. **Build and Run Containers:**

   From the project root, run:
   ```bash
   docker-compose up --build
   ```
   This command will:
   - Build the backend and frontend Docker images.
   - Start a MySQL container with a persistent volume.
   - Start the backend API (Flask) on port 5000.
   - Start the frontend (Next.js) on port 3000 (mapped from container port 80).

4. **Access the Application:**

   - **Frontend:** Open `http://<your-aws-ip>:3000` in your browser.
   - **Backend API:** Accessible at `http://<your-aws-ip>:5000`.

## Database Setup

The MySQL container in `docker-compose.yml` is configured with:
- **Database:** `resume_matcher`
- **User:** `root`
- **Password:** `password`

Data is stored in the `db_data` Docker volume. To manually connect to the database:
```bash
docker exec -it <mysql_container_id> mysql -uroot -p
```
Then use the password `password` to log in.

## AWS SES Setup

1. **Verify Sender Email:**
   - Log in to the [AWS SES Console](https://console.aws.amazon.com/ses/).
   - Navigate to **Email Addresses** and verify your sender email.
   - Update `AWS_SES_SENDER` in `backend/config.py` with this verified email.

2. **Request Production Access (Optional):**
   - To send emails to unverified addresses, request production access in SES.

3. **Region Configuration:**
   - Ensure that `AWS_SES_REGION` in your `config.py` is set to the region where your SES is active.

## Configuration & File Changes

### Protected Settings & Environment Variables:
- **`backend/config.py`:**  
  - Update the MySQL connection string, AWS SES region, and sender email.
- **`docker-compose.yml`:**  
  - Ensure environment variables and connection details match your setup.

### Key Backend Files:
- **`backend/app.py`:** Contains API routes for resume upload, job description submission, and matching logic.
- **`backend/models.py`:** Defines database models for users, resumes, and job descriptions.
- **`backend/utils.py`:** Handles resume parsing and keyword matching.
- **`backend/email_service.py`:** Integrates with AWS SES to send match score emails.
- **`backend/db_init.py`:** Script to initialize database tables.
- **`backend/requirements.txt`:** Lists Python dependencies.

### Key Frontend Files:
- **`frontend/pages/index.js`:** Landing page with a modern UI.
- **`frontend/pages/upload.js`:** Handles resume and job description submission.
- **`frontend/services/api.js`:** Contains API call logic.
- **`frontend/components/Navbar.js`:** Navigation bar component.
- **`frontend/components/Footer.js`:** Footer component.
- **`frontend/styles/globals.css`:** Global CSS styles (updated for a professional look).
- **`frontend/package.json`:** Lists Node.js dependencies and scripts.

## Packages Installed on AWS Ubuntu Instance

**For Dockerized Deployment:**
- **Docker Engine:** Follow the [Docker Engine installation guide](https://docs.docker.com/engine/install/ubuntu/).
- **Docker Compose:** Follow the [Docker Compose installation guide](https://docs.docker.com/compose/install/).

**For Local Development:**
- **Git:** `sudo apt install git -y`
- **Node.js and npm:** `sudo apt install nodejs npm -y`

**Within Containers:**
- **Backend:** Installs Flask, Flask-SQLAlchemy, PyMySQL, PyPDF2, docx2txt, boto3 (as listed in `backend/requirements.txt`).
- **Frontend:** Installs Next.js, React, React-DOM, Axios, and Tailwind CSS (as listed in `frontend/package.json`).

## Docker Compose Orchestration

The `docker-compose.yml` file includes three services:
- **db:** MySQL container with a persistent volume.
- **backend:** Flask backend container (dependent on db).
- **frontend:** Next.js container (dependent on backend).

Example `docker-compose.yml` snippet:
```yaml
version: "3.8"

services:
  db:
    image: mysql:8
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: resume_matcher
      MYSQL_USER: root
      MYSQL_PASSWORD: password
    volumes:
      - db_data:/var/lib/mysql
    ports:
      - "3306:3306"

  backend:
    build: ./backend
    restart: always
    environment:
      SQLALCHEMY_DATABASE_URI: "mysql+pymysql://root:password@db/resume_matcher"
      SQLALCHEMY_TRACK_MODIFICATIONS: "False"
      AWS_SES_REGION: "us-east-1"
      AWS_SES_SENDER: "your-email@example.com"
    ports:
      - "5000:5000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    restart: always
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  db_data:
```

## Additional Notes

- **File Uploads:**  
  Uploaded resumes are stored in the `uploads/` directory inside the backend container. Consider using AWS S3 for production file storage.

- **Security:**  
  For production, update default credentials, secure environment variables, and use HTTPS.

- **Scaling:**  
  For a scalable architecture, consider AWS services like RDS for MySQL, ECS/EKS for container orchestration, and CloudFront for CDN.

- **Logging & Monitoring:**  
  Integrate with AWS CloudWatch or another monitoring tool to track performance and errors.

---

This comprehensive `README.md` provides detailed steps for deploying, configuring, and running the Resume Matcher Application on an AWS Ubuntu instance. If you have any questions or need further modifications, feel free to reach out!

Happy Coding!
```

---

Feel free to modify this file to suit your deployment environment and project specifics. Let me know if you need any further adjustments!