docker build -t tests .
docker run --rm --name tests_run --network my_network tests
docker cp tests_run:/app/allure-results .