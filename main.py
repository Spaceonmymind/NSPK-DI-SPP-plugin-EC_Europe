from selenium import webdriver

from logging import config
config.fileConfig('dev.logger.conf')
from ec_europa_eu import EcEuropaEu

driver = webdriver.Chrome()

parser = EcEuropaEu(driver)
docs = parser.content()


print(*docs, sep='\n\r\n')