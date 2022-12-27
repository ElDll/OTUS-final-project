pipeline {
  agent any
  parameters {
    string(defaultValue: '192.168.1.76', description: 'executor', name: 'executor')
  }

  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("tests", "-f Dockerfile .")
      	     }
          }
       }
    }

     stage('Run tests') {
        steps {
           catchError {
              script {
                 docker.image('aerokube/selenoid:1.10.8').withRun('-p 4444:4444')
                 docker.image('aerokube/selenoid-ui:dev-latest').withRun('-p 8080:8080')
          	     bat "docker run --name tests_run --network my_network tests --executor %executor%"
        	  }
      	   }
         }
     }

     stage('Copy allure-results') {
     steps {
           catchError {
              script {
          	     bat "docker cp tests_run:/app/allure-results ."
        	  }
      	   }
         }
     }

     stage("Delete container") {
        steps {
    	catchError {
      	   script {
        	      bat "docker rm tests_run"
      	     }
          }
       }
    }

     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'allure-results']]
    	   ])
  	        }
         }
     }
}