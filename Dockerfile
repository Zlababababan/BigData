FROM ubuntu

WORKDIR /usr/src/workspace
COPY . .
RUN apt-get -y update

RUN apt-get -y install python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y vim
RUN pip3 install -r requirements.txt
RUN ipykernel install --user
RUN git config --global user.name yayozor
RUN git config --global user.email yass27150@hotmail.fr
RUN git clone https://github.com/yayozor/BigData

EXPOSE 8000
CMD ["jupyter","notebook","--port=8000","--no-browser","--ip=0.0.0.0","--allow-root"]
