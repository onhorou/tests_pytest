### install webdriver for linux
```
curl -L https://chromedriver.storage.googleapis.com/{number_version_chromedriver}/chromedriver_linux64.zip -o chromedriver.zip
sudo unzip chromedriver.zip -d /usr/bin/
sudo chmod +x /usr/bin/chromedriver
```
> Где `{number_version_chromedriver}` = chrome local browser version

### install dependencies
- cd to the directory where requirements.txt is located.
- activate your virtualenv.
- run: pip install -r requirements.txt in your shell.

### running tests with generating a report in allure
```bash
pytest --alluredir=./allure-results
```