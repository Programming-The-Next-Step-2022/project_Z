import os

import bcrypt


class SetupKey:

    def __init__(self):
        """
        If the person uses the program for the first time, they are asked to
        give a master key. If this is not the first login, the master key that
        has been previously given will be used.
        """
        try:
            key_file = open("key.txt", "rb")
            self.key = key_file.read()
            key_file.close()
        except (OSError, IOError) as e:
            key_file = open("key.txt", "w+")
            self.key = self.init_key()




        # with open("key.txt", "rb") as key_file:
        #     # print(key_file.read().decode( "utf-8" ))
        #     if os.stat("key.txt").st_size == 0:
        #         self.key = self.init_key()
        #     else:
        #         self.key = key_file.read()


    def init_key(self):
        """
        Initialize a master key and save it in a textfile

        :return: str the master key
        """
        key = input("Please choose a master password: ")
        key_repeat = input("Please type your master password again: ")

        # Only save the key if the user has entered the same password the
        # second time
        if self.validate_key(key, key_repeat):
            hashed_key = self.get_hashed_password(key)
            with open("key.txt", "wb") as key_file:
                key_file.write(hashed_key)

        return self.get_hashed_password(key)

    def validate_key(self, key, key_repeat):
        """
        Check if the user has given two times the same key

        :param key: str key
        :param key_repeat: str second key
        :return: boolean if the two given keys are the same
        """
        while True:
            if key != key_repeat:
                key_repeat = input(
                    "The master password is not the same, please try"
                    " again! ")
            else:
                break
        return True

    def get_hashed_password(self, password):
        """
        Hash a password
        :param password: str containing the password to be hashed

        :return: hashed password
        """

        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

