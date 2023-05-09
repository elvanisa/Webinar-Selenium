import unittest
from HTMLTestRunner.runner import HTMLTestRunner
from unittest.suite import TestSuite
import tricentis, tricentis2

if __name__ == "__main__":
    #create test suite
    suite = TestSuite()

    #add test cases
    suite.addTest(unittest.TestLoader().loadTestsFromModule(tricentis))

    #run test
    runner = HTMLTestRunner(
        log=True, 
        verbosity=2, 
        output='report', 
        title='Test report Webinar', 
        report_name='report QA',
        open_in_browser=True,
        description="ini hasil testing", 
        tested_by="SQA",
        add_traceback=False)

runner.run(suite)