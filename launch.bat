docker build -t tests .
docker run --name tests_run --network my_network tests --executor %executor% --browser %browser% --url %opencart_address% -n %threads%
docker cp tests_run:/app/allure-results .
docker rm tests_run