# Automation test using Playwright-pytest for online sim purchase
### Navigates to https://onlinesim.robi.com.bd/robi and automates the process of purchasing a prepaid sim through home delivery

Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

To run the code, move to onlinesimrobi folder and run the command:
```
pytest
```
Files:
+ /conftest: creates single page instance for all tests
+ /pytest.ini: runs tests in msedge with added cli commands
+ /html-test-report: step by step execution of tests
