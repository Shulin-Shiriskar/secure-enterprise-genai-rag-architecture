FROM python:3.12-slim
WORKDIR /srv
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY scripts ./scripts
COPY sample_docs ./sample_docs
RUN python scripts/ingest.py
ENV RAG_DB_PATH=/srv/rag.db ANSWER_MODE=extractive PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
