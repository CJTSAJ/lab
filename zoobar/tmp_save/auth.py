from zoodb import *
from debug import *

import hashlib
import random

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput.encode('utf-8')).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = person_setup()
    person = db.query(Person).get(username)

    cred_db = cred_setup()
    cred = cred_db.query(Cred).get(username)
    if not person:
        return None
    if cred.password == password:
        return newtoken(cred_db, cred)
    else:
        return None

def register(username, password):
    db = person_setup()
    cred_db = cred_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username

    newcred = Cred()
    newcred.username = username
    newcred.password = password

    db.add(newperson)
    db.commit()

    cred_db.add(newcred)
    cred_db.commit()
    return newtoken(cred_db, newcred)
    #return True

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

def get_cred(username, password):
    db_cred = cred_setup()
    cred = db_cred.query(Cred).get(username)
    if cred:
        return newtoken(db_cred, cred)
    else:
        return None
def create_cred(username, password):
    db_cred = cred_setup()
    cred = db_cred.query(Cred).get(username)
    if cred:
        return None
    newcred = Cred()
    newcred.username = username
    newcred.passwd = password
    db_cred.add(newcred)
    db_cred.commit()
 
    return newtoken(db_cred, newcred)    
    
