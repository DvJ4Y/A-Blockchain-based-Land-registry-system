import MySQLdb as mysqldb
from MySQLdb.cursors import DictCursor
from warnings import filterwarnings

filterwarnings('ignore', category=mysqldb.Warning)

APPLICATION_PENDING_CODE = 0
APPLICATION_REJECTED_CODE = 1
APPLICATION_VERIFIED_CODE = 2


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "password"
DB_NAME = "land_registry"

TABLE_OWNER = "owner"
TABLE_PROPERTY = "property"
TABLE_APPLICATION = "application"

OWNER_ID = "id"
OWNER_PROPERTY = "property"
OWNER_PROPERTY_VERIFIED = "is_verified"

PROPERTY_TOKEN = "property"
PROPERTY_VALIDITY = "is_valid"

APPLICATION_USER_ID = "user_id"
APPLICATION_PROPERTY = "property"
APPLICATION_VERIFIED = "ownership_verified"


OWNER_ID_PROP = "VARCHAR(64) NOT NULL"
OWNER_PROPERTY_PROP = "VARCHAR(100) UNIQUE NOT NULL"
OWNER_PROPERTY_VERIFIED_PROP = "BOOLEAN NOT NULL DEFAULT FALSE"

PROPERTY_TOKEN_PROP = "VARCHAR(100) UNIQUE NOT NULL"
PROPERTY_VALIDITY_PROP = "BOOLEAN NOT NULL DEFAULT FALSE"

APPLICATION_USER_ID_PROP = "VARCHAR(64) NOT NULL"
APPLICATION_PROPERTY_PROP = "VARCHAR(100) UNIQUE NOT NULL"
# default is 0 where 0 - pending, 1 - rejected, 2 - verified
APPLICATION_VERIFIED_PROP = "INTEGER NOT NULL DEFAULT 0"


owner_create_query = """CREATE TABLE IF NOT EXISTS %(TABLE_OWNER)s
                        (%(OWNER_ID)s %(OWNER_ID_PROP)s,
                         %(OWNER_PROPERTY)s %(OWNER_PROPERTY_PROP)s,
                         %(OWNER_PROPERTY_VERIFIED)s %(OWNER_PROPERTY_VERIFIED_PROP)s);
                         """ % (locals())

property_create_query = """CREATE TABLE IF NOT EXISTS %(TABLE_PROPERTY)s
                           (%(PROPERTY_TOKEN)s %(PROPERTY_TOKEN_PROP)s,
                            %(PROPERTY_VALIDITY)s %(PROPERTY_VALIDITY_PROP)s);
                            """ % (locals())

application_create_query = """CREATE TABLE IF NOT EXISTS %(TABLE_APPLICATION)s
                              (%(APPLICATION_USER_ID)s %(APPLICATION_USER_ID_PROP)s,
                               %(APPLICATION_PROPERTY)s %(APPLICATION_PROPERTY_PROP)s,
                               %(APPLICATION_VERIFIED)s %(APPLICATION_VERIFIED_PROP)s);
                               """ % (locals())


class DatabaseMan(object):

    def __init__(self):

        db = mysqldb.connect(host=DB_HOST,
                             user=DB_USER,
                             passwd=DB_PASSWORD,
                             cursorclass=DictCursor,
                             db=DB_NAME)

        cur = db.cursor()

        self.db = db
        self.cur = cur

        initial_queries = (owner_create_query,
                           property_create_query,
                           application_create_query)

        for query in initial_queries:

            self.cur.execute(query)

        self.db.commit()

    def newApplication(self, id, property):

        new_application_query = """INSERT INTO %(TABLE_APPLICATION)s
                                   (%(APPLICATION_USER_ID)s, %(APPLICATION_PROPERTY)s)
                                   VALUES
                                   ("%(id)s", "%(property)s");""" % (dict(globals(), **locals()))

        try:
            self.cur.execute(new_application_query)
            self.db.commit()

        except:
            pass

    def getOwnerProperties(self, id):

        get_property_query = """SELECT * FROM %(TABLE_OWNER)s
                                WHERE
                                %(OWNER_ID)s = "%(id)s";
                                """ % (dict(locals(), **globals()))

        try:
            self.cur.execute(get_property_query)
            self.db.commit()

            ownerPropertiesDict = self.cur.fetchall()

            return ownerPropertiesDict

        except:
            pass

    def getAllPendingApplications(self):

        get_application_query = """SELECT * FROM %(TABLE_APPLICATION)s
                                   WHERE
                                   %(APPLICATION_VERIFIED)s = False;
                                """ % (dict(locals(), **globals()))

        try:
            self.cur.execute(get_application_query)
            self.db.commit()

            pendingApplicationsAllDict = self.cur.fetchall()

            return pendingApplicationsAllDict

        except:
            pass

    def getApplications(self, id):

        get_application_query = """SELECT * FROM %(TABLE_APPLICATION)s
                                   WHERE
                                   %(APPLICATION_USER_ID)s = "%(id)s"
                                   AND
                                   %(APPLICATION_VERIFIED)s = "%(APPLICATION_PENDING_CODE)s";
                                   """ % (dict(locals(), **globals()))

        try:
            self.cur.execute(get_application_query)
            self.db.commit()

            applicationPropertiesDict = self.cur.fetchall()

            return applicationPropertiesDict

        except:
            pass

    def verifyApplication(self, id, property):

        verify_application_query = """UPDATE %(TABLE_APPLICATION)s
                                      SET %(APPLICATION_VERIFIED)s = %(APPLICATION_VERIFIED_CODE)s
                                      WHERE
                                      %(APPLICATION_USER_ID)s = "%(id)s"
                                      AND
                                      %(APPLICATION_PROPERTY)s = "%(property)s"
                                      """ % (dict(globals(), **locals()))

        owner_update_query = """INSERT INTO %(TABLE_OWNER)s
                                (%(OWNER_ID)s, %(OWNER_PROPERTY)s, %(OWNER_PROPERTY_VERIFIED)s)
                                VALUES
                                ("%(id)s", "%(property)s", True)
                                """ % (dict(globals(), **locals()))

        try:
            self.cur.execute(verify_application_query)
            self.cur.execute(owner_update_query)

            self.db.commit()

        except:
            pass

    def rejectApplication(self, id, property):

        reject_application_query = """UPDATE %(TABLE_APPLICATION)s
                                      SET %(APPLICATION_VERIFIED)s = %(APPLICATION_REJECTED_CODE)s
                                      WHERE
                                      %(APPLICATION_USER_ID)s = "%(id)s"
                                      AND
                                      %(APPLICATION_PROPERTY)s = "%(property)s";
                                      """ % (dict(globals(), **locals()))

        owner_update_query = """INSERT INTO %(TABLE_OWNER)s
                                (%(OWNER_ID)s, %(OWNER_PROPERTY)s, %(OWNER_PROPERTY_VERIFIED)s)
                                VALUES
                                ("%(id)s", "%(property)s", False);
                                """ % (dict(globals(), **locals()))

        try:
            self.cur.execute(reject_application_query)
            self.cur.execute(owner_update_query)
            self.db.commit()

        except:
            pass
