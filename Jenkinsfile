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
          	     docker.run("--name tests_run", "--network my_network", "tests", "--executor %executor%")
        	     }
      	    }
         }
     }

     stage("Delete container") {
        steps {
    	catchError {
      	   script {
        	      docker.build("-t tests .")
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