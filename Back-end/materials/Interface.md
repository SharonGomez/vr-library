# Interface

## Interface

- book/recommend

  - response`<list >` obj >
    - book-id
- book/get

  - body
    - book-id (str)
  - response`<obj>`
    - book-detail
- book/categories**(removed)**

  - response`<list>`
- book/categories/get

  - response`<list>`
- book/all

  - response <list -> obj>
- book/get-file **(removed)**

  - body
    - book-id
  - response
    - file(url => str)
- book/comment/get

  - body

    - amount
  - response

    - list
- book/comment/post

  - body
    - post
  - response
    - statue
- rent/book/add

  - body
    - book-id
  - response
    - status => success or fail
- rent/book/update => (update/delete)

  - body
    - book-id
  - response
    - status => success or fail
- room/list

  - response `<list>`

    - room -> seat

      ```json
      {
          "room_id": "xxxxxxx",
          "seatList": [{
              "seat_id": "xxx",
              ...
          }],
          "total_seat_amount": 30,
          "total_rest_amount": 20,
          ...
      }
      ```
- rent/seat/add

  - body

    - room-id
    - seat-id
  - response

    - status => success or fail
- rent/seat/update => (update/delete)

  - body
    - book-id
  - response
    - status => success or fail
- book/search

  - body

    - search-content
  - response `<list>`

    ```json
    {
        "book_id": "xxxx",
        "desc": "xxxxx",
        "name": "xxxx",
        "thumbnail": "xxxx"
    }
    ```
- user/login

  - body
    - email
    - pwd
  - response`<obj>`
    - user-detail
    - book-list
    - seat-info
- user/signup

  - body
    - username
    - email
    - pwd
  - response
    - status => success or fail
- user/model

  - body
    - user-id
  - response`<str>`
- model/list

  - response <list - string>
  - ```json
    {
    	statue: 200,
        msg: "ok",
        model_list: [{
            name: "xxx",
            url: "xxx"
            model_id: "xxx"
        }]
    }
    ```

## Interface Name: recommendation

Interface acquisition method: POST

URL: book/recommendation

Interface status: Completed

### Body

```json
{
  "amount": 20
}
```

### Response:

```json
{
"status":200,
"msg":"ok",
"data":[{
    "book_id":"1231223",
    "book_name":"test",     // can not be null
    "book_url": "",
    "thumbnail":  "",//saved as url in database
}], 
}
```

| Field Name | Field Type | Null or not | Default Value | Sample          | description                             |
| ---------- | ---------- | ----------- | ------------- | --------------- | --------------------------------------- |
| statue     | char       | N           |               | 200             | response result<br />(sucessful or not) |
| msg        | string     | Y           |               | ok              | detail response statue                  |
| data       | list       |             |               |                 | contain the things listed below         |
| book_id    | Char       | N           | 0000000       | 1221223         | Generate by Chart                       |
| book_name  | string     | Y           |               | History of Roma |                                         |
| book_url   | string     | Y           |               | ../1221223.pdf/ | saved as pdf file                       |
| thumbnail  | string     | Y           |               | ../1221223.png/ | give a url and saved as a png file      |

## Interface Name: Book

Interface acquisition method: POST

URL: book/get/

Interface status: completed

### Body:

```json
{
	"book_id": "1231232"
}
```

### Response:

```json
{
"status": 200,
"msg":"ok",
"data":{
    "book_id":"1231232",
    "book_name":"History of Roma",
    "thumbnail":".../xxxx.png/",
    "book_url":".../xxx.pdf",
    "desc":"the book tells a story...",
    "author":"John.Smith",
    "category":"horror",
    "font_amount":1223456,
    "ISBN":"RJDEWF4",
    "language":"English",
    "status":10,
    "upload_time": "4235329858434",
    "read_amount":32,
    "comment_amount":32,
    "recommended_amount":13
    }
}
```

