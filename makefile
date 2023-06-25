run:
	docker-compose up --build -d

test:
	docker-compose run --rm analyzer python -m pytest app/tests/

# lint:
# 	docker-compose run --rm analyzer flake8 app

black:
	docker-compose run --rm analyzer black app


build-server:
	@echo "Building server..."
	docker run --rm -u `id -u`:`id -g` -v ${PWD}:/local openapitools/openapi-generator-cli \
		generate \
		-i /local/analyzer.yaml \
		-g python-flask \
		-o /local/server
	@echo "Done"

build-client:
	@echo "Building client..."
	docker run --rm -u `id -u`:`id -g` -v ${PWD}:/local openapitools/openapi-generator-cli \
		generate \
		-i /local/analyzer.yaml \
		-g python \
		-o /local/client
	@echo "Done"