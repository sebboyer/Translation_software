'''
Config file :
- INPUT : to be changed according to the course to translate
- PARAMETER INITIALIZATION : initialize global var 

Last updated :
Sebastien Boyer (sebboyer@mit.edu)

Date : Feb 2016

'''


###############################################################################
############################### INPUT 
###############################################################################


## COURSE INFORMATION
COURSE_NAME = 'mitx-3.086x-2013-sond'
COURSE_START_DATE = '2013-16-09 12:00:00' # The format is '2012-03-05 12:00:00'
DIR = '/home/sebboyer/port/data_copy/'
CSV_PREFIX = 'MITx-3.086x-2013_SOND___2014_08_17___tracking_log.json.2016-03-09T12_29_48.037470_13848.sql'

TRANS_DIR = '/home/sebboyer/port/Translation_software/'
MYSQL_HOST = 'alfa6.csail.mit.edu'
MYSQL_PORT = 3306


###############################################################################
################################ PARAMETER INITIALIZATION
###############################################################################

# Configuration file
import re

## Input source
## Can be either 'csv', 'sql' or 'json'
INPUT_SOURCE = 'csv'
QUOTECHAR = "'" 
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
# MIT courses : %Y-%m-%dT%H:%M:%S.%f
# Stanford Courses : %Y-%m-%d %H:%M:%S

CSV_SOURCE_DIR = ''.join([DIR, COURSE_NAME, '/intermediary_csv/'])

EDX_TRACK_EVENT = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_EdxTrackEventTable.csv'])
CORRECT_MAP = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_CorrectMapTable.csv'])
ANSWER = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_AnswerTable.csv'])

## Output files
DEST_DIR = ''.join([DIR, COURSE_NAME, '/moocdb_csv/'])

### Hierarchy pretty prints
RESOURCE_HIERARCHY = DEST_DIR + 'resource_hierarchy.org'
PROBLEM_HIERARCHY = DEST_DIR + 'problem_hierarchy.org' 

### MOOCdb CSV tables
OBSERVED_EVENTS = DEST_DIR + 'observed_events.csv'
RESOURCES = DEST_DIR + 'resources.csv'
RESOURCES_URLS = DEST_DIR + 'resources_urls.csv'
URLS = DEST_DIR + 'urls.csv'
RESOURCE_TYPES = DEST_DIR + 'resource_types.csv'
PROBLEMS = DEST_DIR + 'problems.csv'
SUBMISSIONS = DEST_DIR + 'submissions.csv'
ASSESSMENTS = DEST_DIR + 'assessments.csv'
PROBLEM_TYPES = DEST_DIR + 'problem_types.csv'
OS = DEST_DIR + 'os.csv'
AGENT = DEST_DIR + 'agent.csv'

### Log file
VERBOSE = True
LOG_FILE = DEST_DIR + 'log.org'

## Specific formatting variables
# DOMAIN = 'https://www.edx.org'
DOMAIN = 'https://www.edx.org'

## Course URL parsing
IS_URL = re.compile('^(/|http)')
DOUBLE_SLASH = '(?<!:)//.*$'
PARAMETERS = '((undefined)?\?.*$)'
ANCHOR = '(#|\+|;|\$|\[).*$'
MODULE = '((answer|solution)[^/]*$)'
MISSING_TRAILING_SLASH = '(?<!/)$'
GET_DOMAIN = re.compile('(?P<domain>^.+://[^/]+)')
COURSEWARE = re.compile('courseware/(?P<unit>[^/]+)?/?(?P<subunit>[^/]+)?/?(?P<seq>\d{1,2})?')
BOOK = re.compile('book/(?P<booknum>\d{1,2})/(?P<page>\d{1,4})?')

############## MYSQL setting

CSV_SOURCE = DIR + COURSE_NAME + '/moocdb_csv'
CSV_DEST = '/tmp/' + COURSE_NAME 


############# Curation settings 
MAX_DURATION_SECONDS = 3600
DEFAULT_DURATION_SECONDS = 100 
CURATION_DIR = ''.join([TRANS_DIR, 'MOOCdb_curation'])


