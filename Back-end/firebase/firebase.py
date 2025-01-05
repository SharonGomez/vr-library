import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


User1 = {
    'user_id': '10001',
    'user_name': 'John Doe',
    'password': '123456',
    'email': 'john@example.com',
    'avatar': 'http://example.com/image.png',
    'phone': '+353 755634434',
    'create_time': '2020-08-17T12:00:00',
    'gender': 'male',
    'birth_date': '2000-01-01T12:00:00',
    'desc': 'A simple user.',
    'is_delete': False
}


User2 = {
    'user_id': '10002',
    'user_name': 'John Smith',
    'password': '2325t45',
    'email': 'john_smith@example.com',
    'avatar': 'http://example.com/image.png',
    'phone': '+86 13334445555',
    'create_time': '2020-08-17T12:00:00',
    'gender': 'male',
    'birth_date': '2000-01-01T12:00:00',
    'desc': 'A simple user.',
    'is_delete': False
}

User3 = {
    'user_id': '10003',
    'user_name': 'Arnold Doe',
    'password': 'a123456',
    'email': 'arnold@example.com',
    'avatar': 'http://example.com/image.png',
    'phone': '+353 435654324',
    'create_time': '2020-08-17T12:00:00',
    'gender': 'male',
    'birth_date': '2000-01-01T12:00:00',
    'desc': 'A simple user.',
    'is_delete': False
}

book1 = {
    'book_id': '1000001',
    'book_name': 'historty of Roma',
    'book_url': 'http://example.com/book.pdf',
    'thumbnail': 'http://example.com/thumbnail.png',
    'author': 'John Doe',
    'category': 'Fiction',
    'font_amount': 234,
    'desc': 'A good book.',
    'ISBN': '978-3-16-148410-0',
    'language': 'English',
    'status': 1,
    'upload_time': '2020-08-17T12:00:00',
    'read_amount': 0,
    'comment_amount': 0,
    'recommended_amount': 0,
    'is_delete': False
}

book2 = {
    'book_id': '12345',
    'book_name': 'Book Title',
    'book_url': 'http://example.com/book.pdf',
    'thumbnail': 'http://example.com/thumbnail.png',
    'author': 'John Doe',
    'category': 'Fiction',
    'font_amount': 234,
    'desc': 'A good book.',
    'ISBN': '978-3-16-148410-0',
    'language': 'English',
    'status': 1,
    'upload_time': '2020-08-17T12:00:00',
    'read_amount': 0,
    'comment_amount': 0,
    'recommended_amount': 0,
    'is_delete': False
}
book3 = {
    'book_id': '1000003',
    'book_name': 'To Kill a Mockingbird',
    'book_url': 'https://www.gutenberg.org/files/218/218-h/218-h.htm',
    'thumbnail': 'https://covers.openlibrary.org/b/id/555230-S.jpg',
    'author': 'Harper Lee',
    'category': 'Fiction',
    'font_amount': 281,
    'desc': 'To Kill a Mockingbird is a novel by Harper Lee published in 1960. It is set in the 1930s in Maycomb, a fictional town in Alabama. The novel explores themes of racism and injustice through the eyes of Scout Finch, a young girl who grows up in the town.',
    'ISBN': '978-0-446-31078-0',
    'language': 'English',
    'status': 1,
    'upload_time': '2020-12-01T10:30:00',
    'read_amount': 3456,
    'comment_amount': 70,
    'recommended_amount': 120,
    'is_delete': False
}

book4 = {
    'book_id': '1000004',
    'book_name': '1984',
    'book_url': 'https://www.gutenberg.org/files/1984/1984-pdf.pdf',
    'thumbnail': 'https://covers.openlibrary.org/b/id/7222246-S.jpg',
    'author': 'George Orwell',
    'category': 'Fiction',
    'font_amount': 328,
    'desc': "1984 is a dystopian novel by George Orwell published in 1949. The novel is set in a totalitarian society in which the government exercises total control over every aspect of citizens' lives. The novel explores themes of government oppression, propaganda, and the power of language.",
    'ISBN': '978-0-452-28423-4',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-01-15T16:45:00',
    'read_amount': 5678,
    'comment_amount': 150,
    'recommended_amount': 300,
    'is_delete': False
}

