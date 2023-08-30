pipeline {
  agent any
  stages {
    stage('in') {
      steps {
        echo 'we are in the jenkins'
        cleanWs(cleanWhenFailure: true, cleanWhenAborted: true, cleanWhenNotBuilt: true, cleanWhenUnstable: true, cleanWhenSuccess: true)
        pwd()
        dir(path: 'D:\\jenkinstest')
      }
    }

  }
}