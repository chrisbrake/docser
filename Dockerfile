FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY . ./
RUN apk add g++ make && pip install --no-cache-dir -r requirements.txt
CMD [ "python", "-m", "docser" ]