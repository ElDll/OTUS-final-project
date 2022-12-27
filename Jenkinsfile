pipeline {
  agent any
  parameters {
    string(defaultValue: '-m "not need_admin_url"', description: 'mark', name: 'mark')
    string(defaultValue: '192.168.1.76', description: 'executor', name: 'executor')
    string(defaultValue: 'http://192.168.1.76:8081', description: 'url', name: 'url')
    string(defaultValue: '1', description: 'threads', name: 'threads')
    string(defaultValue: 'chrome', description: 'browser', name: 'browser')
    string(defaultValue: '104', description: 'bv', name: 'bv')
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

    stage('Run opencart') {
        steps {
           catchError {
              script {
                     bat "docker-compose up -d"
        	  }
      	   }
        }
     }

     stage('Configure selenoid') {
        steps {
           catchError {
              script {
                     bat "cm_windows_amd64.exe selenoid start --port 4444"
                     bat "cm_windows_amd64.exe selenoid-ui start --port 8080"
                     bat "docker network connect pipe_test_my_network selenoid"
                     bat "docker network connect pipe_test_my_network selenoid-ui"
        	  }
      	   }
        }
     }

     stage('Run tests') {
        steps {
           catchError {
              script {
                     bat "docker run --name tests_run --network pipe_test_my_network tests %mark% --executor %executor% --url %url% -n %threads% --browser %browser% --bv %bv%"
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

     stage('Stop selenoid') {
     steps {
           catchError {
              script {
          	     bat "cm_windows_amd64.exe selenoid stop"
          	     bat "cm_windows_amd64.exe selenoid-ui stop"
        	  }
      	   }
         }
     }

     stage("Stop opencart") {
        steps {
    	catchError {
      	   script {
        	      bat "docker-compose down"
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