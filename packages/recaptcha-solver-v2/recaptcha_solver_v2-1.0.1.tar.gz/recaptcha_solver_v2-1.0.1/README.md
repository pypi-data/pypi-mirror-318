# Recaptcha Solver

This package provides a solution for solving Google reCAPTCHA challenges using audio recognition.

## Installation

Install the package via pip:

```bash
pip install recaptcha-solver
```


## Example Usage

`recaptcha_solver_v2` module:

```python
from DrissionPage import ChromiumPage
from RecaptchaSolver import RecaptchaSolver
import time

driver = ChromiumPage()
recaptchaSolver = RecaptchaSolver(driver)

driver.get("https://www.google.com/recaptcha/api2/demo")

t0 = time.time()
recaptchaSolver.solveCaptcha()
print(f"Time to solve the captcha: {time.time()-t0:.2f} seconds")

driver.ele("#recaptcha-demo-submit").click()

driver.close()
```