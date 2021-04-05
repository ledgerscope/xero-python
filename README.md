# xero-python

[![image](https://img.shields.io/pypi/v/xero-python.svg)](https://pypi.python.org/pypi/xero-python)

<!-- [![image](https://img.shields.io/travis/xero-github/xero-python.svg)](https://travis-ci.com/xero-github/xero-python) -->

<!-- [![Documentation Status](https://readthedocs.org/projects/xero-python/badge/?version=latest)](https://xero-python.readthedocs.io/en/latest/?badge=latest) -->

<!--  *   Documentation: <https://xero-python.readthedocs.io>. -->

Official python SDK for Xero API generated by OpenAPI spec for oAuth 2

## Features

* XERO API Client with oauth2 token integration.
* Automatic OAuth 2 token refresh before token expiration.
* Class based interface for Xero API endpoints.
* Model classes used to represent API data.
* Currently Supported API sets:

    * [Accounting API](https://developer.xero.com/documentation/api/api-overview)
    * [Assets API](https://developer.xero.com/documentation/assets-api/overview)
    * [Files API](https://developer.xero.com/documentation/files-api/overview-files)
    * [Payroll API (AU)](https://developer.xero.com/documentation/payroll-api/overview)
    * [Payroll API (NZ)](https://developer.xero.com/documentation/payroll-api-nz/overview)
    * [Payroll API (UK)](https://developer.xero.com/documentation/payroll-api-uk/overview)
    * [Projects API](https://developer.xero.com/documentation/projects/overview-projects)
    
* Error handling for ease of use.

## SDK Documentation
* [Accounting](https://xeroapi.github.io/xero-python/v1/accounting/index.html)

## Starter Project
We've created [xero-python-outh2-starter](https://github.com/XeroAPI/xero-python-oauth2-starter) a project to demonstrate how to use this SDK.

* oauth 2 flow to obtain a token
* token refresh
* identity to obtain tenant_id
* organisation endpoint
* create contact
* create multiple contacts
* get invoices using where clause

Here is a [15 min video walkthrough](https://www.youtube.com/watch?v=i8JWtbMo90M) on using the starter project.

## Kitchen Sync app
We've created [xero-python-outh2-app](https://github.com/XeroAPI/xero-python-oauth2-app) a project to demonstrate how to make API calls and displays the python code used to make the call and the JSON response.

* oauth 2 flow to obtain a token
* token refresh
* identity to obtain tenant_id
* accounting
    * accounts
    * contacts
    * invoices
* assets
    * asset
    * asset type
    * asset settings
* projects
    * projects
    * project users
    * tasks
    * time
* au payroll
    * employee
    * leave applications
    * pay items
    * payroll calendar
    * pay runs
    * pay slips
    * settings
    * superfunds
    * superfund products
    * timesheets
* uk payroll
    * employees
    * employement
    * employees tax
    * employee opening balance
    * employees leave
    * employees leave balances
    * employees statutory leave balances
    * employees statutory leave summary
    * employees statutory sick leave
    * employees leave periods
    * employees leave types
    * employees pay templates
    * employer pensions
    * deductions
    * earnings orders
    * earnings rates
    * leave types
    * reimbursements
    * timesheets
    * payment methods
    * payrun calendars
    * salary and wage
    * pay runs
    * pay slips
    * settings
    * tracking categories

## Credits

* This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.


## Contribution

Please read [contribution](https://github.com/xero-github/xero-python/blob/master/CONTRIBUTING.md) guidelines.

## License

This software is published under the [MIT License](http://en.wikipedia.org/wiki/MIT_License).

	Copyright (c) 2020 Xero Limited

	Permission is hereby granted, free of charge, to any person
	obtaining a copy of this software and associated documentation
	files (the "Software"), to deal in the Software without
	restriction, including without limitation the rights to use,
	copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the
	Software is furnished to do so, subject to the following
	conditions:

	The above copyright notice and this permission notice shall be
	included in all copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
	OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
	NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.
