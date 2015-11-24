db.define_table('supplier',
    Field('Name','string',requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'supplier.Name'))),
    Field('country', length=28, label=T("Country"), default='India',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_state', length=28, label=T("State"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_city', length=28, label=T("city"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_address', length=28, label=T("Door/street NO. "), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_zip', length=6, type='integer',label=T("ZIP code"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_no',type='integer',length=10, label=T("Contact number"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'supplier.s_no'))),
    Field("s_email",label=T("Email"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'supplier.s_email'))) ,   
    Field('s_transaction','integer',label=T("Transaction(Till now)"),default='0',writable=False)
)
#need to set email_validators

db.define_table('product',
    Field('Name',requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'product.Name'))),
    Field('price','integer', length=28, label=T("Price/Qty"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),)),
    Field('qty','integer',default='0')
)

db.define_table('product_supplier',
    Field('s_name',requires=(IS_IN_DB(db, 'supplier.Name'))),
    Field('p_name',requires=(IS_IN_DB(db, 'product.Name')))    
)
#max zip code terni

db.define_table('customer',
    Field('c_name',label=T("Customer Name"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'customer.c_name'))),
    Field('country', length=28, label=T("Country"), default='India',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_state', length=28, label=T("State"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_city', length=28, label=T("city"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_address', length=28, label=T("Door/street NO. "), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_zip', length=6, type='integer',label=T("ZIP code"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty))),
    Field('s_no',type='integer',length=10, label=T("Contact number"), default='',
        requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'customer.s_no'),)),
    Field("s_email",label=T("Email"),requires=(IS_NOT_EMPTY(error_message=auth.messages.is_empty),IS_NOT_IN_DB(db, 'customer.s_email'))) ,   
    Field('credit','integer',label=T("Credits"),default='0',writable=False)
)




