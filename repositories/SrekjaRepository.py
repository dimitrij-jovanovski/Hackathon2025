from models.Database import Database


class SrekjaRepository:

    @staticmethod
    def initialize_database():

        db = Database()


        db.execute('''
                       CREATE TABLE IF NOT EXISTS Users (
                           user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT UNIQUE NOT NULL,
                           email TEXT UNIQUE NOT NULL,
                           password TEXT NOT NULL,
                           profile_picture_url TEXT DEFAULT NULL,
                           bio TEXT DEFAULT NULL,
                           luck_charm TEXT DEFAULT NULL,
                           followers_count INTEGER DEFAULT NULL,
                           following_count INTEGER DEFAULT NULL,
                           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )
                   ''')

        db.execute('''
                        CREATE TABLE IF NOT EXISTS Posts (
                             post_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             user_id INTEGER NOT NULL,
                             text TEXT NOT NULL,
                             likes INTEGER DEFAULT 0,
                             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                             FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
                        )
                    ''')

        db.execute('''
                        CREATE TABLE IF NOT EXISTS PostImages (
                            image_id INTEGER PRIMARY KEY,
                            image_url TEXT DEFAULT NULL,
                            post_id INTEGER NOT NULL,
                            FOREIGN KEY (post_id) REFERENCES Posts(post_id) ON DELETE SET NULL ON UPDATE CASCADE
                        )
                    ''')

        db.execute('''
                        CREATE TABLE IF NOT EXISTS PostComments (
                            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            post_id INTEGER NOT NULL,
                            parent_id INTEGER DEFAULT NULL, -- NULL for top-level comments
                            text TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (post_id) REFERENCES Posts(post_id) ON DELETE SET NULL ON UPDATE CASCADE,
                            FOREIGN KEY (parent_id) REFERENCES PostComments(comment_id) ON DELETE SET NULL ON UPDATE CASCADE
                        )
                    ''')


        db.execute('''
                        CREATE TABLE IF NOT EXISTS Follows (
                            follow_id INTEGER PRIMARY KEY,
                            follower_user_id INTEGER NOT NULL,
                            follows_user_id INTEGER NOT NULL,
                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (follower_user_id) REFERENCES Users(user_id) ON DELETE SET NULL ON UPDATE CASCADE,
                            FOREIGN KEY (follows_user_id) REFERENCES Users(user_id) ON DELETE SET NULL ON UPDATE CASCADE
                         )
                    ''')

        db.commit()

    @staticmethod
    def insert_user(username, email, password, profile_picture_url, bio, luck_charm, followers_count, following_count):
        db = Database()
        db.execute('''
                INSERT INTO Users (username, email, password, profile_picture_url, bio, luck_charm, followers_count, following_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (username, email, password, profile_picture_url, bio, luck_charm, followers_count, following_count))
        db.commit()

    @staticmethod
    def insert_post(user_id, text, likes):
        db = Database()
        db.execute('''
                INSERT INTO Posts (user_id, text, likes) 
                VALUES (?, ?, ?)
            ''', (user_id, text, likes))
        db.commit()

    @staticmethod
    def insert_image(image_url, post_id):
        db = Database()
        db.execute('''
                INSERT INTO PostImages (image_url, post_id) 
                VALUES (?, ?)
            ''', (image_url, post_id))
        db.commit()

    @staticmethod
    def insert_comment(post_id, parent_id, text):
        db = Database()
        db.execute('''
                        INSERT INTO PostComments (post_id, parent_id, text)
                        VALUES (?, ?, ?)
                    ''', (post_id, parent_id, text))
        db.commit()

    @staticmethod
    def insert_follows(follower_user_id, follows_user_id):
        db = Database()
        db.execute('''
                INSERT INTO Follows (follower_user_id, follows_user_id)
                VALUES (?, ?)
            ''', (follower_user_id, follows_user_id))
        db.commit()