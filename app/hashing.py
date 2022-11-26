
from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    """
    class for hashing and verifying passwords
    """
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
