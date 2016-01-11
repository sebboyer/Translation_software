
-- Copy CSV files from /tmp folder to mySQL DB

use COURSE_NAME;

-- SET @COURSE_NAME = 'moocdb_csv_test'

-- Copy agent data

LOAD DATA local INFILE  '/tmp/COURSE_NAME/agent.csv'
INTO TABLE agent
FIELDS TERMINATED BY ',';

-- Copy answer data
-- LOAD DATA local INFILE '/tmp/COURSE_NAME/answer.csv'
-- INTO TABLE answer
-- FIELDS TERMINATED BY ',';

-- Copy assessments data
LOAD DATA local INFILE '/tmp/COURSE_NAME/assessments.csv'
INTO TABLE assessments
FIELDS TERMINATED BY ',';

-- Copy observed_events data
LOAD DATA local INFILE '/tmp/COURSE_NAME/observed_events.csv'
INTO TABLE observed_events
FIELDS TERMINATED BY ',';

-- Copy os data
LOAD DATA local INFILE '/tmp/COURSE_NAME/os.csv'
INTO TABLE os
FIELDS TERMINATED BY ',';

-- Copy problem_types data
LOAD DATA local INFILE '/tmp/COURSE_NAME/problem_types.csv'
INTO TABLE problem_types
FIELDS TERMINATED BY ',';

-- Copy problems data
LOAD DATA local INFILE '/tmp/COURSE_NAME/problems.csv'
INTO TABLE problems
FIELDS TERMINATED BY ',';

-- Copy resource_types data
LOAD DATA local INFILE '/tmp/COURSE_NAME/resource_types.csv'
INTO TABLE resource_types
FIELDS TERMINATED BY ',';


-- Copy resources data
LOAD DATA local INFILE '/tmp/COURSE_NAME/resources.csv'
INTO TABLE resources
FIELDS TERMINATED BY ',';


-- Copy resources_urls data
LOAD DATA local INFILE '/tmp/COURSE_NAME/resources_urls.csv'
INTO TABLE resources_urls
FIELDS TERMINATED BY ',';

-- Copy submissions data
LOAD DATA local INFILE '/tmp/COURSE_NAME/submissions.csv'
INTO TABLE submissions
FIELDS TERMINATED BY ',';

-- Copy urls data
LOAD DATA local INFILE '/tmp/COURSE_NAME/urls.csv'
INTO TABLE urls
FIELDS TERMINATED BY ',';