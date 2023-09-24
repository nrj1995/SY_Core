pipeline {
    agent any

    stages {
        stage('stop Nginx') {
            steps {
                echo 'start stage'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'sy_web_server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '',
                                    execCommand: 
    '''
       sudo systemctl status nginx
       sudo systemctl stop nginx
    ''',
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: '',
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '')],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: false)])
            
                echo 'end stage'
                
            }
        }
        stage('update the code repo') {
            steps {
                echo 'start stage'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'sy_web_server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '',
                                    execCommand: 
    '''
       cd /home/ubuntu/SY_Core
       git pull
    ''',
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: '',
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '')],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: false)])
            
                echo 'end stage'
                
            }
        }
        stage('check for migration and migrate') {
            steps {
                echo 'start stage'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'sy_web_server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '',
                                    execCommand: 
    '''
       cd /home/ubuntu/SY_Core
       source sy_env/bin/activate
       cd MasterStoryyatra
       python manage.py makemigrations
       python manage.py migrate
       deactivate
    ''',
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: '',
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '')],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: false)])
            
                echo 'end stage'
                
            }
        }
        stage('collect static') {
            steps {
                echo 'start stage'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'sy_web_server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '',
                                    execCommand: 
    '''
       cd /home/ubuntu/SY_Core
       source sy_env/bin/activate
       cd MasterStoryyatra
       python manage.py collectstatic --noinput
       deactivate
       sudo systemctl daemon-reload
       sudo systemctl restart gunicorn
       sudo systemctl start nginx
    ''',
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: '',
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '')],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: false)])
            
                echo 'end stage'
                
            }
        }
        stage('restart gunicorn and ngnix') {
            steps {
                echo 'start stage'
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'sy_web_server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '',
                                    execCommand: 
    '''
       sudo systemctl daemon-reload
       sudo systemctl restart gunicorn
       sudo systemctl start nginx
    ''',
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: '',
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '')],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: false)])
            
                echo 'end stage'
                
            }
        }
    }
}

#testing pipline

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace 'your-git-repo-url' with the actual URL of your Git repository
                bat 'git clone https://github.com/nrj1995/SY_Core.git .'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create virtual environment and install requirements
                bat 'python -m venv test'
                bat '.\\test\\Scripts\\activate'
                bat 'pip install -r requirement.txt'
            }
        }

        stage('Migrate Database') {
            steps {
                // Run database migrations
                bat '.\\test\\Scripts\\activate '
                bat 'cd MasterStoryyatra && dir && python manage.py migrate &'
        
            }
        }

        stage('Collect Static Files') {
            steps {
                // Collect static files
                echo 'avoiding below step'
                //bat '.\\venv\\Scripts\\activate && python manage.py collectstatic --noinput'
            }
        }

        stage('Run Server') {
            steps {
            //   script {
            //         // Start your server here, replace 'your_server_start_command' with the actual command
            //         def serverProcess = bat(script: 'start /B python MasterStoryyatra/manage.py runserver', returnStatus: true)

            //         // Check if the server process is running
            //         if (serverProcess == 0) {
            //             currentBuild.description = 'Server started successfully.'
            //         } else {
            //             currentBuild.description = 'Failed to start the server.'
            //             error 'Failed to start the server.'
            //         }
            //     }
                bat '.\\test\\Scripts\\activate '
                bat 'cmd /c python MasterStoryyatra/manage.py runserver &'
                //sleep time: 10, unit: 'SECONDS'
                //bat 'taskkill /F /FI "WINDOWTITLE eq Django Server*"'
            }
        }
        stage('Delay') {
            steps {
                // Add a delay of 1 minute (60 seconds)
                echo 'will add if needed'
            }
        }
        
    }
    post {
            always {
            // Close the Django server after 5 minutes
            bat 'taskkill /F /IM "python.exe" /FI "WINDOWTITLE eq manage.py runserver*"'
            // Deactivate the virtual environment
            bat 'test\\Scripts\\deactivate'
            // Clean up workspace (delete repository and files)
            deleteDir()
           
             }
        }
        
}
