FROM golang:1.9-alpine

RUN apk add --no-cache --purge -uU python3 python3-dev gcc musl-dev git alpine-sdk libc-dev linux-headers
RUN mkdir -p /opt && cd /opt && git clone https://github.com/twosigma/locust-s3
RUN pip3 install -r /opt/locust-s3/requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN go get github.com/twosigma/locust-s3/locustfiles/go/locust-s3
RUN cd /opt/locust-s3
RUN LOCUST_CONFIG=/opt/locust-s3/config/getservicetest.yaml locust -f /opt/locust-s3/locustfiles/python/s3.py  --no-web -c 10 -r 10 -t 1s --only-summary -L WARNING --csv=/tmp/res.csv


