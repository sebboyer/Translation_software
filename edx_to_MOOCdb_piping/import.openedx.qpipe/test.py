import config as cfg

# Import general lib
import sys
import os 
import extractor
import config as cfg

# Import transformation related scripts
from events import *
from resources import *
from eventformatter import *
from eventmanager import *
from helperclasses import *
from submissions import *
from util import * 
from moocdb import MOOCdb

## Import CUration related scripts
import sys
sys.path.insert(0, cfg.CURATION_DIR)
import sql_functions
import mysql.connector
from mysql.connector.constants import ClientFlag
import main


# For monitoring
import pdb
from subprocess import check_output
from subprocess import call

ROOT_DIR = os.getcwd()
MOOCDB_DIR = cfg.DEST_DIR
CONFIG_DIR = ROOT_DIR + '/config/'

# Log file, best viewed with emacs org-mode
#LOG = cfg.LOG_FILE
#sys.stdout = open(LOG, 'w+')

# File to pretty print resource hierarchy
HIERARCHY = cfg.RESOURCE_HIERARCHY
PB_HIERARCHY = cfg.PROBLEM_HIERARCHY

from subprocess import check_output

###############################################################################
################################ MYSQL DATABASE CREATION AND CURATION
###############################################################################
print '****** Create and Curate MYSQL db from csv files *******' 


########################## Create MYSQL DATABASE

dbName = cfg.COURSE_NAME
usernameSQL =str(sys.argv[1])# input('Enter your username for mySQL Database : ')
passSQL = sys.argv[2] #input('Enter corresponding password : ')
dbHost = cfg.MYSQL_HOST
dbPort = cfg.MYSQL_PORT
startDate = cfg.COURSE_START_DATE

print 'Creating MYSQL Database : '+dbName


def execute(cnx,cmd):
    try:
        sql_functions.executeSQL(cnx,cmd)
    except mysql.connector.Error as err:
        print err
        exit(1)


## Create the .sql script for DB creation
fileName='create_mysqlDB.sql'
toBeReplaced=['COURSE_NAME']
replaceBy=['201_test']#[cfg.COURSE_NAME]
cmd=sql_functions.replaceWordsInFile(fileName,toBeReplaced, replaceBy)
print cmd
#cnx = mysql.connector.connect(user=usernameSQL,password=passSQL,host=dbHost, port=dbPort)
#execute(cnx,cmd)


########################## FILL MYSQL DATABASE
print 'Filling MYSQL Database : '+cfg.COURSE_NAME+' with csv files data'

## Create the .sql script for DB creation
fileName='copy_to_mysqlDB.sql'
toBeReplaced=['COURSE_NAME']
replaceBy=[cfg.COURSE_NAME]
cmd=sql_functions.replaceWordsInFile(fileName,toBeReplaced, replaceBy)
copy_name="copy_to_mysqlDB_"+cfg.COURSE_NAME+".sql"
copy_script = open(copy_name, "w")
copy_script.write(cmd)
copy_script.close()
shell_cmd="mysql -u "+usernameSQL+" --password='"+passSQL+"' --local-infile < "+copy_name
call(shell_cmd,shell=True)
os.remove(copy_name) # not tested


######################## CURATION of the MYSQL DB 
print "Curating MYSQL database : "+cfg.COURSE_NAME

# Postprocesing scripts :
# 0 = initial_preprocessing.sql
# 1 = add_submissions_validity_column.sql
# 2 = problems_populate_problem_week.sql
# 3 = users_populate_user_last_submission_id.sql

scripts = [0,1,2,3]   

#main.curate(dbName = dbName, userName=userName, passwd=passwd, dbHost=dbHost, dbPort=dbPort, startDate=startDate,scripts=scripts)
