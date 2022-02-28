# Coding challenge
### Description:
Technical Challenge for the Python Developer Vacancy.

### Heroku
```
https://library-sandro.herokuapp.com/
```

### Requirements:

The following components must be installed:

[Python](https://www.python.org//) v3+.

### Installation:

* Clone repository

```
git clone https://github.com/SandroJordao/python-library.git
```

* Create virtual env

```
python -m venv .venv
```

* Install requirements
``` 
pip install -r requirements.txt
```

* Create the database 
``` 
python manage.py migrate 
```

* Create a superuser 
``` 
python manage.py createsuperuser 
```

* Start the server
``` 
python manage.py runserver 
```

Access the system.

### Command for importing authors in .csv
``` 
python manage.py import_authors authors.csv
```

## API
Resources available for access via API:
* [**Authors**](#Authors)
* [**Books**](#Books)

## Authors [/authors/]

### List [GET]
Response 200 (application/json)

```
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "Stephen King"
		}
	]
}
```

### Read [GET /authors/{id}]
###### Parameters
* *id (required, number)*

Response 200 (application/json)

```	
{
	"id": 1,
	"name": "Stephen King"
}	
```

### Create [POST /authors/]
Request (application/json)

Body

```
{
	"name": "J. K. Rowling"
}
```	

### Update [PUT /authors/{id}]	
###### Parameters
* *id (required, number)*	

Body

```
{
	"name": "J. K. Rowling"
}
```	

### Delete [DELETE  /authors/{id}]
###### Parameters
* *id (required, number)*


## Books [/books/]

### List [GET]
Response 200 (application/json)

```
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
		    "id": 1,
		    "name": "Christine",
		    "edition": 1,
		    "publication_year": 1983,
		    "authors": [
			1
		    ]
		}
	]
}
```

### Read [GET /books/{id}]
###### Parameters
* *id (required, number)*

Response 200 (application/json)

```	
{
    "id": 1,
    "name": "Christine",
    "edition": 1,
    "publication_year": 1983,
    "authors": [
        1
    ]
}	
```

### Create [POST /books/]
Request (application/json)

Body

```
{
    "name": "Christine",
    "edition": 1,
    "publication_year": 1985,
    "authors": [
        1
    ]
}
```	

### Update [PUT /books/{id}]	
###### Parameters
* *id (required, number)*	

Body

```
{
    "name": "Christine",
    "edition": 1,
    "publication_year": 1983,
    "authors": [
        1
    ]
}
```	

### Delete [DELETE  /books/{id}]
###### Parameters
* *id (required, number)*
