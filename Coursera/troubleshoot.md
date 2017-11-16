```sudo pip install selenium```

find the directory of webdriver/chrome(safari, firefox)
e.g. 

1. downloads geckodriver (chromedriber)
open unix system directory: finder, hit (command + shift + G)
(trick: 
again: ```pip install selenium```
terminal will give you 
Requirement already satisfied: selenium in /Library/Python/2.7/site-packages)


when using script

```Python
from selenium import webdriver
driver = webdriver.Chrome()
```