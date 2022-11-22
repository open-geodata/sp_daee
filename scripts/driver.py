"""
Driver
out.22
"""

import os
import time

import requests
from dotenv import dotenv_values, find_dotenv
from paths import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu

# config = dotenv_values(find_dotenv(usecwd=False))
# os.environ['GH_TOKEN'] = config['GH_TOKEN']


# Set Options
options = Options()
options.headless = False
options.set_preference('intl.accept_languages', 'pt-BR, pt')
options.set_preference('browser.download.folderList', 2)
options.set_preference('browser.download.manager.showWhenStarting', False)
options.set_preference('browser.download.dir', str(input_path))
options.set_preference(
    'browser.helperApps.neverAsk.saveToDisk',
    'application/octet-stream, application/pdf, application/vnd.ms-excel',
)
options.set_preference(
    'general.useragent.override',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
)
options.set_preference('pdfjs.disabled', True)
options.set_preference('plugin.scan.Acrobat', '99.0')
options.set_preference('plugin.scan.plid.all', False)
options.set_preference('browser.helperApps.showOpenOptionForPdfJS', False)
options.set_preference('browser.download.forbid_open_with', True)


# By default, all driver binaries are saved to user.home/.wdm folder. (0)
# You can override this setting and save binaries to project.root/.wdm. (1)
os.environ['WDM_LOCAL'] = '0'
# print(os.getenv('WDM_LOCAL'))


# Download Driver
driver_binary = GeckoDriverManager(
    # path=project_path,
    # path=None,
    cache_valid_range=30
).install()
print(f'>>>>>> {driver_binary}')


# Create Driver
driver = webdriver.Firefox(
    service=Service(
        executable_path=driver_binary, log_path=logs_path / 'geckodriver.log'
    ),
    options=options,
)


# Add-ons Xpath
xpath_path = adds_path / 'xpath.xpi'
xpath_path = xpath_path.absolute().resolve()
if not xpath_path.is_file():
    r = requests.get(
        'https://addons.mozilla.org/firefox/downloads/file/3588871/xpath_finder-1.0.2-fx.xpi'
    )

    with open(xpath_path, 'wb') as f:
        f.write(r.content)

driver.install_addon(str(xpath_path), temporary=True)


if __name__ == '__main__':
    # Get Url
    driver.get('https://github.com/SergeyPirogov/webdriver_manager')
    driver.get('about:config')

    # Close Connection
    time.sleep(4)
    # driver.quit()

    # Message
    # print('Driver close!!')
