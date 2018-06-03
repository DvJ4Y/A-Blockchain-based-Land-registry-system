from hashlib import sha256
from textwrap import dedent
from time import sleep
from os import system

# project imports
import database as dbLib


def aadhaarInput():

    aadhaar = raw_input("Enter Your Aadhaar Number: ").strip()

    try:
        # Is it a number at all?
        assert int(aadhaar)

        if len(aadhaar) == 12:
            return aadhaar
        else:
            raise ValueError

    except ValueError:
        print "Invalid Number! Enter Again."
        print
        return aadhaarInput()

def showProperties(dbMan):

    ownedProperties = dbMan.getOwnerProperties(userId)

    pendingProperties = dbMan.getApplications(userId)

    print "Your Properties' Digital Identities:"
    print

    try:
        for index, _property in enumerate(pendingProperties):

            print "%s - %s : Verification Pending" % (index + 1, _property[dbLib.APPLICATION_PROPERTY])

    except:
        pass

    try:
        for index, _property in enumerate(ownedProperties):

            if _property[dbLib.OWNER_PROPERTY_VERIFIED] == True:
                print "%s - %s : Verified!" % (index + 1, _property[dbLib.OWNER_PROPERTY])

    except:
        pass

    try:

        for index, _property in enumerate(ownedProperties):

            if _property[dbLib.OWNER_PROPERTY_VERIFIED] == False:
                print "%s - %s : Rejected!" % (index + 1, _property[dbLib.OWNER_PROPERTY])

    except:
        pass

    print


dbMan = dbLib.DatabaseMan()

aadhaarNo = aadhaarInput()
# userId = sha256(aadhaarNo).hexdigest()
userId = aadhaarNo

print "Fingerprint Verification!(dummy text)"
sleep(3)  # just for real feel, nothing real in this, but will be for sure...
print "Fingerprint Verified!"
sleep(1)

while True:

    print dedent("""
                 Your aadhaar number: %s

                 1. Digitalize Your Current Property Ownership:
                 2. Show Properties Owned\n""" % (
                 userId))

    choice = raw_input("Enter Your Choice: ")
    print

    if choice == "1":

        print "Enter Your Owned Property Details: "
        plotNo = raw_input("Enter Plot No: ")
        areaNo = raw_input("Enter Area No: ")

        propertyToken = "&".join(["plotNo=" + plotNo, "areaNo=" + areaNo])

        dbMan.newApplication(userId, propertyToken)

        print
        print "Your details have been sent to the government!"
        print "Govt. verification is pending..."
        print "Official agents will come to your property for verification"
        print "Keep your property documents ready!"
        print
        print "Once verified, your aadhaar card will link to your property"
        print "And this digital ownership of your property will be published"
        print "to the blockchain so that anybody can see who's the owner of"
        print "which property and nobody but the owner can change it."
        print
        break

    elif choice == "2":
        showProperties(dbMan)
        break

    else:
        print "Invalid Choice! Enter Again."
        continue
