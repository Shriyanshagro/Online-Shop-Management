from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

#need to find max input for rank
 
auth.settings.extra_fields['auth_user']= [
    Field('mobile', type='integer',length=10, label=T("Mobile Number"), requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db,'auth_user.mobile'))),
    Field('country', length=28, label=T("Country"), default='India',requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_state', length=28, label=T("State"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_city', length=28, label=T("city"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_address', length=28, label=T("Door/street NO. "),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('zip', length=6, type='integer',label=T("ZIP code"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('e_rank',type='integer',length=1, label=T("Present rank in Company"), default='4',writable=False,requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('salary',type='integer', label=T("Salary(will be updated)"), default='0',writable=False),
    Field('e_absent',type='integer',label=T("Leave"),default='0',writable=False),
    Field('credit',type='integer',default='0',writable=False),
    Field('image','upload',label=T("Profile Pic"))
    ]
            
## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server =''
mail.settings.sender = ''
mail.settings.login = ''

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = False

## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.

