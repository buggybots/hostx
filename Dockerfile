FROM ubuntu:16.04
# MAINTANER Your Name "youremail@domain.tld"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 80
RUN mkdir ~/.streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["happ.py"]


# Prasoon shared
# FROM ubuntu:16.04
# MAINTANER Your Name "youremail@domain.tld"
# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev
# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt
# COPY . /app
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]