book5 = {
    'book_id': '1000005',
    'book_name': 'Pride and Prejudice',
    'book_url': 'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm',
    'thumbnail': 'https://www.penguin.com.au/books/pride-and-prejudice-9780141949055',
    'author': 'Jane Austen',
    'category': 'Fiction',
    'font_amount': 321,
    'desc': 'Pride and Prejudice is a novel by Jane Austen published in 1813. The novel is set in rural England in the late 18th century and follows the Bennet family, particularly the second eldest daughter Elizabeth, as she navigates the social mores of the time in her search for love and marriage.',
    'ISBN': '978-1-62793-415-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-02-07T08:15:00',
    'read_amount': 1234,
    'comment_amount': 30,
    'recommended_amount': 80,
    'is_delete': False
}
book6 = {
    'book_id': '1000006',
    'book_name': 'The Great Gatsby',
    'book_url': 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm',
    'thumbnail': 'https://cloud.firebrandtech.com/api/v2/img/111/9780785839996/XL',
    'author': 'F. Scott Fitzgerald',
    'category': 'Fiction',
    'font_amount': 180,
    'desc': 'The Great Gatsby is a novel by F. Scott Fitzgerald published in 1925. Set in the Roaring Twenties, the story follows the enigmatic Jay Gatsby as he tries to win back his lost love, Daisy Buchanan, while navigating the shallow and corrupt world of the wealthy elite.',
    'ISBN': '978-0-7432-7356-5',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-02-15T12:00:00',
    'read_amount': 5678,
    'comment_amount': 120,
    'recommended_amount': 220,
    'is_delete': False
}

book7 = {
    'book_id': '1000007',
    'book_name': '1984',
    'book_url': 'https://www.gutenberg.org/files/1984/1984-h/1984-h.htm',
    'thumbnail': 'https://www.deviantart.com/saltedm8/art/1984-Book-Cover-740855970',
    'author': 'George Orwell',
    'category': 'Science Fiction',
    'font_amount': 328,
    'desc': '1984 is a dystopian novel by George Orwell published in 1949. Set in a future totalitarian society, the story follows Winston Smith as he rebels against the Party and falls in love with fellow rebel Julia, but ultimately succumbs to the all-seeing eye of Big Brother.',
    'ISBN': '978-0-451-52493-5',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-04-20T15:30:00',
    'read_amount': 9876,
    'comment_amount': 230,
    'recommended_amount': 320,
    'is_delete': False
}

book8 = {
    'book_id': '1000008',
    'book_name': 'The Lord of the Rings',
    'book_url': 'https://www.gutenberg.org/files/120/120-h/120-h.htm',
    'thumbnail': 'https://wendyvancamp.files.wordpress.com/2014/02/the-lord-of-the-rings-book-cover.jpg',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 1178,
    'desc': 'The Lord of the Rings is an epic high fantasy novel by J.R.R. Tolkien published in 1954. Set in the fictional world of Middle-earth, the story follows hobbit Frodo Baggins as he sets out to destroy the One Ring, while facing challenges from various allies and enemies along the way.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 5678,
    'comment_amount': 180,
    'recommended_amount': 280,
    'is_delete': False
}

book9 = {
    'book_id': '1000009',
    'book_name': 'The Hobbit',
    'book_url': 'https://ia803100.us.archive.org/7/items/TheHobbitEnhancedEditionJ.R.R.Tolkien/The%20Hobbit%20%28Enhanced%20Edition%29%20-%20J.%20R.%20R.%20Tolkien.pdf',
    'thumbnail': 'https://ahmadataka.files.wordpress.com/2013/01/the-hobbit.jpg',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 310,
    'desc': 'The Hobbit is a children\'s fantasy novel by J.R.R. Tolkien published in 1937. Set in Middle-earth, the story follows hobbit Bilbo Baggins as he is recruited by wizard Gandalf to help a group of dwarves reclaim their home and treasure from a dragon named Smaug.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 1234,
    'comment_amount': 56,
    'recommended_amount': 78,
    'is_delete': False
}

book10 = {
    'book_id': '1000010',
    'book_name': 'The Fellowship of the Ring',
    'book_url': 'https://ia601003.us.archive.org/3/items/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf/j-r-r-tolkien-lord-of-the-rings-01-the-fellowship-of-the-ring-retail-pdf.pdf',
    'thumbnail': 'https://tolkiengateway.net/wiki/File:Fellowship_extended.jpg',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 423,
    'desc': 'The Fellowship of the Ring is an epic high fantasy novel by J.R.R. Tolkien published in 1954. Set in Middle-earth, the story follows hobbit Frodo Baggins as he sets out to destroy the One Ring, while facing challenges from various allies and enemies along the way.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 5678,
    'comment_amount': 180,
    'recommended_amount': 280,
    'is_delete': False
}

