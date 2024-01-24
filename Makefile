build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

clean:
	@rm -rf backend/src/csv/
	@rm -f */**/download_data*
	@rm -f */**/*~

re: down build up logs