| Field Name       | Field Type | Null or not | Default value | Sample                                | Description                                                  |
| ---------------- | ---------- | ----------- | ------------- | ------------------------------------- | ------------------------------------------------------------ |
| statue           | char       | N           |               | 200                                   | response result(sucessful or not)                            |
| msg              | string     | Y           |               | ok                                    | detail response statue                                       |
| data             | obj        |             |               |                                       |                                                              |
| book_id          | Char       | N           | 0000000       | 1221223                               | Generate by Chart                                            |
| book_Name        | String     | Y           |               | History of Roma                       |                                                              |
| thumbnail        | String     | Y           |               | ../1221223.png/                       | give a url and saved as a png file                           |
| book_url         | string     | Y           |               | ../1221223.pdf/                       | saved as pdf file                                            |
| desc             | string     | Y           |               | the book tells a<br />story about.... | description of the book                                      |
| author           | string     | Y           |               | John.Smith                            |                                                              |
| category         | string     | Y           |               | Horror                                |                                                              |
| font_amount      | boolean    | Y           |               | 13345677                              |                                                              |
| ISBN             | String     | Y           |               | RJSV284884929                         |                                                              |
| language         | String     | Y           |               | English                               |                                                              |
| status           | int        | N           | 30            | 10                                    | can or cannot lend or lending<br />10 can be lend<br />20 lending<br />30 can not lend |
| upload_time      | timestamp  | Y           |               | 14814                                 | book upload time                                             |
| read_amount      | int        | Y           | 0             | 30                                    | times the book<br />lent                                     |
| comment_amount   | int        | Y           | 0             | 20                                    |                                                              |
| recommend_amount | int        | Y           | 0             | 10                                    | like+1<br />dislike-1                                        |

## Interface Name: book/categories/get

Interface Acquisition Method: Post

URL: book/categories/get

Interface Status: completed

### Body

```json
{
	"category":"horror"
}
```

### Response

```json
{
"status":200,
"msg":"ok",
"data":[{
    "category":"horror",
    "book_id":"1231232",
    "book_name":"history of Roma",
    "author":"John.Smith",
    "book_url":".../xxx.pdf/",
    "thumbnail":".../xxx.png/",
    "recommended_amount":13
}]
}
```

| Field Name         | Field Type | Null or not | Default Value | Sample          | description                             |
| ------------------ | ---------- | ----------- | ------------- | --------------- | --------------------------------------- |
| statue             | int        | N           |               | 200             | response result<br />(sucessful or not) |
| msg                | string     | Y           |               | ok              | detail response statue                  |
| data               | list       |             |               |                 | contain the things listed below         |
| category           | string     | Y           |               | horror          |                                         |
| book_id            | string     | N           | 0000000       | 1221223         | Generate by Chart                       |
| book_name          | string     | Y           |               | History of Roma |                                         |
| author             | string     | Y           |               |                 |                                         |
| book_url           | string     | Y           |               | ../1221223.pdf/ | saved as pdf file                       |
| thumbnail          | string     | Y           |               | ../1221223.png/ | give a url and saved as a png file      |
| recommended_amount | int        | Y           |               | 20              | like+1<br />dislike-1                   |

## Interface Name: rent/book/add

Interface Acquisition Method: Post

URL: rent/book/add

Interface Status: completed

### Body

```json
{
    "user_id": "0000123",
    "book_id": "121223",
    "start_time":"5886868",
    "end_time": "18181818",
}
```

### Response

```json
{
    "data": {
        "reservation_id": "123123123",
    }
    "status":200,
    "msg":"ok"
}
```

| Field Name     | Field Type | Null or not | Default Value | Sample     | description                             |
| -------------- | ---------- | ----------- | ------------- | ---------- | --------------------------------------- |
| reservation_id | string     | N           |               | 12312asdad | reservation_id                          |
| status         | int        | N           |               | 200        | response result<br />(sucessful or not) |
| msg            | string     | N           |               | ok         | detail response statue                  |

## Interface Name: book/all

Interface Acquisition Method: Get

URL: book/all

Interface Status: completed

### Response

