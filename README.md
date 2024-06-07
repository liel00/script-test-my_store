
# script-tests-my-store

## Overview
This project contains automated tests for an online store, focusing on various functionalities like searching products, navigating pages, applying filters, and user authentication.

## Prerequisites
To run the project, ensure you have the following Python packages installed:
- Selenium
- Pytest
- Pytest-HTML
- Webdriver-Manager

You can install these packages using pip:
```sh
pip install selenium pytest pytest-html webdriver-manager
```

## Test Descriptions
1. **Search for Products**: Checks if the search results contain at least one item.
2. **Search for Non-Existent Product**: Tests searching for a product that doesn't exist in the store.
3. **Navigate to T-Shirts Page**: Verifies navigation to the T-SHIRTS page.
4. **Filter by Color**: Tests the color filter in the summer category.
5. **User Authentication**: Tests logging in with an existing user and ensures a non-existing user is blocked.
6. **Logout**: Verifies if a user can successfully log out.

## Test Reporting
After running the tests, a report is generated detailing what passed and what failed. If a test fails, it includes a screenshot and logs of the test.

## Running the Tests
To execute the tests, use the following command:
```sh
pytest --html=report.html
```
This will generate a `report.html` file with the test results.

## Repository Structure
- **PageObjects**: Contains page object models.
- **TestData**: Includes test data files.
- **assets**: Stores assets like images or other resources.
- **test**: Contains the test cases.
- **utilities**: Includes utility functions or helper scripts.
- **MyStoreTest.iml**: IntelliJ IDEA project file.
- **debug.log**: Debug log file.
- **logfile.log**: Log file for test execution.
- **report.html**: HTML report of test results.

## License
This project is open-source. Contributions are welcome.
