from models import Database
import random
from datetime import datetime

from repositories.SrekjaRepository import SrekjaRepository


class FillDataBase:

    @staticmethod
    def populate_database():

        # Insert Users
        users = [
            ("user1", "user1@example.com", "password1", None, "Bio 1", "Lucky Charm 1", 10, 5),
            ("user2", "user2@example.com", "password2", None, "Bio 2", "Lucky Charm 2", 15, 7),
            ("user3", "user3@example.com", "password3", None, "Bio 3", "Lucky Charm 3", 20, 10),
            ("user4", "user4@example.com", "password4", None, "Bio 4", "Lucky Charm 4", 8, 3),
            ("user5", "user5@example.com", "password5", None, "Bio 5", "Lucky Charm 5", 25, 12),
            ("user6", "user6@example.com", "password6", None, "Bio 6", "Lucky Charm 6", 30, 15),
            ("user7", "user7@example.com", "password7", None, "Bio 7", "Lucky Charm 7", 5, 2),
            ("user8", "user8@example.com", "password8", None, "Bio 8", "Lucky Charm 8", 12, 6),
            ("user9", "user9@example.com", "password9", None, "Bio 9", "Lucky Charm 9", 18, 9),
            ("user10", "user10@example.com", "password10", None, "Bio 10", "Lucky Charm 10", 22, 11)
        ]

        for user in users:
            SrekjaRepository.insert_user(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7])


        for i in range(1, 11):
            SrekjaRepository.insert_post(f"Post content {i}", random.randint(0, 50))
            SrekjaRepository.insert_image(f"https://example.com/image{i}.jpg", random.randint(1, 10))
            SrekjaRepository.insert_comment((random.randint(1, 10), None if i % 2 == 0 else random.randint(1, i), f"Comment {i}"))


        # Insert Follows
        for i in range(1, 11):
            follower = random.randint(1, 10)
            follows = random.randint(1, 10)
            while follower == follows:
                follows = random.randint(1, 10)

            SrekjaRepository.insert_follows(follower, follows)

        print("Database successfully populated with sample data.")