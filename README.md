# Python Playwright Automation Framework

This is a minimal, yet robust, framework for web automation built using Python, Playwright, and Pytest.

## 1. Setup

Prerequisites

Python 3.8+ installed.

### Installation Steps

Clone the files into a new directory.

Install dependencies using the requirements.txt file:

pip install -r requirements.txt


### Install Playwright browser drivers: Playwright requires its supported browser binaries (Chromium, Firefox, WebKit) to be installed locally.

playwright install


## 2. Execution

Run tests using the pytest command. You can specify which browser to run against using the --browser flag.

### Run on Chromium (Default)

pytest OR pytest --browser=chromium


### Run on Firefox

pytest --browser=firefox


### Run on WebKit (Safari)

pytest --browser=webkit


## Headless vs. Headed Mode

Tests run headless (no visible browser UI) by default for speed.

To run tests in headed mode (with the browser UI visible) for debugging, use the --headed flag:

pytest --headed --browser=chromium


## Example Test Run

The base_test_case.py will run two automated tests against the Playwright documentation site, testing the search functionality using the configured fixtures.
