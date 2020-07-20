FROM python:3.8-alpine
LABEL maintainer="nguyen.ensma@gmail.com"
#Install dependencies
RUN pip install Django==3.0.8 && \
    apk add --no-cache jpeg-dev zlib-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers && \
    pip install Pillow==7.2.0
#Add source
COPY manage.py /app/manage.py
COPY mySite /app/mySite
COPY PhotoLab /app/PhotoLab
COPY LICENSE /app/LICENSE
#BUILD
RUN cd /app && \
    export PATH="/root/anaconda3/bin:${PATH}" && \
    python manage.py migrate && \
    python manage.py makemigrations PhotoLab
WORKDIR /app
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0:8080"]
