run-kafka:
	docker-compose -f docker-compose.kafka.yml up

run-services:
	docker-compose up --build