pipeline {
  agent any
  stages {
    stage('Build Docker') {
      steps {
        sh '''
          cd service-a
          docker build -t service-a .
          docker tag service-a <your-ecr-url>/service-a:latest
          aws ecr get-login-password | docker login --username AWS --password-stdin <your-ecr-url>
          docker push <your-ecr-url>/service-a:latest
        '''
      }
    }
    stage('Deploy') {
      steps {
        sh '''
          aws ecs register-task-definition --cli-input-json file://service-a/ecs-task-def.json

          aws deploy create-deployment \
            --application-name service-a \
            --deployment-group-name service-a-bluegreen \
            --deployment-config-name CodeDeployDefault.ECSAllAtOnce \
            --s3-location bucket=your-bucket,bundleType=zip,key=service-a.zip
        '''
      }
    }
  }
}
