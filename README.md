# About

* A cron script that calls the YouTube API continuously in background every 60 seconds for fetching the latest videos for a predefined search query and stores the data of videos (Video title, description, publishing datetime, thumbnails URLs ) in the database.
* A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime
* A basic search API to search the stored videos using their title and description.




# Languages & Tools

* Python, Django, Django-Rest-Framework(DRF)
* MYSQL


# Django app setup guidelines 🚀

### Development Environment Setup: LINUX

---


**Step 1**: Fork the Repository

<br>
Click on <a href="#" target="_self"></a> to fork <a href="https://github.com/akhil484/fampay">this</a> repsository


---

**Step 2**: Creating Project Directory

<br>

```bash
cd desktop
mkdir myprojects
cd myprojects
```


---


**Step 3**: Cloning Repository using Git

<br>

```bash
git clone https://github.com/'<your-github-username>'/fampay.git
```


---


**Step 4**: Change directory to yt

<br>

```bash
cd yt
```


---


**Step 5**: Creating Virtual Environment

<br>
Install virtualenv
<br><br>

```bash
python3.8 -m venv projectenv
```

To Activate `virtual environment`

```bash
cd projectenv/bin
source activate
```

To deactivate `virtual environment`

```bash
deactivate
```

---


**Step 6**: Installing Requirements

<br>
Note: Before installing requirements, Make sure Virtual Environment is activated.
<br><br>

```bash
pip install -r requirements.txt
```


---


**Step 7**: Making database migrations

<br>

```bash
python manage.py makemigrations
python manage.py migrate
```


---


---

**Step 8**: Running the Project in local server

<br>
<b>Note:</b> Before running the project in local server, Make sure you activate the Virtual Environment.
<br><br>

```bash
python manage.py runserver
```
<br/>

---

<br>

--- 






