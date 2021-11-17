import asyncio
from pyppeteer import launch
import time

times = 0

launch_args = {
    "executablePath": r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    #"headless": False,
    "userDataDir": r"G:/123/",
    "args": [
        "--start-maximized",
        "--no-sandbox",
        "--disable-infobars",
        "--ignore-certificate-errors",
        "--log-level=3",
        "--enable-extensions",
        "--window-size=1920,1080",
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    ],
    'dumpio':True
}

async def chrome(url):
    global times
    browser = await launch(**launch_args)
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(10 * 1000)

    await page.goto(url)
    await page.setViewport({"width": 1920,"height": 1080})
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    #time.sleep(10)
    r = await page.content()
    await browser.close()
    return r


#asyncio.get_event_loop().run_until_complete(chrome())