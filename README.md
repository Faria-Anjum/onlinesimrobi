# Automated testing on scopes of onlinesim.robi.com.bd using Playwright-pytest
### Navigates to https://onlinesim.robi.com.bd/robi and performs automated tests on:
- Purchasing prepaid Robi SIM
- Purchasing postpaid Robi SIM
- Upgrading Robi SIM to 4.5G
- Switching service provider to Robi
- Replacing Robi SIM
- Transferring ownership of Robi SIM

Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

To run the code, move to onlinesimrobi folder and run the command:

```
pytest
```
Config files:
+ /conftest: creates single page instance for all test functions
+ /pytest.ini: runs tests in msedge with added cli commands

Reports:
+ /html-test-report: step by step execution of test functions across all tests
