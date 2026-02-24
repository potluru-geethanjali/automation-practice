pipeline {
    agent any

    /* ==========================
       PARAMETERS
    ========================== */
    parameters {
        string(name: 'FILE_NAME',
               defaultValue: '05_python_datatypes.py',
               description: 'Enter Python file to execute')

        choice(name: 'ENV',
               choices: ['dev', 'qa', 'prod'],
               description: 'Select environment')

        booleanParam(name: 'ARCHIVE_LOGS',
                     defaultValue: true,
                     description: 'Archive log files?')
    }

    /* ==========================
       TRIGGERS
    ========================== */
    // triggers {
    //     // Nightly build at 2 AM
    //     cron('H 2 * * *')
    // }

    stages {

        stage("Print Environment Info") {
            steps {
                echo "Selected Environment: ${params.ENV}"
                echo "Selected File: ${params.FILE_NAME}"
            }
        }

        stage("Run Python Test") {
            steps {
                sh """
                cd /Users/geethanjali/Documents/IV_PREP/
                python3 ${params.FILE_NAME} > output.log
                """
            }
        }
    }

    /* ==========================
       ARTIFACTS
    ========================== */
   // post {
   //     always {
   //         script {
   //             if (params.ARCHIVE_LOGS) {
   //                 archiveArtifacts artifacts: '**/output.log',
   //                                  fingerprint: true
   //             }
   //         }
   //     }
   //  }
}
