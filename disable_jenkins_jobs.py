
'''
@author: sumit
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