```json
{
"status": 200,
"msg":"ok",
"data": [{
    "book_id": "1231232",
    "category": "horror",
    "book_name":"histort of Roma",
    "author":"John.Smith",
    "book_url":".../xxxx.pdf",
    "thumbnail": "...../xxxx.png/",
    "recommended_amount":13
}]
}
```

| Field Name         | Field Type | Null or not | Default Value | Sample          | description                                                                       |
| ------------------ | ---------- | ----------- | ------------- | --------------- | --------------------------------------------------------------------------------- |
| status             | char       | N           |               | 200             | response result<br />(sucessful or not),jistificate if the user rent successfully |
| msg                | string     | Y           |               | ok              | detail response statue<br />to jistificate if the user rent successfully          |
| data               | list       |             |               |                 | contain the things listed below                                                   |
| category           | string     | Y           |               | horror          | searching book id based on this                                                   |
| book_id            | string     | N           | 0000000       | 1221223         | Generate by Chart                                                                 |
| book_name          | string     | Y           |               | History of Roma |                                                                                   |
| author             | string     | Y           |               |                 |                                                                                   |
| book_url           | string     | Y           |               | ../1221223.pdf/ | saved as pdf file                                                                 |
| thumbnail          | string     | Y           |               | ../1221223.png/ | give a url and saved as a png file                                                |
| recommended_amount | int        | Y           |               | 200             | Like: +1, dislike: -1                                                             |

## Interface Name: rent/book/update

Interface Acquisition Method: Post

URL: rent/book/update

Interface Status: completed

Interface desc:

### Body

```json
{
    "reservation_id":"7878",
    "user_id": "000123",
    "book_id": "1231223",
    "start_time": "123123",
    "end_time": "123123",
    "is_detete": true,
}
```

| Field Name     | Field Type | Null or not | Default value | Sample  | Description                                                                     |
| -------------- | ---------- | ----------- | ------------- | ------- | ------------------------------------------------------------------------------- |
| reservation_id | string     | N           |               | 4565363 |                                                                                 |
| user_id        | string     | Y           |               |         |                                                                                 |
| book_id        | string     | Y           |               |         |                                                                                 |
| start_time     | timestamp  | Y           |               |         |                                                                                 |
| end_time       | timestamp  | Y           |               |         |                                                                                 |
| is_delete      | boolean    | Y           |               |         | will influence the state of the book, change to"can be rent"or"can not be rent" |

### Response

```json
{
	"status": 200,
	"msg": "ok"
}
```

| Field Name | Field Type | Null or not | Default value | Sample | Description                       |
| ---------- | ---------- | ----------- | ------------- | ------ | --------------------------------- |
| status     | int        | N           |               | 200    | response result(sucessful or not) |
| msg        | string     | Y           |               | ok     | detail response statue            |

## Interface Name: User/book/Reservation

Interface Acquisition Method: Post

URL: user/book_reservation

Interface status: completed

### Body

```json
{
   "user_id": "test"
}
```

### Response

```json
{
   "status": 200,
   "msg": "ok",
   "data":[{
       "user_id":"849233",
       "user_name":"ecnusidnv",
       "reservation_id": "248924",
       "book_id":"329",
       "book_name":"vgrdtvr",
       "start_time": "3435",  //timestamp
       "end_time":"493045" // timestamp
   }]
}
```

## Interface Name: User/seat/reservation

Interface Acquisition Method: Post

URL: user/seat-reservation

Interface status: Completed

### Body

```json
{
   "user_id":"38921"
}
```

### Response

```json
{
   "status": 200,
   "msg": "ok",
   "data":{
       "user_id":"849233",
       "user_name":"ecnusidnv",
       "reservation_id": "248924",
       "seat_id":"329",
       "start_time": "3435",
       "end_time":"493045"
   }
}
```

## Interface Name: Room/all

Interface Acquisition Method: GET

URL: room/all

Interface status: Completed

### response

```json
{
    "status":200,
    "msg":"ok",
    "data": [{
        "room_id": "123",
        "room_capacity": 123,
        "reader_amount": 123,
        "room_name": 123,
        "thumbnail": ".../xxxx.png/",
        "rest_amount": 3,
        "is_available":"true"
    }]
}
```

