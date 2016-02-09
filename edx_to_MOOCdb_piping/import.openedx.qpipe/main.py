# Author : Sebastien Boyer  (sebboyer@mit.edu)

import sys
import os 
import extractor
import config as cfg

from events import *
from resources import *
from eventformatter import *
from eventmanager import *
from helperclasses import *
from submissions import *
from util import * 
from moocdb import MOOCdb

import sys
sys.path.insert(0, '/home/sebboyer/port/Translation_software/MOOCdb_curation')
import sql_functions
import mysql.connector
from mysql.connector.constants import ClientFlag
import main


# For monitoring
# from pdb import set_trace as bp
import pdb
from subprocess import check_output
from subprocess import call



# pdb.set_trace()

ROOT_DIR = os.getcwd()
MOOCDB_DIR = cfg.DEST_DIR
CONFIG_DIR = ROOT_DIR + '/config/'

# Log file, best viewed with emacs org-mode
LOG = cfg.LOG_FILE
sys.stdout = open(LOG, 'w+')

# File to pretty print resource hierarchy
HIERARCHY = cfg.RESOURCE_HIERARCHY
PB_HIERARCHY = cfg.PROBLEM_HIERARCHY

# MOOCdb storage interface
# TODO Apply branching to allow different options
moocdb = MOOCdb(MOOCDB_DIR)

# Instanciating the piping architecture
event_formatter = EventFormatter(moocdb, CONFIG_DIR)
resource_manager = ResourceManager(moocdb, HIERARCHY_ROOT='https://', CONFIG_PATH = CONFIG_DIR)
event_manager = EventManager(moocdb)
submission_manager = SubmissionManager(moocdb)
curation_helper = CurationHelper(MOOCDB_DIR)

print '**Processing events**' 

########## For testig only
print cfg.EDX_TRACK_EVENT
n_rows=check_output(["wc", "-l",cfg.EDX_TRACK_EVENT])
n_rows=n_rows.split(" ")
n_rows=int(n_rows[7])   # 0 for linux systems   / 7 for MacOS systems
ind_event=0
##########

Extract=extractor.get_events()

for raw_event in Extract:

    # For testing only
    ind_event+=1
    if ind_event%500==0:
        print ' Completed : ', 100*float(ind_event)/float(n_rows),'%'

    # Shut down for debug
    # print '* Processing event #' + raw_event['event_id'] + ' @ ' + raw_event['page']
    # print '** Applying filter'

    # Apply event filter
    if event_formatter.pass_filter(raw_event) == False:
        # print 'Event filtered out' # Shut down for debug
        continue
            
    # Format raw event and instanciate corresponding Event subclass
    event = event_formatter.polish(raw_event)
    # print '- Instanciated event :: ' + event['event_type'] + '->' + event.__class__.__name__
    
    # Inserts resource into the hierarchy
    # print '** Inserting resource' # Shut down for debug
    resource_id = resource_manager.create_resource(event)
    event.set_data_attr('resource_id', resource_id)

    # Store submission, assessment and problem
    submission_manager.update_submission_tables(event)

    # Record curation hints
    curation_helper.record_curation_hints(event)

    # Store observed event
    event_manager.store_event(event)

print '* All events processed'
print '** Writing CSV output to : ' + MOOCDB_DIR

event_formatter.serialize()
event_manager.serialize()
resource_manager.serialize(pretty_print_to=HIERARCHY)
submission_manager.serialize(pretty_print_to=PB_HIERARCHY)
curation_helper.serialize()

print '* Writing resource hierarchy to : ' + HIERARCHY
print '* Writing problem hierarchy to : ' + PB_HIERARCHY
# Close all opened files
moocdb.close()


########## Move file to desired location (accessible from MYSQL DB)
print 'Move csv files to /tmp folder (accessible from MYSQL)'
script='/home/sebboyer/port/Translation_software/edx_to_MOOCdb_piping/import.openedx.qpipe/'+'move_csv.sh'
check_output(['sh',script,cfg.COURSE_NAME])


########################## Create MYSQL DATABASE
print 'Creating MYSQL Database : '+cfg.COURSE_NAME

def execute(cnx,cmd):
    try:
        sql_functions.executeSQL(cnx,cmd)
    except mysql.connector.Error as err:
        print err
        exit(1)

usernameSQL = input('Enter your username for mySQL Database : ')
passSQL = input('Enter corresponding password : ')

## Create the .sql script for DB creation
fileName='create_mysqlDB.sql'
toBeReplaced=['COURSE_NAME']
replaceBy=[cfg.COURSE_NAME]
cmd=sql_functions.replaceWordsInFile(fileName,toBeReplaced, replaceBy)
cnx = mysql.connector.connect(user=usernameSQL,password=passSQL)
execute(cnx,cmd)


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

dbName = cfg.COURSE_NAME
userName = usernameSQL
passwd = passSQL
dbHost = 'alfa6.csail.mit.edu'
dbPort = 3306
startDate = cfg.COURSE_START_DATE

# Postprocesing scripts :
# 0 = initial_preprocessing.sql
# 1 = add_submissions_validity_column.sql
# 2 = problems_populate_problem_week.sql
# 3 = users_populate_user_last_submission_id.sql

scripts = [0,1,2,3]   

main.curate(dbName = dbName, userName=userName, passwd=passwd, dbHost=dbHost, dbPort=dbPort, startDate=startDate,scripts=scripts)



print "Curating MYSQL database : "+cfg.COURSE_NAME

usernameSQL = 'sebboyer'
passSQL = '37d(b08F'
dbName = '203_test'
userName = usernameSQL
passwd = passSQL
dbHost = 'alfa6.csail.mit.edu'
dbPort = 3306
startDate = '2012-03-05 12:00:00'
scripts = [0,1,2,3]   








