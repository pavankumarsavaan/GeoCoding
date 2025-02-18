# **Geo Location Utility**
This project has a utility that calls the below GET API's to retrieve the geo location 
1. By location - http://api.openweathermap.org/geo/1.0/direct?q={city},{state}&limit={limit}&appid={APIkey} if the input parameter contains city & state
2. By zipcode - http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country}&appid={APIkey} if the input parameter is a zipcode

and displays the response in ```GREEN``` if the request is successful or in ```RED``` if it fails along with the response output.

It is implemented using Python programming language and makes use of pip file to install the dependent libraries like requests, coloroma etc

**_requests_** - library to make http requests

**_colorma_** - library to pretty print the output and to color code the outputs in red or green

## **Pre-requisites**
Before running this utility, make sure you have below components installed

1. Python
2. Pipenv

### **Installation**
#### **Mac**
1. Install home brew if not installed already with command
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Python _(Version **3.11** preferred)_ with command
`brew install python`
3. Verify the python installation with command
`python3 --version`
`Ex: Output : Python 3.11.9`
4. Install pipenv
`pip3 install pipenv`
5. Generate piplock file for dependencies
`pipenv lock`
6. Sync the dependencies
`pipenv sync`
7. Create virtual env
`pipenv shell`

#### **Windows**
1. Download python installer _(Version **3.11** preferred)_ by visiting the website **[Python Community Edition](https://www.python.org/downloads/release/python-3119/)** 
2. Under Files at the bottom, select the relevant OS version EX: Windows installer (64-bit)
3. Install python by double-clicking the .exe installer. Make sure to select the add PATH variable to env variable checkbox
4. Open command prompt and verify the python installation with command 
`python3 --version`
`Ex: Output : Python 3.11.9`
5. Install pipenv
`pip install pipenv`

## Run Utility

1. Unzip/Extract and place the GeoCoding folder in local machine
2. Navigate to the _**GeoCoding**_ root folder 
3. Generate piplock file for dependencies
`pipenv lock`
4. Sync the dependencies
`pipenv sync`
5. Create virtual env
`pipenv shell`
6. Run the geolocation utility with the below command

#### **Mac**

`python3 geo_location_util.py "Madison, WI" "12345"`

#### **Windows**

`python geo_location_util.py "Madison, WI" "12345"`

## Sample Outputs

Sample outputs with screenshots are uploaded under **_results_** folder for reference

1. Successful API response with valid inputs - **_results/Success.png_**

`python geo_location_util.py "Madison, WI" "12345"`

`Response for input: Madison, WI -> Success
[
    {
        "name": "Madison",
        "local_names": {
            "ru": "\u041c\u0430\u0434\u0438\u0441\u043e\u043d",
            "ta": "\u0bae\u0bc7\u0b9f\u0bbf\u0b9a\u0ba9\u0bcd",
            "en": "Madison",
            "uk": "\u041c\u0435\u0434\u0456\u0441\u043e\u043d",
            "zh": "\u9ea6\u8fea\u900a",
            "sr": "\u041c\u0435\u0434\u0438\u0441\u043e\u043d",
            "pl": "Madison"
        },
        "lat": 43.074761,
        "lon": -89.3837613,
        "country": "US",
        "state": "Wisconsin"
    }
]`

`Response for input: 12345 -> Success
{
    "zip": "12345",
    "name": "Schenectady",
    "lat": 42.8142,
    "lon": -73.9396,
    "country": "US"
}`

2. Failed API response with invalid inputs - **_results/Failed.png_**

`python geo_location_util.py "506001" "503111"`

`Response for input: 506001 -> Failed
{
    "cod": "404",
    "message": "not found"
}`

`Response for input: 503111 -> Failed
{
    "cod": "404",
    "message": "not found"
}`

3. Success & Failed API responses with mixed inputs - **_results/Success&Failed.png_**

`python geo_location_util.py "Madison, WI" "506001"`

`Response for input: Madison, WI -> Success
[
    {
        "name": "Madison",
        "local_names": {
            "sr": "\u041c\u0435\u0434\u0438\u0441\u043e\u043d",
            "pl": "Madison",
            "ru": "\u041c\u0430\u0434\u0438\u0441\u043e\u043d",
            "ta": "\u0bae\u0bc7\u0b9f\u0bbf\u0b9a\u0ba9\u0bcd",
            "en": "Madison",
            "uk": "\u041c\u0435\u0434\u0456\u0441\u043e\u043d",
            "zh": "\u9ea6\u8fea\u900a"
        },
        "lat": 43.074761,
        "lon": -89.3837613,
        "country": "US",
        "state": "Wisconsin"
    }
]`

`Response for input: 506001 -> Failed
{
    "cod": "404",
    "message": "not found"
}`