| Field Name    | Field Type | Null or not | Default Value | Sample | description                                |
| ------------- | ---------- | ----------- | ------------- | ------ | ------------------------------------------ |
| statue        | char       | N           |               | 200    | response result<br />(sucessful or not)    |
| msg           | string     | Y           |               | ok     | detail response statue                     |
| room_id       | string     | N           | 001           | 012    | generate when created                      |
| seat_List     |            |             |               |        |                                            |
| room_capacity | int        | N           | 10            | 10     | seat amount in the room, total_seat_amount |
| reader_amount | int        | Y           |               |        | reader amount in the room                  |
| rest_amount   | int        | N           |               |        | seats available amount                     |
| is_available  | boolean    | Y           |               |        |                                            |

## Interface Name: book/comment/get

Interface Acquisition Method: POST

URL: book/comment/get

Interface Status: completed

### Body

```json
{
	"book_id": "1231231"
}
```

### Response

```json
{
    "status": 200,
    "msg":"ok",
    "data":[{
        "book_id": "1231232",
        "comment_id":"0012",
        "user_id": "002393",
        "user_name": "xxx",
        "content": "I hate backend",
        "comment_page": 134,
        "create_time": "1818"
    }]
}
```

| Field Name   | Field Type | Null or not | Default Value | Sample         | description                             |
| ------------ | ---------- | ----------- | ------------- | -------------- | --------------------------------------- |
| status       | int        | N           |               | 200            | response result<br />(sucessful or not) |
| msg          | string     | Y           |               | ok             | detail response statue                  |
| data         | list       |             |               |                | contain the things listed below         |
| book_id      | string     | N           | 0000000       | 1231232        |                                         |
| comment_id   | string     | N           | 00000         | 00010          | generate by chart                       |
| user_id      | string     | N           |               |                |                                         |
| user_name    | string     | N           |               | user           | user name                               |
| content      | string     | N           |               | I hate backend | comment to the book                     |
| comment_page | int        | Y           |               | 000015         | page number which contain this comment  |
| create_time  | timestamp  | Y           |               | 8218919        | comments create time                    |

## Interface Name: book/comment/post

Interface Acquisition Method: Post

URL: book/comment/post

Status: Completed

### Body

```json
{
    "book_id":"1231232",
    "comment_page": 13,
    "content": "I hate backend",
    "user_id": "138"
}
```

### Response

```json
{
    "status": 200,
    "msg": "ok"
}
```

## Interface Name: model/list

Interface Acquisition Method: GET

URL: model/list

Interface Status: Completed

Response:

```json
{
    "status": 200,
    "msg": "ok",
    "model_list": [{
        "model_name": "xxx",
        "model_url": "xxx",
        "model_id": "xxx",
        "thumbnail":"xxx"
    }]
}
```

| Field Name | Field Type  | Null or not | Default value | Description  |
| ---------- | ----------- | ----------- | ------------- | ------------ |
| model_id   | string      | N           |               | Model Id     |
| model_name | String      | N           |               | Model Name   |
| model_url  | String(URL) | Y           |               | URL of Model |

## Interface Name: user/model

Interface Acquisition Method: POST

URL: user/model

Interface Status: Completed

### Body:

```json
{
	"user_id": "123" // click on the book thumbnail
}
```

### Response:

```json
{
    "data": {
          "model_url": "https://xxx",
          "thumbnail": "123123"
    },
    "status": 200, 
    "msg": "OK"
}
```

| Field Name | Field Type  | Null or not | Default value | Description  |
| ---------- | ----------- | ----------- | ------------- | ------------ |
| model      | String(URL) | N           |               | URL of Model |
| thumbnail  | String      | N           |               |              |

## Interface Name: user/signup

Interface Acquisition Method: POST

URL: user/signup

Interface Status: Completed

### Body:

```json
{ 
    "user_name": "test",
    "email": "test@gmail.com",
    "password" : "XXXX",
    "avatar" : "http:xxx",
    "phone" : "9292929292929",
    "gender" : "Male",
    "birth-date" : "02/02/1990",
    "desc":"enuivbhsv"
}
```

