FROM python:3.12.8-bookworm
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD python3 start.py