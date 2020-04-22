To start a MongoDB server on Docker, enter the following:
$docker run -d -p 27017:27017 mongo:3.2.20-jessie
$docker container list
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
4c6706af399b mongo:3.2.20-jessie "docker-entrypoint.s..." About a minute ago Up About a minute 0.0.0.0:27017->27017/tcp silly_ardinghelli

To run the application
----------------------

```
./init.sh
source venv/bin/activate
export FLASK_APP=main.py
flask run
```
