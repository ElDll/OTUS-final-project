docker build -t tests .
docker run --name tests_run --network my_network tests --executor {$executor}
docker cp tests_run:/app/allure-results .
docker rm tests_run