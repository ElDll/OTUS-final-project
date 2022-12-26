pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("-t tests .")
      	     }
          }
       }
    }

     stage('Run tests') {
        steps {
           catchError {
              script {
          	     docker.run("--name tests_run --network my_network tests --executor %executor% --browser %browser% --url %opencart_address% -n %threads% --bv %bv%")
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