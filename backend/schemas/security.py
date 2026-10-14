from passlib.context import CryptContext
#pwd_context is used to hash and verify passwords using the bcrypt algorithm. It provides a secure way to store passwords in the database.
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
#crypt context is a utility that provides methods for hashing and verifying passwords. It uses the bcrypt algorithm to securely hash passwords before storing them in the database. The deprecated="auto" argument ensures that any deprecated hashing algorithms are automatically handled and updated to the recommended ones.
#crypt context parameters are 
#   schemes: A list of hashing algorithms to use.
#   deprecated: How to handle deprecated algorithms.
#we use crypt context cause we can easily switch to a different hashing algorithm in the future if needed, without having to change the code that uses it. It also provides a consistent interface for hashing and verifying passwords, making it easier to maintain and test the code.
def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )