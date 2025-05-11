---

# Django Video Uploader

**Django video uploader** is a simple Django-based web application that allows users to upload and view video files through a browser interface. It serves as a foundational project for learning Django’s file handling, form processing, and media management capabilities.

---

## 🚀 Features

* Upload video files via a web form
* Store uploaded videos in the server’s media directory
* Display uploaded videos using HTML5 video player
* Lightweight and beginner-friendly codebase([Stack Overflow][1], [Stack Overflow][2], [doprax.com][3])

---

## 🛠 Requirements

* Python 3.x
* Django 3.x or later([Stack Overflow][4])

---

## 📦 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bishesh910/DjangoVideoUploader.git
   cd DjangoVideoUploader/RPAvideo
   ```



2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```



5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```



6. **Access the application:**

   Open your browser and navigate to `http://127.0.0.1:8000/` to use the video uploader.

---

## 📁 Project Structure

```plaintext
RPAvideo/
├── manage.py
├── RPAvideo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── uploader/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── upload.html
├── media/
└── requirements.txt
```



---

## 📝 Notes

* Uploaded videos are stored in the `media/` directory.
* Ensure that the `MEDIA_URL` and `MEDIA_ROOT` settings in `settings.py` are configured to serve media files correctly during development.


---
