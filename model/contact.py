from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None,id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email1=None, email2=None, email3=None,
                 all_emails_from_home_page = None,all_phones_from_home_page=None):
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
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,self.address,
                                         self.homephone, self.mobilephone,  self.workphone, self.secondaryphone,
                                         self.email1, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.address is None or other.address is None or self.address == other.address) \
               and (self.homephone is None or other.homephone is None or self.homephone == other.homephone)\
               and (self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone)\
               and (self.workphone is None or other.workphone is None or self.workphone == other.workphone)\
               and (self.secondaryphone is None or other.secondaryphone is None or self.secondaryphone == other.secondaryphone)\
               and (self.email1 is None or other.email1 is None or self.email1 == other.email1)\
               and (self.email2 is None or other.email2 is None or self.email2 == other.email2)\
               and (self.email3 is None or other.email3 is None or self.email3 == other.email3)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
