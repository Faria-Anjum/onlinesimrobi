# Automation test using Playwright-pytest for onlime sim purchase
### Navigates to https://onlinesim.robi.com.bd/robi and automates the process of purchasing a prepaid sim through home delivery

Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

To run the code, navigate to onlinesimrobi/tests and run the command:
```
pytest
```
Files:
+ /tests/pytest.ini: runs tests in msedge with added cli commands
+ /tests/html-test-report: step by step execution of tests
