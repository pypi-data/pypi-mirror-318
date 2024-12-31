# GLPI REST API Python SDK v0.1.1

This Python library provides a wrapper for the GLPI REST API. It offers a collection of resources representing various GLPI items built upon generic classes.

## Supported Items

* **Tickets:**
    * CRUD operations
    * User assignment
    * Document attachment
* **Ticket Categories:**
    * CRUD operations
* **Request Origin:**
    * CRUD operations
* **Ticket Users:**
    * CRUD operations
* **Users:**
    * CRUD operations
    * Related ticket querying
* **User Emails:**
    * CRUD operations
* **Documents:**
    * CRUD operations
    * Downloading
* **Document Items:**
    * CRUD operations

## How it Works

1. **Connection:** The library establishes a connection to the GLPI server using the authentication method specified in the `.env` file (basic or user token).
2. **Item Modeling:** GLPI items are modeled using dataclasses and generic parent classes to provide specific functionalities for each item.
3. **Resource Creation:** Resources are created for the modeled GLPI items. These resources handle querying, filtering, and creating items.

**Item Hierarchy:**

Items can have subitems or parent items, also represented as resources. Here's an example of this hierarchy:

```
Ticket Categories -> Tickets -> Document Items
User -> Ticket Users <- Tickets
```

## Resource Methods

Every resource has at least the following methods:

* `get(id)`: Retrieves an item with the specified ID.
* `all()`: Retrieves all items.
* `get_multiple(*ids)`: Retrieves multiple items with the provided IDs.
* `search(filters[])`: Filters items using GLPI's search engine.
* `instance(**kwargs)`: Instantiates a GLPI item based on API responses and modeled dataclasses.
* `create(**kwargs)`: Create's a resource with the specified data.

## Item Methods

Every GLPI item has at least the following methods:

* `post_initialization()`: Executes after an item is initialized, allowing for adding new attributes.
* `as_dict()`: Represents the item as a dictionary with formatted attributes.
* `get_api_object()`: Provides access to all attributes returned by the GLPI API.
* `get_subitems_resource()`: Creates a resource for a subitem related to this item (e.g., a Ticket with its Document Items).
* `get_related_parent()`: Fetches a parent item using the parent's resource and the related field (e.g., accessing the parent Ticket of a Ticket User item using the `tickets_id` field).
* `update()`: Updates the item.
* `delete()`: Deletes the item.

## Usage

**1. Create a GLPI Connection:**

```python
from py_glpi.connection import GLPISession

connection = GLPISession()
```

**2. Create a Resource Instance:**

```python
from py_glpi.resources.tickets import Tickets

resource = Tickets(connection)
```

**3. Perform Operations:**

* Retrieve all tickets:

```python
resource.all()
```

* Get a specific ticket:

```python
resource.get(11)
```

* Create a new ticket:
  ##### For attribute reference, visit https://github.com/glpi-project/glpi/blob/main/apirest.md

```python
resource.create(
    name="Test",
    content="Test ticket created with REST Api",
    itilcategories_id=12
)
```


**4. Using the GLPI Search Engine:**

By default, GLPI requires complex filtering criteria. This library simplifies it using the `FilterCriteria` class:

```python
from py_glpi.models import FilterCriteria

filter = FilterCriteria(
    field_uid="Ticket.name",  # Searchable field UUID
    operator="Equals",        # Comparison operator
    value="Test"              # Matching value
)

resource.search(filter)

# Specifying a non-existent field_uid will raise an exception that includes a reference of all the searchable field_uids for the sepcified Resource.
```

Filters can be related using logical operators (AND, OR, XOR) defined as follows:

```python
filter1 = filter
filter2 = FilterCriteria(
    field_uid="Ticket.content",
    operator="Contains",
    value="API"
)

filter = filter1 & filter2  # AND operation
filter = filter1 | filter2  # OR operation
filter = filter1 & filter2 | filter3 # Mixed operation

result = resource.search(filter)  # Logical operations between filter criteria will produce a list related by thus operation.
```

**5. ItemList Methods:**

Methods that return multiple items (all, search, get_multiple) use an extended list class named `ItemList`. This class provides the following methods:

* `filter(**kwargs)`: Offline Filters the results using the `leopards` library (refer to https://github.com/mkalioby/leopards for usage).
* `exclude(**kwargs)`: Reverse Offline Filters the results using the `leopards`.
* `to_representation()`: Returns a list with the result of executing to_dict() method of each contained item.

```python
result = resource.filter(priority__gt=2)  # Offline filters the search result, returns only the tickets with a priority higher than 2.
result = result.exclude(urgency__lt=4)  # Returns only the tickets with a urgency higher than 3.
```

For more usage examples, refer to tests

