# Automated testing on scopes of the Robi DA website (onlinesim.robi.com.bd) using Playwright-pytest
### Navigates to https://onlinesim.robi.com.bd and performs:

+ Case-defined tests on:
  - Purchasing prepaid Robi SIM
  - Purchasing prepaid Airtel SIM
  - Purchasing postpaid Robi SIM
    
+ Acceptance tests on:
  - Upgrading Robi SIM to 4.5G
  - Upgrading Airtel SIM to 4.5G
  - Switching service provider to Robi
  - Switching service provider to Airtel
  - Replacing Robi SIM
  - Replacing Airtel SIM
  - Transferring ownership of Robi SIM
  - Transferring ownership of Airtel SIM

Requires installation of:
- python 3.12
- pytest-playwright
- pytest-xdist
- pytest-html

To run tests, move to onlinesimrobi folder and run the command:

```
pytest
```

Config files:
+ /conftest: creates single page instance for all test functions
+ /pytest.ini: runs tests in msedge with added cli commands

Reports:
+ /html-test-report: step by step execution of test functions across all tests