### Response:

```json
{
    "status": 200,
    "msg": "OK"
}
```

## Interface Name: user/login

Interface Acquisition Method: GET

URL: user/login

Interface Status: Completed

### Body:

```json
{ 
    "email": "test@gmail.com",
    "password" : "XXXX"
}
```

### Response:

```json
{
    "data": {
        "user_name": "test",
        "email": "test@gmail.com",
        "password" : "XXXX",
        "avatar" : "http:xxx",
        "phone" : "9292929292929",
        "gender" : "Male",
        "birth-date" : "02/02/1990",
        "desc":"enuivbhsv"
    },
    "status": 200, 
    "msg": "OK"
}
```

| Field Name | Field Type  | Null or not | Default value | Description |
| ---------- | ----------- | ----------- | ------------- | ----------- |
| user_name  | String(URL) | Y           |               | User name   |

## Interface Name: user/update

Interface Acquisition Method: POST

URL: user/update

Interface Status: Completed

### Body:

```json
{ 
    "user_id": "123123",
    "user_name": "test",
    "password" : "XXXX",
    "avatar" : "http:xxx",
    "phone" : "9292929292929",
    "gender" : "Male",
    "birth-date" : "02/02/1990",
    "desc":"enuivbhsv"
}
```

| Field Name | Field Type  | Null or not | Default value | Description |
| ---------- | ----------- | ----------- | ------------- | ----------- |
| user_id  | String(URL) | Y           |               | User name   |


### Response:

```json
{
    "status": 200, 
    "msg": "OK"
}
```

| Field Name | Field Type  | Null or not | Default value | Description |
| ---------- | ----------- | ----------- | ------------- | ----------- |
| user_name  | String(URL) | Y           |               | User name   |


## Interface Name: book/search

Interface Acquisition Method: GET

URL: book/search

Interface Status: Completed

### Body

```json
{ 
    "search": "romance"
}
```

### Response:

```json
{
    "data": [{
      "book_id": "xxx",
      "book_name": "xxx",
      "author": "xxxx",
      "desc": "xxx",
      "thumbnail": "xxx",
    }],
    "status": 200, 
	  "msg": "OK"
}
```

| Field Name | Field Type  | Null or not | Default value | Description      |
| ---------- | ----------- | ----------- | ------------- | ---------------- |
| book_id    | string      | N           |               | Book ID          |
| desc       | string      | N           |               | Book Description |
| book_name  | String      | Y           |               | Book Name        |
| thumbnail  | string(URL) | N           |               | Image            |

## Interface Name: rent/seat/update

Interface Acquisition Method: POST

URL: rent/seat/update

Interface Status: Completed

### Body:

```json
{
    "reservation_id":"7878",
    "user_id": "000123",
    "seat_id": "1231223",
    "start_time": "123123",
    "end_time": "123123",
    "is_detete": "true",
}
```

| Field Name     | Field Type | Null or not | Default value | Sample  | Description                                                                     |
| -------------- | ---------- | ----------- | ------------- | ------- | ------------------------------------------------------------------------------- |
| reservation_id | string     | N           |               | 4565363 |                                                                                 |
| user_id        | string     | Y           |               |         |                                                                                 |
| seat_id        | string     | Y           |               |         |                                                                                 |
| start_time     | timestamp  | Y           |               |         |                                                                                 |
| end_time       | timestamp  | Y           |               |         |                                                                                 |
| is_delete      | boolean    | Y           |               |         | will influence the state of the seat and reader_amount |

### Response:

```json
{
    "status": 200, 
    "msg": "OK"
}
```

## Interface Name: rent/seat/add

Interface Acquisition Method: POST

URL: rent/seat/add

Interface Status: Completed

### Body:

```json
{ 
    "room_id": "63283",
    "user_id": "12112",
    "start_time": "123123213",
    "end_time": "12321312"
}
```

### Response:

```json
{
    "data": {
        "reservation_id": "x12312312"
    }
    "status": 200,
    "msg": "OK"
}
```
