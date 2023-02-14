E2E test project high level design

Build all infra structre components to allow us to test and maesure from client prespective.

Main scenario is client requesting a video content and the expected result is the client recieving the video content
as expected. test need to maesure the time from request to response.

The main scenario break down for few scenarios:
    1. Setup stage before test suit is started e.g. clean all caches data.
    2. Verifing all api are working - working with requests module (get, post, delete and put)
    3. Add logging to every action so debugging will be clear. (write to file)
    4. Add project documentaion 
    5. Generate test reports





Monitor Object 
get_cache_servers() - assert that all caches in response are either in state Availabele or Not available and return list of all available caches.

Router Object 
get_video_request() - return redirect request to one of the availabele cache servers. 

Cache Object
clear_content() - setup for clean env before each test.
is_content_localy_stored(content_id) - return boolean

To Run the tests install project dependencies preferably in a virtual env and than either:
    1. run_test.sh 
    2. poetry run pytest --junitxml "test-report.xml" --html "test-report.html"