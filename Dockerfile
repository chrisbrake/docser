FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY . /tmp/
RUN apk add g++ make && \
    cd /tmp && \
    pip install --no-cache-dir -r requirements.txt && \
    python setup.py install
CMD [ "python", "-m", "docser" ]