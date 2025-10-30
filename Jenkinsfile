pipeline {
    agent any
    
    environment {
        // MLflow tracking sunucusu
        MLFLOW_TRACKING_URI = 'http://localhost:5000'
        // Python sanal ortam yolu
        VENV_PATH = "${WORKSPACE}/venv"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Kod repository\'den çekiliyor...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Python sanal ortamı kuruluyor...'
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv ${VENV_PATH}
                            . ${VENV_PATH}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv %VENV_PATH%
                            call %VENV_PATH%\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Train Model') {
            steps {
                echo 'Model eğitiliyor ve MLflow\'a kaydediliyor...'
                script {
                    if (isUnix()) {
                        sh '''
                            . ${VENV_PATH}/bin/activate
                            python src/train.py 100 10
                        '''
                    } else {
                        bat '''
                            call %VENV_PATH%\\Scripts\\activate.bat
                            python src\\train.py 100 10
                        '''
                    }
                }
            }
        }
        
        stage('Test Model') {
            steps {
                echo 'Model test ediliyor...'
                echo 'Test başarılı! (Gerçek projede test scriptleri eklenebilir)'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline başarıyla tamamlandı! Model MLflow\'a kaydedildi.'
            echo 'MLflow UI: http://localhost:5000'
        }
        failure {
            echo 'Pipeline başarısız oldu! Logları kontrol edin.'
        }
        always {
            echo 'Pipeline tamamlandı.'
        }
    }
}