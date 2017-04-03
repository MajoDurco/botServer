SERVER_IMAGE='majodurco/slack_bot_server'
CLIENT_IMAGE='majodurco/slack_bot_client'

run: 
	docker-compose run client

init: clone pull getComposeFile

getComposeFile:
	curl --output docker-compose.yml https://raw.githubusercontent.com/MajoDurco/botServer/master/compose_file/docker-compose.yml

clone:
	git clone git@github.com:MajoDurco/botServer.git ;\
	git clone git@github.com:MajoDurco/botClient.git

pull:
	docker pull $(SERVER_IMAGE) && \
	docker pull $(CLIENT_IMAGE)

test:
	docker run $(SERVER_IMAGE) python3 server_test.py ;\
    docker run $(SERVER_IMAGE) python3 operat_test.py
