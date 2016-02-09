#!/usr/bin/env python

'''


Author : Sebasien Boyer
Date : Feb 2016

Launch complete pipeline 
FROM : log data in the COURSE FOLDER
TO : MYSQL database in MOOCdb format

use example:
python full_pipe.py FOLDER/ COURSE_NAME COURSE_PREFIX

'''


# from subprocess import check_output
import subprocess

import argparse



JSON_TO_CSV_SCRIPT = 'import.openedx.apipe/scripts/transformGivenLogfiles.sh'


if __name__ == "__main__":



    ############  Parse arguments

    parser = argparse.ArgumentParser()
    
    parser.add_argument("folder",help='Folder where the course folder lie',type=str)
    parser.add_argument("course_name",help='Name of the course (should be the name as the name of the course folder ',type=str)
    parser.add_argument("prefix",help='The prefix used as names for the log data',type=str)

    args = parser.parse_args()

    ################################################################
    ############  Create environment for log data translation
    ################################################################

    print "********  Creating environment **********"

    cmd_queue = []

    ## Create directories
    LOG_DATA = ''.join([args.folder,args.course_name,'/log_data/'])
    INT_CSV = ''.join([args.folder,args.course_name,'/intermediary_csv/'])
    MOOC_CSV = ''.join([args.folder,args.course_name,'/moocdb_csv/'])

    cmd_queue.append(' '.join(['mkdir',LOG_DATA]))
    cmd_queue.append(' '.join(['mkdir',INT_CSV]))
    cmd_queue.append(' '.join(['mkdir',MOOC_CSV]))

    ## Move and Unzip Json files
    LOG_FILES = ''.join([args.folder,args.course_name,'/',args.prefix,'*'])
    cmd_queue.append(' '.join(['mv',LOG_FILES,LOG_DATA[:-1]]))  # don't include /
    JSON_FILE = ''.join([LOG_DATA,args.prefix,'___tracking_log.json.gz'])
    cmd_queue.append(' '.join(['gzip','-d',JSON_FILE]))

    # for cmd in cmd_queue:
    #     subprocess.call(cmd, shell=True)


    ################################################################
    ############  Launch APIPE (translation from json to intermediary csv)
    ################################################################

    print "********  Translating from json to csv **********" 
    cmd_queue = []

    JSON_FILE = ''.join([LOG_DATA,args.prefix,'___tracking_log.json'])
    cmd_queue.append(' '.join(['bash',JSON_TO_CSV_SCRIPT,INT_CSV,JSON_FILE]))

    # for cmd in cmd_queue:
    #     subprocess.call(cmd, shell=True)

    ################################################################
    ############ Launch QPIPE
    ################################################################

    print "********  Transform csv and populate MYSQL Table **********" 




