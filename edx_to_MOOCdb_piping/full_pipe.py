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
import sys
import argparse
import os




JSON_TO_CSV_SCRIPT = 'import.openedx.apipe/scripts/transformGivenLogfiles.sh'






def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


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

    question = 'Do you want to create folder environment for Log transformation ?'


    if query_yes_no(question):
        print "********  Creating environment **********"

        cmd_queue = []

        ## Create directories
        LOG_DATA = ''.join([args.folder,args.course_name,'/log_data/'])
        INT_CSV = ''.join([args.folder,args.course_name,'/intermediary_csv/'])
        MOOC_CSV = ''.join([args.folder,args.course_name,'/moocdb_csv/'])

        if os.path.isdir(LOG_DATA[:-1]) or os.path.isdir(INT_CSV[-1]) or os.path.isdir(MOOC_CSV[-1]):
            print "Careful : folder already exist !"
            print "Didn't touch them."
        else :
            cmd_queue.append(' '.join(['mkdir',LOG_DATA]))
            cmd_queue.append(' '.join(['mkdir',INT_CSV]))
            cmd_queue.append(' '.join(['mkdir',MOOC_CSV]))

        ## Move and Unzip Json files
        LOG_FILES = ''.join([args.folder,args.course_name,'/',args.prefix,'*'])
	print LOG_FILES
        if os.path.exists(LOG_FILES):
            cmd_queue.append(' '.join(['mv',LOG_FILES,LOG_DATA[:-1]]))  # don't include /
        else:
            print "No such file : ",LOG_FILES

        JSON_FILE = ''.join([LOG_DATA,args.prefix,'___tracking_log.json.gz'])
        print JSON_FILE
	if os.path.exists(JSON_FILE):
            cmd_queue.append(' '.join(['gzip','-d',JSON_FILE]))
        else:
            print "No such file : ",LOG_FILES
        

        for cmd in cmd_queue:
            subprocess.call(cmd, shell=True)


    ################################################################
    ############  Launch APIPE (translation from json to intermediary csv)
    ################################################################

    question = 'Do you want to translate log files into csv ?'
    
    if query_yes_no(question):

        print "********  Translating from json to csv **********" 
        cmd_queue = []

        JSON_FILE = ''.join([LOG_DATA,args.prefix,'___tracking_log.json'])
        cmd_queue.append(' '.join(['bash',JSON_TO_CSV_SCRIPT,INT_CSV,JSON_FILE]))

        for cmd in cmd_queue:
            subprocess.call(cmd, shell=True)

    ################################################################
    ############ Launch QPIPE
    ################################################################

    question = 'Do you want to create folder environment for Log transformation ?'

    if query_yes_no(question):

        print "********  Transform csv and populate MYSQL Table **********" 




