def validatepassword(new, confirm):
  password,confirmpassword = None,None
  if len(new.value)<=5 or hasplaceholder(new):password="password must be above 5 characters"
  if confirm.value != new.value:confirmpassword="passwords do not match"
  return password,confirmpassword
