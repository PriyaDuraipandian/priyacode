pipeline {
  agent any

  stages {
    stage('Prepare') {
      steps {
        sh '''
          echo "Using Python version:"
          python3 --version || python --version
          ls -l
        '''
      }
    }

    stage('Run sample script') {
      steps {
        sh 'python3 sample_script.py'
      }
    }
  }

  post {
    always {
      echo "Pipeline finished."
    }
  }
}