book11 = {
    'book_id': '1000003',
    'book_name': 'The Two Towers',
    'book_url': 'https://gosafir.com/mag/wp-content/uploads/2019/12/Tolkien-J.-The-lord-of-the-rings-HarperCollins-ebooks-2010.pdf',
    'thumbnail': 'https://static.wikia.nocookie.net/lotr/images/9/9b/The_Two_Towers_1st_edition_cover.jpg/revision/latest?cb=20190917134803',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 352,
    'desc': 'The Two Towers is an epic high fantasy novel by J.R.R. Tolkien published in 1954. Set in Middle-earth, the story continues from where The Fellowship of the Ring left off and follows hobbit Frodo Baggins as he continues his quest to destroy the One Ring.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 3456,
    'comment_amount': 90,
    'recommended_amount': 150,
    'is_delete': False
}

book12 = {
    'book_id': '1000012',
    'book_name': 'The Catcher in the Rye',
    'book_url': 'http://giove.isti.cnr.it/demo/eread/Libri/sad/Rye.pdf',
    'thumbnail': 'https://en.wikipedia.org/wiki/File:The_Catcher_in_the_Rye_(1951,_first_edition_cover).jpg',
    'author': 'J.D. Salinger',
    'category': 'Fiction',
    'font_amount': 234,
    'desc': 'The Catcher in the Rye is a novel by J.D. Salinger published in 1951. It tells the story of Holden Caulfield, a teenage boy who has been expelled from his prep school and is wandering around New York City.',
    'ISBN': '978-0-316-76953-6',
    'language': 'English',
    'status': 1,
    'upload_time': '2020-12-01T10:30:00',
    'read_amount': 2345,
    'comment_amount': 67,
    'recommended_amount': 120,
    'is_delete': False
}

book13 = {
    'book_id': '1000013',
    'book_name': 'The Great Gatsby',
    'book_url':'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm', 
    'thumbnail':'https://en.wikipedia.org/wiki/File:The_Great_Gatsby_Cover_1925_Retouched.jpg',
    'author':'F. Scott Fitzgerald',
    'category':'Fiction',
    'font_amount': 256,
    'desc':'The Great Gatsby is a novel by F. Scott Fitzgerald published in 1925. It tells the story of Jay Gatsby, a wealthy man who throws lavish parties in hopes of winning back his former love, Daisy Buchanan.',
    'ISBN':'978-0-7432-7356-5',
    'language':'English',
    'status':1,
    'upload_time':'2020-12-01T10:30:00',
    'read_amount':3456,
    'comment_amount':70,
    'recommended_amount':120,
    'is_delete':False
}

book14 = {
    'book_id':'1000014',
    'book_name':'1984',
    'book_url':'https://www.gutenberg.org/files/1984/1984-h/1984-h.htm', 
    'thumbnail':'https://covers.openlibrary.org/b/id/7222246-S.jpg',
    'author':'George Orwell',
    'category':'Fiction',
    'font_amount':256,
    'desc':'1984 is a dystopian novel by George Orwell published in 1949. It tells the story of Winston Smith, a man living in a totalitarian society where individuality and independent thinking are forbidden.',
    'ISBN':'978-0-14-103614-4',
    'language':'English',
    'status':1,
    'upload_time':'2020-12-01T10:30:00',
    'read_amount':3456,
    'comment_amount':70,
    'recommended_amount':120,
    'is_delete':False
}

book15 = {
    'book_id': '1000015',
    'book_name': 'The Silmarillion',
    'book_url': 'https://ia802804.us.archive.org/5/items/TheSilmarillionIllustratedJ.R.R.TolkienTedNasmith/The%20Silmarillion%20%28Illustrated%29%20-%20J.%20R.%20R.%20Tolkien%3B%20Ted%20Nasmith%3B.pdf',
    'thumbnail': 'https://en.wikipedia.org/wiki/The_Silmarillion#/media/File:Silmarillion.png',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 365,
    'desc': 'The Silmarillion is a collection of mythopoeic works by J.R.R. Tolkien published posthumously in 1977. It tells the story of the creation of Middle-earth and its inhabitants, including elves, dwarves, and men.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 789,
    'comment_amount': 23,
    'recommended_amount': 45,
    'is_delete': False
}

