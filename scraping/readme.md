# Function 1: __init__(self, timeout=10)
## This function is the constructor of the SeleniumScraper class. It initializes the timeout variable, which is set to 10 by default. It also creates an httpx.AsyncClient object, which is used to send HTTP requests asynchronously. Additionally, it sets the storagePath variable to the path where the log files will be stored, and initializes a logging object to write log messages to the file.

### Parameters
* timeout: the timeout value for the HTTP requests

- usage
```
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self.storagePath = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(self.storagePath):
            os.makedirs(self.storagePath)
        logging.basicConfig(
            filename=os.path.join(self.storagePath, "log.txt"),
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )
```
> Note: The __init__ function is the constructor of the SeleniumScraper class. It takes one parameter: timeout. The timeout parameter is the timeout value for the HTTP requests. It initializes the timeout variable, which is set to 10 by default. It also creates an httpx.AsyncClient object, which is used to send HTTP requests asynchronously. Additionally, it sets the storagePath variable to the path where the log files will be stored, and initializes a logging object to write log messages to the file.

# Function 2: fetch_request_async(self, url, params=None)
## This function sends an HTTP GET request asynchronously using the httpx library. It takes a url argument as input and an optional params dictionary. If the response status code is 200, it returns the text content of the response. If the response status code is 301, it retries the request with the new location in the Location header. If an exception occurs during the request, it writes the exception message to the log file and returns None.

### Parameters
* url: the URL of the webpage to fetch
* params: a dictionary of parameters to send with the request

- usage
```
    async def fetch_request_async(self, url, params=None):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
            }
            response = await self.session.get(url, headers=headers)
    
            if response.status_code == 200:
                print("Response status code successful for url: {} and status code: {}".format(url, 200))
                return response.text
            
            if response.status_code == 301:
                # retry with redirect
                response = await self.session.get(response.headers['Location'])
                response.raise_for_status()
                if response.status_code == 200:
                    return response.text
                
        except Exception as e:
            logging.info(
                "Exception occurred for url: {} and exception: {}".format(url, e)
            )
            pass
            return None

```
> Note: The fetch_request_async function is used to send an HTTP GET request asynchronously using the httpx library. It takes two parameters: url and params. The url parameter is the URL of the webpage to fetch. The params parameter is a dictionary of parameters to send with the request. If the response status code is 200, it returns the text content of the response. If the response status code is 301, it retries the request with the new location in the Location header. If an exception occurs during the request, it writes the exception message to the log file and returns None.

# Function 3: fetch_request_normal(self, url, params=None)
## This function sends an HTTP GET request using the requests library. It takes a url argument as input and an optional params dictionary. If the response status code is 200, it returns the text content of the response. If the response status code is 301, it retries the request with the new location in the Location header. If an exception occurs during the request, it writes the exception message to the log file and returns None.

### Parameters
* url: the URL of the webpage to fetch
* params: a dictionary of parameters to send with the request

- usage
```
    def fetch_request_normal(self, url, params=None):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print("Response status code successful for url: {} and status code: {}".format(url, 200))
                return response.text
            
            if response.status_code == 301:
                # retry with redirect
                response = requests.get(response.headers['Location'])
                response.raise_for_status()
                if response.status_code == 200:
                    return response.text
            
        except Exception as e:
            logging.info(
                "Exception occurred for url: {} and exception: {}".format(url, e)
            )
            pass
            return None
```
> Note: The fetch_request_normal function is used to send an HTTP GET request using the requests library. It takes two parameters: url and params. The url parameter is the URL of the webpage to fetch. The params parameter is a dictionary of parameters to send with the request. If the response status code is 200, it returns the text content of the response. If the response status code is 301, it retries the request with the new location in the Location header. If an exception occurs during the request, it writes the exception message to the log file and returns None.

# Function 4: get_xpath_link(self, doc, xpath, website)
## This function takes an HTML document doc, an XPath xpath, and a website URL as input. It extracts all the links that match the XPath expression and appends the website URL to each link that starts with a forward slash. It returns a list of the modified links. If an exception occurs during the process, it writes the exception message to the log file and returns None.

### Parameters
* doc: an HTML document made using the LXML library
* xpath: an XPath expression
* website: the website URL

