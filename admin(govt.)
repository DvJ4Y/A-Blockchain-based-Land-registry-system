from time import sleep
from textwrap import dedent
import database as dbLib

dbMan = dbLib.DatabaseMan()


def selectApplication():

    pendingApplications = dbMan.getAllPendingApplications()

    totalPendingApplications = len(pendingApplications)

    if totalPendingApplications > 0:

        try:
            for index, _property in enumerate(pendingApplications):

                print "%s: %s - %s" % (index + 1,
                                       _property[dbLib.APPLICATION_USER_ID],
                                       _property[dbLib.APPLICATION_PROPERTY])

        except:
            pass

        print "%s: Exit" % (totalPendingApplications + 1)

        applicationNo = raw_input("Enter Application Number: ")

        try:
            applicationNo = int(applicationNo)

            if applicationNo == totalPendingApplications + 1:
                exit(0)

            application = pendingApplications[applicationNo - 1]

            return application

        except ValueError:

            print "Invalid Choice! Enter Again"
            return selectApplication()

    else:
        return None


print "Fingerprint Verfication: Person 1/3(Dummy text)!"
sleep(2)
print "Fingerprint Verified!(1/3)"
sleep(1)
print "Fingerprint Verfication: Person 2/3(Dummy text)!"
sleep(2)
print "Fingerprint Verified!(2/3)"
sleep(1)
print "Fingerprint Verfication: Person 3/3(Dummy text)!"
sleep(2)
print "Fingerprint Verified!(3/3)"
sleep(1)

print
print "Welcome to the..."
print "Property Verfication Panel For Government!"
print

while True:

    print "1. Pending Applications"
    print "2. Exit"

    choice = raw_input("Enter Your Choice: ")
    print

    if choice == "1":

        application = selectApplication()

        if application is not None:

            is_verified = raw_input("Is this property ownership correct?(Yes/No/Leave): ")

            userId = application[dbLib.APPLICATION_USER_ID]
            _property = application[dbLib.APPLICATION_PROPERTY]

            if is_verified in ['y', 'Y', 'yes', 'Yes', 'YES']:
                dbMan.verifyApplication(userId, _property)
                print "Property Ownership Marked as Verified"

            elif is_verified in ['n', 'N', 'no', 'No', 'YES']:
                dbMan.rejectApplication(userId, _property)
                print "Property Ownership Marked as Rejected"

            elif is_verified in ['l', 'L', 'leave', 'Leave', 'LEAVE']:
                print "Verification Status Unchanged!"
                print
                continue

            break

        else:
            print "No property ownership digitalization application found!"
            print

    elif choice == "2":
        exit(0)
