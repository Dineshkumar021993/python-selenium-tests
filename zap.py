import time
from selenium import webdriver
from zapv2 import ZAPv2

# Start ZAP proxy
zap = ZAPv2(apikey='8muzev924gia5f14th5je42orf0', proxies={'https': 'http://localhost:8081'})

# Set up a WebDriver instance (e.g., Chrome)
driver = webdriver.Chrome()

# Define the target URL
target_url = "https://finsights.biz/"

# Perform some actions on the website (e.g., navigate to a page)
driver.get(target_url)
time.sleep(5)  # Wait for the page to load

# Spider the website to discover links (optional)
zap.spider.scan(target_url)

# Wait for the spider to finish (you can add more advanced waiting logic)
while int(zap.spider.status()) < 100:
    print("Spider progress: {}%".format(zap.spider.status()))
    time.sleep(5)

# Perform an active scan on the target
zap.ascan.scan(target_url)

# Wait for the scan to finish (you can add more advanced waiting logic)
while int(zap.ascan.status()) < 100:
    print("Scan progress: {}%".format(zap.ascan.status()))
    time.sleep(5)

# Generate a report
report = zap.core.htmlreport()

# Save the report to a file
with open("zap_report.html", "w", encoding="utf-8") as report_file:
    report_file.write(report)

