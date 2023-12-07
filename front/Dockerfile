FROM ultralytics/ultralytics:latest-cpu

COPY requirements.txt requirements.txt
COPY best.pt best.pt
COPY crop_labeled.csv crop_labeled.csv

RUN pip install --upgrade pip

COPY fast.py fast.py
COPY fish.py fish.py

RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 8000

CMD uvicorn fast:app --host 0.0.0.0 --port 8000
