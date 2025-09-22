pipeline {
  agent any

  stages {
    stage('Build the Docker image') {
      steps {
          sh '''
          cd /Users/santhapriya/Documents/sampleprogram
          docker build -t test_script:v2 .
          '''
      }
    }

    stage('Run docker container') {
      steps {
          sh '''
	  docker run test_script:v2
	  '''
      }
    }
  }

  post {
    always {
      echo "Pipeline finished."
    }
  }
}
