##  build for env
#FROM python:3.8
#WORKDIR /app
#COPY requirements.txt .
#RUN python -m pip install -U pip && \
#    python -m pip install -Ur requirements.txt

FROM awesomepayne/collector_appliance:v1
WORKDIR /code
COPY . .
CMD ["supervisord","-c", "supervisord.conf"]