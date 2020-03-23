# Edit: This API is deprecated! It has instead been merged with https://github.com/ExpDev07/coronavirus-tracker-api

> Simple API for tracking the coronavirus (COVID-19, SARS-CoV-2), with per county data for each state

## Endpoints

Requests should go to the base url: `` https://coronavirus-county-api.herokuapp.com/`` 

(e.g:  https://coronavirus-county-api.herokuapp.com/latest)

### Getting confirmed cases and deaths
```http
GET /latest
```
```json
{
  "West Virginia":{
      "Jefferson":{
         "confirmed":1,
         "deaths":"0"
      },
      "Mercer":{
         "confirmed":1,
         "deaths":"0"
      }
  },
  ...
}
```

## Data

The data comes from https://coronavirus.1point3acres.com/en. The site is scraped from, and the results cached every day.

## Prerequisites

* [Python 3](https://www.python.org/downloads/)

## Installation

* `git clone https://github.com/JKSenthil/coronavirus-county-api.git`
* `cd coronavirus-county-api`
* `pip install requirements.txt`

## Running

* `flask run`
* Note that scraping will not work because the selenium code is intended for heroku, change the configuration lines in `scraper.py` and add your preferred browser driver 

## License

Available for use by anyone, just credit the datasource and link this repository
