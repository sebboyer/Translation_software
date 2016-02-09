# Configuration file
import re

## Input source
## Can be either 'csv', 'sql' or 'json'
INPUT_SOURCE = 'csv'
QUOTECHAR = "'" 
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
# MIT courses : %Y-%m-%dT%H:%M:%S.%f
# Stanford Courses : %Y-%m-%d %H:%M:%S


## CSV input files
COURSE_NAME='201x-2013-Spring'
COURSE_START_DATE = '2012-03-05 12:00:00' # The format is '2012-03-05 12:00:00'

CSV_SOURCE_DIR = '/home/sebboyer/port/data_copy/201x-2013-Spring/intermediary_csv/'
CSV_PREFIX = 'test'

EDX_TRACK_EVENT = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_EdxTrackEventTable.csv'])
CORRECT_MAP = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_CorrectMapTable.csv'])
ANSWER = ''.join([CSV_SOURCE_DIR, CSV_PREFIX, '_AnswerTable.csv'])

## Output files
DEST_DIR = '/home/sebboyer/port/data_copy/201x-2013-Spring/moocdb_csv/'

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

## Curation settings 
MAX_DURATION_SECONDS = 3600
DEFAULT_DURATION_SECONDS = 100 