book16 = {
    'book_id': '1000016',
    'book_name': 'The Children of Hurin',
    'book_url': 'https://archive.org/stream/J.R.R.TolkienTheChildrenOfHurin/J.R.R.Tolkien+-+The+Children+of+Hurin_djvu.txt',
    'thumbnail': 'https://upload.wikimedia.org/wikipedia/en/8/85/The_Children_of_Hurin_cover.jpg',
    'author': 'J.R.R. Tolkien',
    'category': 'Fantasy',
    'font_amount': 365,
    'desc': 'The Children of Hurin is an epic high fantasy novel by J.R.R. Tolkien published posthumously in 2007. It tells the story of Turin Turambar and his sister Nienor as they struggle against the evil Morgoth in Middle-earth.',
    'ISBN': '978-0-618-34625-3',
    'language': 'English',
    'status': 1,
    'upload_time': '2021-08-05T09:00:00',
    'read_amount': 2345,
    'comment_amount': 67,
    'recommended_amount': 120,
    'is_delete': False
}

book17 = {
    "book_id": "1000017",
    "book_name": "The Wise Man's Fear",
    "book_url": "https://www.scribd.com/document/75732781/Patrick-Rothfuss-King-Killer-Chronicle-02-The-Wise-Mans-Fear",
    "thumbnail": "https://en.wikipedia.org/wiki/The_Wise_Man%27s_Fear#/media/File:The_Wise_Man's_Fear.jpg",
    "author": "Patrick Rothfuss",
    "category": "Fantasy Fiction",
    "font_amount": 256,
    "desc": "The Wise Man's Fear is a fantasy novel by Patrick Rothfuss published in 2011. It is the second book in The Kingkiller Chronicle series and continues the story of Kvothe as he travels to the court of Maer Alveron in Vintas.",
    "ISBN": "978-0-7564-0474-1",
    "language": "English",
    "status": 1,
    "upload_time": "2020-12-01T10:30:00",
    "read_amount": 2345,
    "comment_amount": 67,
    "recommended_amount": 120,
    'is_delete':False
}
book18 = { 
    "book_id": "1000018", 
    "book_name": "To Kill a Mockingbird", 
    "book_url": "https://giove.isti.cnr.it/demo/eread/libri/angry/mockingbird.pdf", 
    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/7/79/To_Kill_a_Mockingbird.JPG", 
    "author": "Harper Lee", 
    "category": "Fiction", 
    "font_amount": 200, 
    "desc": "To Kill a Mockingbird is a novel by Harper Lee published in 1960. It is set in the Deep South and explores themes of racial injustice and the loss of innocence.", 
    "ISBN": "0-892-55411-9", 
    "language": "English", 
    "status": 1, 
    "upload_time": "2020-01-01T12:00:00", 
    "read_amount": 10000, 
    "comment_amount": 500, 
    "recommended_amount": 500, 
    'is_delete':False 
}
book19 = {
    "book_id": "1000019", 
    "book_name": "The Alchemist", 
    "book_url": "https://ia601006.us.archive.org/13/items/OceanofPDF.comTheAlchemist/_OceanofPDF.com_The_Alchemist.pdf", 
    "thumbnail": "https://images.app.goo.gl/miVhevoNs5sozVjU7", 
    "author": "Paulo Coelho", 
    "category": "Fiction", 
    "font_amount": 120, 
    "desc": "The Alchemist is a novel by Paulo Coelho published in 1988. It is a philosophical tale about a shepherd boy who sets out to fulfill his dreams and discovers the true meaning of life.", 
    "ISBN": "978-0062315007", 
    "language": "English", 
    "status": 1, 
    "upload_time": 
    "2020-05-01T12:00:00", 
    "read_amount": 15000, 
    "comment_amount": 1000, 
    "recommended_amount": 800, 
    "is_delete": False
}

book20 = {
    "book_id": "1000020", 
    "book_name": "The Power of Now", 
    "book_url": "https://ia601000.us.archive.org/33/items/ThePowerOfNowEckhartTolle_201806/The%20Power%20Of%20Now%20-%20Eckhart%20Tolle.pdf", 
    "thumbnail": "https://images.app.goo.gl/NEP8p2fAN6WyUh689", 
    "author": "Eckhart Tolle", 
    "category": "Non-fiction", 
    "font_amount": 90, 
    "desc": "The Power of Now is a self-help book by Eckhart Tolle published in 1997. It explores the importance of living in the present moment and letting go of negative thoughts.", 
    "ISBN": "978-1577314806", 
    "language": "English", 
    "status": 1, "upload_time": 
    "2020-06-01T12:00:00", 
    "read_amount": 8000, 
    "comment_amount": 500, 
    "recommended_amount": 300, 
    "is_delete": False
}

