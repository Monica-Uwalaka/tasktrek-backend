import bcrypt

def get_hashed_password(password: str) -> str:
  """
  returns str representation of the hashed password
  """
  hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt(10))
  return hashed_password.decode("utf-8")

def verify_password(password, hashed_password):
  if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode()):
    return True
  else:
    return False