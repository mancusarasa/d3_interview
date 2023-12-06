FROM python:3.9

RUN mkdir -p /root/d3_project
WORKDIR /root/d3_project
ADD . ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Run migrations and start the server
RUN ./manage.py makemigrations
RUN ./manage.py migrate

# Default entrypoint
ENTRYPOINT ./manage.py runserver 0.0.0.0:$API_PORT
