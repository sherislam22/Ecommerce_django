FROM python:3.10.2

ENV PYTHONPATH 1

WORKDIR /core
ADD  ./apps /core/
RUN pip3 install virtualenv
RUN virtualenv env -p python3
RUN source env/bin/activate


RUN /usr/local/bin/python -m pip install --upgrade pip 


RUN pip3 install -r requirements.txt

RUN cd core