- usage
```
    def get_xpath_link(self, doc, xpath, website):
        try:
            name = doc.xpath("".join(xpath))
            print(name)
            for i in range(len(name)):
                if name[i].startswith("/"):
                    name[i] = website + name[i]
                else:
                    name[i] = name[i]
            return name

        except Exception as e:
            logging.info("Error in getting {}: {}".format(name, e))
            pass
            return None
            pass
```
> Note: The get_xpath_link function is used to extract links from an HTML document using an XPath expression. It takes three parameters: doc, xpath, and website. The doc parameter is an HTML document made using the LXML library. The xpath parameter is an XPath expression. The website parameter is the website URL. The function extracts all the links that match the XPath expression and appends the website URL to each link that starts with a forward slash. It returns a list of the modified links. If an exception occurs during the process, it writes the exception message to the log file and returns None.

# Function 5: get_selenium_driver(self)
## This function creates a headless Chrome webdriver using the selenium library. It sets various options for the Chrome browser to run in headless mode and disables various features such as logging and extensions. It returns the webdriver object.

### Parameters
* None

- usage
```
    def get_selenium_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--silent")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver
```
> Note: The get_selenium_driver function is used to create a headless Chrome webdriver using the Selenium library. It is used if simple requests are not enough to fetch the page. It takes no parameters and returns a Selenium webdriver object. add more chrome options if needed.


# Function 6: fetch_request_selenium(self, url, waiting_time=1)
## This function uses a Selenium webdriver to fetch an HTML page. It takes a url argument as input and an optional waiting_time argument, which is set to 1 by default. It opens the URL in the headless Chrome browser and waits for waiting_time seconds before returning the page source as an html object. If an exception occurs during the process, it writes the exception message to the log file and returns None.

### Parameters
* url: the URL of the webpage to fetch
* waiting_time: the amount of time to wait before returning the page source (in seconds)
- usage
```
    def fetch_request_selenium(self, url, waiting_time=1):
        try:
            driver = await self.get_selenium_driver()
            driver.get(url)
            time.sleep(waiting_time)
            doc = html.fromstring(driver.page_source)
            logging.info("Response status code successful for url: {} and status code: {}".format(url, 200))
            driver.close()
            return doc

        except Exception as e:
            logging.info(
                "Exception occurred for url: {} and exception: {}".format(url, e)
            )
            pass
```
> Note: The fetch_request_selenium function is used to fetch an HTML page using a Selenium webdriver. It is used if simple requests are not enough to fetch the page.

# Function 7: get_xpath_data(self, doc, xpath)
## This function takes an HTML document doc and an XPath xpath as input. It extracts all the data that matches the XPath expression and returns a list of the extracted data. If an exception occurs during the process, it writes the exception message to the log file and returns None.

### Parameters
* doc: an HTML document made using the LXML library
* xpath: an XPath expression

- usage
```
    def get_xpath_data(self, doc, xpath):
        try:
            name = doc.xpath(xpath)
            return name

        except Exception as e:
            print("Error in getting {}: {}".format(name, e))
            pass
            return None
```
> Note: The get_xpath_data function is used to extract data from an HTML document using an XPath expression. It takes two parameters: doc and xpath. The doc parameter is an HTML document made using the LXML library. The xpath parameter is an XPath expression. The function extracts all the data that matches the XPath expression and returns a list of the extracted data. If an exception occurs during the process, it writes the exception message to the log file and returns None.


# Function 8: slow_selenium_scroll(driver, speed):

## This function uses the Selenium WebDriver to scroll down a webpage slowly. The function takes two parameters:

### Parameters
* driver: a Selenium WebDriver instance
* scroll_pause_time: the amount of time to pause between each scroll (in seconds)
The function scrolls down the webpage slowly by executing a JavaScript code snippet that scrolls the page by a certain amount and then pauses for a specified time before scrolling again. The amount and duration of the scrolling can be adjusted by modifying the values of the scroll_step and scroll_pause_time variables respectively.

- usage
```
    def slow_page_scroll(self, driver, speed):
        current_scroll_position = driver.execute_script("return window.pageYOffset;")
        while current_scroll_position < driver.execute_script(
            "return document.body.scrollHeight;"
        ):
            driver.execute_script(
                "window.scrollTo(0, arguments[0]);", current_scroll_position
            )
            current_scroll_position += 1000
            time.sleep(speed)
```

> Note: That this function can be slow, especially if the webpage is very long or contains a lot of content. If performance is an issue, it might be better to use a different approach, such as the execute_script function provided by the WebDriver API.
