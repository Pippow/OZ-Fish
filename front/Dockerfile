FROM ultralytics/ultralytics:latest-cpu

COPY requirements.txt requirements.txt
COPY best.pt best.pt
COPY crop_labeled.csv crop_labeled.csv

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY fast.py fast.py
COPY fish.py fish.py
COPY crop_model.keras crop_model.keras
COPY arial.ttf arial.ttf
EXPOSE 8000

CMD uvicorn fast:app --host 0.0.0.0 --port 8000
