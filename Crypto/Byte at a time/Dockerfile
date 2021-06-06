FROM python:3.8-slim-buster
RUN apt update 
RUN apt install -y gcc python3-dev
RUN pip install flask pycryptodome  
WORKDIR /app
COPY server.py /app
COPY secret.py /app
EXPOSE 8000 
ENTRYPOINT [ "python" ] 
CMD [ "server.py" ]