# Proxy_Selenium

A small proxy built to use for any purpose. 
It was initially built to try ramping a url stats from many proxies without being flagged, now it can probably serve as a base for repeted webscrapping.

## Prerequirements 

This was done using Selenium with a Firefox browser, so a proper geckodriver for your OS will be necessary. 
You can find these drivers [here](https://github.com/mozilla/geckodriver/releases)
You do need to have Firefox installed, and to provide the geckodriver within your $PATH if you use a venv

## Installation step : 

*Note* that the script doesn't have any set up URL, you have to edit it yourself. The proxy API is set but I don't expect anything to last so you might need to change that. 
In summary, line 3 & line 31 must be edited for anything to run.

## Future features : 

- [ ] make the functions run on firefox or chromium
- [ ] adding Tor IP function
- [ ] adding BS4
- [ ] adding scrapy 
