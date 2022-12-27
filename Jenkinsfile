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

//     stage('Create network') {
//         steps {
//            catchError {
//               script {
//                      bat "docker network create my_network"
//         	  }
//       	   }
//         }
//      }

     stage('Configure selenoid') {
        steps {
           catchError {
              script {
                     bat "cm_windows_amd64.exe selenoid start --port 4444"
                     bat "cm_windows_amd64.exe selenoid-ui start --port 8080"
                     bat "docker network connect my_network selenoid"
                     bat "docker network connect my_network selenoid-ui"
        	  }
      	   }
        }
     }

     stage('Run tests') {
        steps {
           catchError {
              script {
                     bat "docker"
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

     stage('Delete network') {
     steps {
           catchError {
              script {
          	    bat "docker network rm my_network"
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