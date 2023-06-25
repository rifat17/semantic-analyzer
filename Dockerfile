FROM python:3.11-slim-bookworm

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('wordnet')"
RUN python -c "import nltk; nltk.download('stopwords')"

COPY . .

EXPOSE 5000

ENV FLASK_APP=app/api/app.py

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