book21 = {
    "book_id": "1000021", 
    "book_name": "Thinking, Fast and Slow", 
    "book_url": "https://ia600808.us.archive.org/14/items/DanielKahnemanThinkingFastAndSlow/Daniel%20Kahneman-Thinking%2C%20Fast%20and%20Slow%20%20.pdf", 
    "thumbnail": "https://images.app.goo.gl/CoioV2WmK5C1qcUu8", 
    "author": "Daniel Kahneman", 
    "category": "Non-fiction", 
    "font_amount": 250, 
    "desc": "Thinking, Fast and Slow is a book by Daniel Kahneman published in 2011. It explores how the human mind processes information and makes decisions, and challenges traditional assumptions about rationality.", 
    "ISBN": "978-0374275631", 
    "language": "English", 
    "status": 1, 
    "upload_time": "2020-07-01T12:00:00", 
    "read_amount": 6000, 
    "comment_amount": 400, 
    "recommended_amount": 200, 
    "is_delete": False
}


Book_reservation = {
    'user_id': '12345',
    'book_id': '12345',
    'create_time': '2020-08-17T12:00:00',
    'return_time': '2020-09-17T12:00:00',
    'start_time': '2020-08-18T12:00:00',
    'end_time': '2020-09-17T12:00:00',
    'is_delete': False
}

Comment_list = {
    "comment_id": "123",
    "user_id": "456",
    "book_id": "789",
    "content": "test content",
    "comment_page": 1,
    "create_time": "2020-04-01 00:00:00",
    "update_time": "2020-04-01 00:00:00",
    "delete_time": "2020-04-01 00:00:00",
    "is_delete": False
}

Reading_room1 = {
    "room_id": "101",
    "room_name": "Reading room 1",
    "room_capacity": 4,
    "reader_amount": 2,
    "is_delete": False,
    "thumbnail" : "https://images.unsplash.com/photo-1496664444929-8c75efb9546f"
}

Reading_room2 = {
    "room_id": "102",
    "room_name": "Reading room 2",
    "room_capacity": 4,
    "reader_amount": 2,
    "is_delete": False,
    "thumbnail" : "https://images.unsplash.com/photo-1496664444929-8c75efb9546f"
}

Seat = {
    "room_id": "123",
    "seat_id": "456",
    "is_available": True,
    "is_delete": False
}

Seat_reservation = {
    "reservation_id": "123",
    "user_id": "456",
    "seat_id": "789",
    "start_time": "2020-04-01 00:00:00",
    "end_time": "2020-04-02 00:00:00",
    "is_delete": False
}

User_environment_config1 = {
    "user_id": "123",
    "environment_id": "456",
    "is_cat": True
}

User_environment_config2 = {
    "user_id": "123",
    "environment_id": "456",
    "is_cat": True
}

User_environment_config3 = {
    "user_id": "123",
    "environment_id": "456",
    "is_cat": True
}

User_environment_config4 = {
    "user_id": "123",
    "environment_id": "456",
    "is_cat": True
}

User_environment_config5 = {
    "user_id": "123",
    "environment_id": "456",
    "is_cat": True
}

Message = {
    "user_id": "123",
    "content": "test message",
    "create_time": "2020-04-01 00:00:00",
    "receiver_id": "456",
    "gesture_id": "789",
    "message_type": "test type",
    "is_delete": False
}

Model = {
    "model_id": "123",
    "model_name": "test model",
    "model_url": "https://www.test.com",
    "create_time": "2020-04-01 00:00:00",
    "is_detele": False
}


def create_collection(coll_name, doc_obj):
    collection_ref = db.collection(coll_name)
    doc_ref = collection_ref.document()
    doc_ref.set(doc_obj)


if __name__ == '__main__':
    # for i in [book1, book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20]:
    #     create_collection("Book", i)


# create_collection("User_environment_config",User_environment_config)
  for i in [User_environment_config1,User_environment_config2,User_environment_config3,User_environment_config4,User_environment_config5 ]:
    create_collection("User_environment_config",i)
    # for i in [User1,User2,User3]:
    #     create_collection("user",i)
    print("finished")
