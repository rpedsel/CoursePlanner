 \#\# Using Selenium Webdriver MacOS 

1. Install Selenium: `sudo pip install selenium`


2. Downloads geckodriver (or chromedriber)

	e.g. `Downloads/geckodriver`

3. Find the directory of webdriver/chrome (safari, firefox)

   * open unix system directory: finder, hit (command + shift + G)

   * Trick: hit again: `pip install selenium`, terminal will give you:

	 "Requirement already satisfied: selenium in /Library/Python/2.7/site-packages"

   * Go to selenium folder find web driver, drill down to Firefox


4. Add path for webdriver and geckodriver:

   * `vim ~/.bash_profile`

   `PATH = '/Library/Python/2.7/site-packages/selenium/webdriver/firefox/:/Users/fp/Downloads/Driver' 
`````export PATH````

   * `source ~/.bash_profile`

5. Call  Selenium Webdriver in Python:

```Python
from selenium import webdriver
driver = webdriver.Chrome()
```