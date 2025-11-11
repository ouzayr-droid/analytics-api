# download and install python
FROM python:3.13.9

# setup linux os packages
# create a virtual environment
# install python packages
# FastAPI Hello World 
# codingforentrepreneurs.com/blog/deploy-fastapi-to-railway-with-this-dockerfile/
# à la 59ème ligne, juste au dessus de RUN chmod+x paracord_runner.sh ajouter la ligne
#        COPY ./boot/docker-run.sh /opt/run.sh
# remplacer tous les paracord_runner.sh par /opt/run.sh