from APIKL import APIKL

files1 = ['java/testDirectory', 'resources/database.json']
files2 = ['java/testDirectory/database.xml', 'resources']
locator = APIKL(files1, 6)
locator.find_keys()
