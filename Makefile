SERVER="slackServer"
IMAGE="majodurco/slack_bot_server"

run: 
	docker run -d --name=$(SERVER) $(IMAGE)

kill:
	docker kill $(SERVER)

clean: kill
	docker rm $(SERVER)

test:
	docker run $(IMAGE) python3 server_test.py ;\
	docker run $(IMAGE)	python3 operat_test.py
