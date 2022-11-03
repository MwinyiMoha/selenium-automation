
## Faru Selenium Automation

This is a test project illustrating automation of selenium in python. It establishes a foundation that can be built on in terms of automating UI tests for Lori applications. This specific example tests the Faru login page and features the following highlights:

- Uses selenium python bindings to test login page on Faru
-  Runs both locally and on GitHub Actions
- Generates a test summary report that can be viewed locally and hosted on GitHub Pages
- Some test behavior can be changed via environment variables

## Assumptions/Limitations

To keep this project simple, the following assumptions/limitations were adopted:

- The test only leverages the Chrome driver but can be extended to use Firefox, Safari etc
- For simplicity, a single page is tested
- This test was run on a Linux environment. Windows users might need extra steps configuring the chrome webdriver binary

## Running the project
- Install the chrome webdriver by following the instructions [here](https://chromedriver.chromium.org/home)
- To run with poetry:
```
$ cd faru-selenium-automation
$ poetry install
$ poetry run pytest
```
- For virtualenv users, a requirements file is provided. Create a pytest ini file and run:
```
$ cd faru-selenium-automation
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pytest
```
- A directory `htmlcov` will be created with an index file which provides a summary report on the test run

Happy testing!!
