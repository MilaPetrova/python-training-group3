from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                         self.homephone, self.mobilephone,  self.workphone, self.secondaryphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.homephone is None or other.homephone is None or self.homephone == other.homephone)\
               and (self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone)\
               and (self.workphone is None or other.workphone is None or self.workphone == other.workphone)\
               and (self.secondaryphone is None or other.secondaryphone is None or self.secondaryphone == other.secondaryphone)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
