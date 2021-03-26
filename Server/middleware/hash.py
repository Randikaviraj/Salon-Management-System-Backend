from Server.middleware import bcrypt

def hashPassword(password):
    pw_hash = bcrypt.generate_password_hash(password)
    return pw_hash

def passwordCheck(orginalpwd,hashpwd):
    return bcrypt.check_password_hash(hashpwd, orginalpwd)