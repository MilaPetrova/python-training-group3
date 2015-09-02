from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.home is None or other.home is None or self.home == other.home)\
               and (self.mobile is None or other.mobile is None or self.mobile == other.mobile)\
               and (self.work is None or other.work  is None or self.work  == other.work)\
               and (self.fax is None or other.fax  is None or self.fax  == other.fax)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
