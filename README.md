# free-style-project

# Movie Database Application

Functions:

1. List Movies in Theater Now

2. Movie Info

3. Actor/Actress Casting History 

4. Current Popular Movies

5. Movie Suggestion.

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

[The Movie DB Homepage](https://www.themoviedb.org/?language=en)

[API Page](https://www.themoviedb.org/documentation/api?language=en)

Download all document in this repository

## Usage

**Important:**

**Please enter your API code in the .env file before use!**

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
**Error**

There are missing info in the database, sometimes the database will have errors(like missing release date in a movie) this will return an error which is out of my control. If ever encounter that please choose something else.

## Testing

Run tests:

```sh
pdb.set_trace() #for testing
```

## [License](LICENSE.md)





