# A-Blockchain-based-Land-registry-system
INTRODUCTION
============

This is a mini version of what is described in our original project document.
In this small mini-project, we have implemented a central-database model
instead of using the decentralized, blockchain model. It provide
two different interfaces for "User" and "Govt."

The User-Interface:-

    First of all, aadhar card number is asked from the the user, and his/her
    fingerprint is verified using Aadhar APIs.

    Once identity verified, he/she can...

    1) apply to digitalize his/her currently owned property
    2) see which property he/she currently owns, properties he/she has applied
       to(with pending verification status), and property applications he/she
       previously applied and got their application rejected by the government
       interface.
    --------------------------------------------------------------------------

    In digitalization application, he is asked for property details(let's
    assume the property details only consists of plot number and area code in
    all over Rajasthan)

    Once he/she fills that form, it is send to government interface from
    where govt. will be able to accept/reject his/her claim on the property.
    As soon as the govt. takes any action(accept/reject), this new ownership
    is published to the blockchain database(not in our current mini-program,
    but in ideal project).

    And once that data is published to the blockchain, nobody but the property
    owner could change(transfer) it right to somebody else.


The Govt-Interface:-

    Govt. will be represented by 3 employees whose fingerprints will verify
    that it's the government.

    After govt. verification, screen will display different different
    user applications for digitalization of their property
    rights

    By choosing each application, govt. will be asked if the ownership details
    that are being claimed in the application is correct or not? Govt. verifies
    that information by sending a agent to the site and collecting paper/legal
    documents from the user.

    Once, agent collect whether the ownership is correct or not, he/she feeds
    that information to govt, and govt. updates the status of application.

    After updating the application status to either "verified", "rejected",
    the information is published on the blockchain(not in current program, but
    in our ideal project model, currently using local database only)

-------------------------------------------------------------------------------

HOW TO RUN
==========

On Ubuntu:

    Step1: Install python2.7, pip2.7(apt-get install python2.7 pip2.7)
    Step2: Install mysql-server(apt-get install mysql-server)

    Step3: Install MySQLdb python module(pip install MySQLdb)
    Step4: Configure mysql(mysql_secure_installation)

    Step5: Create database named `land_registry`

    Now, for user end, we need to run the `user.py` file,

    Step 1: Run the `user.py` file(python user.py)
    Step 2: Follow what you see in the interface(also read above user-interface
           section).

    Also, on the govt. end,

    Step 1: Run the `govt.py` file(python govt.py)
    Step 2: Follow what you see as per the instructions given above in
            govt-interface section.

-------------------------------------------------------------------------------

DIFFERENCE BETWEEN OUR CURRENT PROJECT AND ORIGINAL IDEA
========================================================

Current Project(Mini-Model)                       Ideal Project(Original Model)

1. Uses Centralized MySQL server                  1. Uses Blockchain Database
