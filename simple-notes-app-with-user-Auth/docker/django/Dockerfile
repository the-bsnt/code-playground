#set base image
FROM python:3.10-slim-bookworm

#set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=notes_project.settings

#set working directory 
ENV APP_HOME=/app
WORKDIR $APP_HOME

#install system dependencies 
RUN apt-get update\
    && apt-get install -y --no-install-recommends\
    build-essential\
    postgresql \
    libpq-dev \
    gcc\
    && apt-get clean\
    &&rm -rf /var/lib/apt/lists/*

#install and upgrade python pip 
RUN pip install --upgrade pip 

#copy requirements.txt file and install python packages
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip install -r requirements.txt

#copy project files to container 
COPY . $APP_HOME

# expose port that app listens to 
EXPOSE 8000


#copy and configure entry scripts
COPY ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint




#set Entrypoint

ENTRYPOINT [ "/entrypoint" ]



COPY ./start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start
# CMD [ "scripts.sh" ]






