run-kafka:
	docker-compose -f docker-compose.kafka.yml

run-services:
	docker-compose up --build