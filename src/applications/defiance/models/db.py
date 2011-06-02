# -*- coding: utf-8 -*- 

#########################################################################
## This scaffolding model makes the app work on app engine. 
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    from gluon.contrib.gae_memcache import MemcacheClient
    from gluon.contrib.memdb import MEMDB
    cache.memcache = MemcacheClient(request)
    cache.ram = cache.disk = cache.memcache
    session.connect(request, response, MEMDB(cache.memcache)) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db=MEMDB(Client())
else:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB


from gluon.tools import *
crud=Crud(globals(),db)                      # for CRUD helpers using auth

#########################################################################
## Define your tables below, for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
db.define_table('services', db.Field('name', required=True),
                            db.Field('description', 'text', required=True))
# Initialize services table.
if not db(db.services.id > 0).count():
    db.services.insert(name='Web design and development',
        description='We specialize in Python(web2py, django et al.) based green-field web development. We also do Rails and PHP development. We have expertise in developing rich client side applications. We understand the current web trends and technologies and are well versed to cater to both high scalability, high traffic clients as well as medium sized clients.')
    db.services.insert(name='Application development',
        description='We bring with us a diverse set of skill set ranging from C/C++ to Clojure/Lisp. We undertake all sort of custom application development. We cater to system programming, enterprise applications, embedded systems and anything & everything under the sun. We have development experience in all sorts of programming paradigms(procedural, object-oriented, functional) and languages(C, C++, Java, Clojure, Python).')
    db.services.insert(name='Infrastructure management',
        description='We have ample amount of experience managing and creating various software infrastructures - Mail servers, dns servers, LDAP, routers etc. Our favoured platform for running all kind of services is Linux, though we do use BSDs and Solaris on occasions. We understand the need for 24x7 availability of the systems and tailor it accordingly. We set up the systems and supporting set of code and provide training to the in-house engineers for it.')
    db.services.insert(name='Cloud solutions',
        description='If you are thinking of migrating to the cloud(Amazon EC2, Google App engine or a custom solution), we are the people for you. We have worked on the mentioned systems and we help our clients painlessly move their existing solutions to it. We also undertake development of custom cloud platforms. We have expertise in Hadoop/HDFS, Disco, Xen and other related technologies.')
    db.services.insert(name='Social Media Consulting',
            description='Social media is the new wave. If you feel lost in this world of twitter, linked-in, techcrunch etc., we can help you figure it out. Social media is a powerful medium for promotion. It helps you directly communicate with your audience. We help you make an online brand for yourself and reach-out to a larger audience. We also provide technical writing for your products and services and promote it on various technical blogs.')
    db.services.insert(name='VoIP solutions',
        description='We do development and tailoring for the voIP needs of various clients. Asterisk is our favored platform. We have seen an Asterisk based solution is less expensive and gives the same quality of service.')


db.define_table('content', db.Field('ident', required=True),
                           db.Field('name', default=""),
                           db.Field('seq', 'integer', default=10),
                           db.Field('description', 'text', required=True))
# Initialize content table.
if not db(db.content.id > 0).count():
    db.content.insert(ident='home-main',
        name='Software as it should be',
        seq=10,
        description='We develop elegant web-based and desktop applications. We bring out the beauty in the software. We do not understand beauty in conventional terms; after all, we are defying the conventional. Beauty for us is an aggregate of speed, correctness, aesthetics, efficiency and timeliness.')
    db.content.insert(ident='home-main',
        name='Customer focus',
        seq=20,
        description='We take great pleasure in what we do and always keep customer satisfaction above everything else. Our business is not driven by legal contracts. We follow an agile, transparent model and the customer can choose to be involved with all phases of development.')
    db.content.insert(ident='home-main',
        name='Quality, transparency and flexibility',
        seq=30,
        description='We accept changing the requirements on the run. Being in the software field, we realize that the only constant is change. We do not promise low-cost development; that is not what we do. We believe quality comes at a price. We promise you quality, transparency and flexibility.')
    db.content.insert(ident='home-main',
        name='Take a look',
        seq=40,
        description='Head over to our <a class="ajax" href="/defiance/default/services">services</a> for a glimpse of what we do. If you can not find what you are looking for, there is a fair chance we do it and did not mention it for the sake of brevity. Get in <a class="ajax" href="/defiance/default/contact">touch</a> with us and we will get back to you at the earliest.' )
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=10,
        description='You do not work for us; you work with us.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=15,
        description='1/4th of your typical day(about 6 hours) is work. Enjoy it. If you don\'t, you are in the wrong profession.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=20,
        description=' Work should be fun. If it isn\'t, talk to us. We are more than eager to listen.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=25,
        description='Work should be challenging. We do not insult your intellect with mundane jobs. You are worth more than that.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=30,
        description='You need not carry your work to your homes. We employ you; we don\'t own you.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=35,
        description='You are free to work from home if you so wish. No issues as long as work gets done.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=40,
        description='We believe in team work and so should you.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=45,
        description='But we don\'t undermine individual contribution. You get necessary credit and independence.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=50,
        description='You are free to make mistakes.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=55,
        description='But you are required to take accountability for it by logging & fixing it. ')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=60,
        description='Like you, we hate processes and buzz words. We do not do something just for the sake of it.')
    db.content.insert(ident='careers-zen',
        name='zen',
        seq=65,
        description='And like you, we religiously follow what is beneficial - coding standards, code reviews, continuous integration etc.')


