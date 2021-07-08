## Metamorphic Testing

### Implementing MPSpecific MR with Selenium against google.com

Our metamorphic relationship states that, if query `P` returns `X` number of pages, the follow-up query `P and Q` should return `Y` number of pages such that `Y <= X`.

Refer to `selenium_example.py` and implement the MR in a test case with an assertion. Selenium Python binding documentation is available from [here](https://selenium-python.readthedocs.io/api.html).

### Selenium Webdriver
- For Chrome, please visit: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- For MS Edge, please visit: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- For Apple Safari: run `safaridriver --enable` once to enable WebDriver (for more detailed information, visit [https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari))
- For FireFox, please visit: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

### Checking custom-made sine function

The file `trigonometric.py` contains a custom implementation of sine function based on Taylor series expansion (see [here](https://en.wikipedia.org/wiki/Taylor_series)). Use `Hypothesis` Property Based Testing framework to test the safety of input range, when given $n$ as the number of terms in the Taylor series.