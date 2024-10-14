# Automation test using Playwright-pytest for online sim purchase
### Navigates to https://onlinesim.robi.com.bd/robi and automates features:
- #### Purchasing prepaid sim
- #### Purchasing postpaid sim

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
