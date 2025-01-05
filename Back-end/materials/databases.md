# Databases

## User

- user_id (string)
- user_name (string)
- password (string)
- email (string)
- avatar (string)
- phone (string)
- create_time (timestamp)
- gender(string)
- birth_date (timestamp)
- desc(string)
- is_delete (boolean)

## Book

- book_id  (string)
- book_name  (string)
- book_url (string)
- thumbnail(string)
- author  (string)
- category  (string)
- font_amount(int)
- desc (string)
- ISBN (string)
- language (string)
- status (int)
- upload_time (timestamp)
- read_amount (int)
- comment_amount (int)
- recommended_amount (int)
- is_delete (boolean)

## Book_reservation

- user_id (string)
- book_id (string)
- create_time (timestamp)
- return_time (timestamp)
- start_time (timestamp)
- end_time (timestamp)
- is_delete (boolean)

## Comment_list

- comment_id (string)
- user_id (string)
- book_id (string)
- content (string)
- comment_page (int)
- create_time (timestamp)
- update_time (timestamp)
- delete_time (timestamp)
- is_delete (boolean)

## Reading_room

- room_id (string)
- room_name (string)
- room_capacity (int)
- reader_amount (int)
- is_delete (boolean)
- thumbnail (string)

## Seat

- room_id (string)
- seat_id (string)
- is_available (boolean)
- is_delete (boolean)

## Seat_reservation

- reservation_id (string)
- user_id (string)
- seat_id (string)
- start_time (timestamp)
- end_time (timestamp)
- create_time(timestamp)
- return_time(timestamp)
- is_delete (timestamp)

## User_Environment_Config

- user_id (string)
- environment_id (string)
- is_cat (boolean)

## Message

- user_id (string)
- content (string)
- create_time (timestamp)
- receiver_id (string)
- gesture_id (string)
- message_type (string)
- is_delete (boolean)

## Model

- model_id(string)
- model_name(string)
- model_url(string)
- create_time(timestamp)
- is_detele(boolean)
- thumbnail(string)

## User_model
- user_id(string)
- model_id(string)
- thumbnail(string)
- model_url (string)