**Simple CRUD operation**
----
Create, Read, Update, and Delete data from database.

* **URL**
To create: /create
To read: /read
To update: /update
To delete: /delete/<id>
	
* **Method:**

`GET` | `POST`

* **URL Params**

The id of data is required to delete the data row.
Required:
`id=[integer]`

* **Data Params**

To create data data params required are:
`order_id=[integer]
product_id=[integer]
user_id=[integer]
rating=[float] in range 1 to 5
review=[string]`


To update data data params required are:
`id=[integer]
order_id=[integer]
product_id=[integer]
user_id=[integer]
rating=[float] in range 1 to 5
review=[string]`

* **Success Response:**

**POST url/create**

  * **Code: 200** <br />
    **Content:** `'Data added successfully!'`

**GET url/read**

* **Code: 200** <br />
  **Content:**
{
    `"id" : 1,
    "order_id" : 12,
    "product_id" : 20,
    "user_id" : 1,
    "rating" : 5,
    "review" : "The food is delicious!"`
}

**POST url/update**


  * **Code: 200** <br />
    **Content:** `'Data updated successfully!'`


**GET url/delete/<id>**


  * **Code: 200** <br />
    **Content:** `'Data deleted successfully!'`
    
* **Error Response:**

* **Code: 404** <br />
  **Content:** `{ status : 404
           message :"Not Found:" + request.url}`
