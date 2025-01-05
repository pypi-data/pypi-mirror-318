# Zyank

## What is this?

Zyank -  is a library (a modification of the cianparser library) for parsing the cian website with a set of functions for quickly collecting real estate data

### Library features
    
#### All city name(s) must be on Russian language !!! ####

    Sync version

        the `get_info()` function - takes 2 arguments (**number of pages to be processed**=*int*,**list of cities**=*list*)

        the `get_one_info()` function takes 2 arguments (**number of pages to be processed**=*int*,**city name**=*str*)

    Async version (multiple increase in the speed of the function)

        the `get_async_information()` function takes 2 arguments (**number of pages to be processed**=*int*,**list of cities**=*list*), works asynchronously

        the `get_async_one_information()' function takes 2 arguments (**number of pages to be processed**=*int*,**city name**=*str*), works asynchronously

### Code example

```python


    import asyncio

    from zyank import *

    info = asyncio.run(Parser.AsyncParser.get_async_one_information(city='moscwa')) ## must by write on Ru language

    print(info)
    
    ## This example save information in reports dir##
 ```

### async functon start example

`info = asyncio.run(Parser.AsyncParser.get_async_one_information(city='moscwa'))`

### Links

author [libraries-modifications](https://github.com/VoidHiko "modification author")

repository [base library ](https://github.com/lenarsaitov/cianparser "base library")

