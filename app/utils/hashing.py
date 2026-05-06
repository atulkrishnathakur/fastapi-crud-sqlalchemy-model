from pwdlib import PasswordHash

class Hash:
    @staticmethod # static method is good for helper functions
    def create_hash(password: str):
        password_hash = PasswordHash.recommended()
        hashed_pwd = password_hash.hash(password)
        return hashed_pwd
