# Automation test using Playwright-pytest for online sim purchase
### Navigates to https://onlinesim.robi.com.bd/robi and automates features:
- Purchase prepaid SIM
- Purchase postpaid SIM
- Upgrade SIM to 4.5G
- Switch service provider to Robi
- Replace SIM
- Transfer ownership of SIM

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
+ /html-test-report: step by step execution of test functions across all tests
