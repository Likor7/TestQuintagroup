# Test for Quintagroup

## Instructions for using

**Create python environment**

```
$ python3 -m venv .venv
```

**Activate python environment**

```
$ source .venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Create .env file (or just rename .env.sample to .env)**

## If you create .env file, that file must contain:

```
X_API_KEY=your_api_key_here
```
**Running the Application (without Docker Compose)**

```
python app.py
```

**Running the Application (with Docker Compose)**

```
sudo docker-compose up -d --build
```

```
docker-compose exec app /bin/bash
```

```
python app.py
```

## If want to choose your own workspace/project/task, you should uncomment the parts of code in app.py
