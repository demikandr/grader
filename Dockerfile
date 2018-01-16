FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	python3-pip
RUN mkdir /build
WORKDIR /build
COPY . .

RUN pip3 install .

CMD python3 -m grader
