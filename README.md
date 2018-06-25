# free-style-project

# Movie Database Application

Lookup movies playing in theater, Movie info, Actor casting history, now playing in theater, current popular movies and movie suggestion.

## Prerequisites

Requires Python 3.x

Install package dependencies:

```sh
# Windows:
pip install requests
pip install dotenv
```

## Setup

Please visit The Movie DB's website and get its API access code.

[The Movie DB Homepage URL] (https://www.themoviedb.org/?language=en)

[API Page URL] (https://www.themoviedb.org/documentation/api?language=en)

Download all document in this repository

## Usage

Important:
Please enter your API code in the .env file!

If there is a error "Something Went Wrong, HTTP Status Code:XXX, Please Check Read Me and Try Again Later" present please see list down below for potential problem.

```
HTTP    Status Message
----------------------
200     Sccues
401     Authentication failed: You do not have permissions to access the service.
401     Invalid API key: You must be granted a valid key.
503     Service offline: This service is temporarily offline, try again later.
401     Suspended API key: Access to your account has been suspended, contact TMDb.
500     Internal error: Something went wrong, contact TMDb.
401     Authentication failed.
```


## Testing

Run tests:

```sh
pytest tests/ # specify filepath to exclude tests from downloaded repos
```

## [License](LICENSE.md)





