FROM python:2.7
COPY . /opt/ubicajeros
WORKDIR /opt/ubicajeros
RUN pip install -r requirements.txt && pip install -e .
CMD python ubicajeros/api.py
