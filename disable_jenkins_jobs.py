
'''
@author: sumit
This script will disable all Jenkins jobs present in the Jenkins home directory.
For this it become active we do need to reload all configuration from disk once the script has run.
To reload configuration go to Jenkins -> Manage Jenkins -> Reload Configuration from Disk
OR
Restart Jenkins
'''
import os
from subprocess import *

import xml.etree.ElementTree as ET

class DisableJenkinsJobs():

    def disableAllJenkinsJobs(self):

        jenkinsJobDirectory = "/usr/lib/jenkins/jobs/" #This is the home directory of Jenkins

        for root, dirs, files in os.walk(jenkinsJobDirectory):
            for file in files:
                if file.endswith('config.xml'):
                    full_path_file = (os.path.join(root, file))
                    tree = ET.parse(full_path_file)
                    root = tree.getroot()

                    for disabled in root.findall('disabled'):
                        disabled.text = "true"

                    # this needs SUDO access so run the script with sudo permission
                    tree.write(full_path_file)

JenkinsObject = DisableJenkinsJobs()
JenkinsObject.disableAllJenkinsJobs()
