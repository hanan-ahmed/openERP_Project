#! /usr/bin/env python
#encoding:UTF-8


from openerp.osv import orm, fields



class iti_warehouse(orm.Model):
    _name = "iti.warehouse"

    _columns = {
        'name':fields.char('الاسم'),
        'address': fields.char("العنوان"),
		'date': fields.date('تاريخ الانشاء'),
       'keeper_id': fields.many2one('res.users', "امين المخزن"),
        'manager_id': fields.many2one('res.users', "مديرالمخزن"),
        'super_manager_id': fields.many2one('res.users', "رئيس المخازن"),
        'commitee_member1': fields.many2one('res.users', "عضو اللجنه الاول"),
        'commitee_member2': fields.many2one('res.users', "عضو اللجنه الثاني"),
        'commitee_member3': fields.many2one('res.users', "عضو اللجنه الثالث"),
    }



class iti_category(orm.Model):
    _name = 'iti.category'
    _columns = {
        'name': fields.char('اﻻسم'),
        'cat_id': fields.integer('cat_id', required=True),
        'desc': fields.text('الوصف'),
    }


class iti_subcategory(orm.Model):
    _name = 'iti.subcategory'
    _columns = {
        'name': fields.char('اﻻسم'),
        'subcat_id': fields.integer('subcat_id', required=True),
        'desc': fields.text('الوصف'),
        'category_id': fields.many2one('iti.category', string='الباب'),
    }


class iti_subsubcategory(orm.Model):
    _name = 'iti.subsubcategory'
    _columns = {
        'name': fields.char('اﻻسم'),
        'subsubcat_id': fields.integer('subsubcat_id', required=True),
        'desc': fields.text('الوصف'),
        'subcategory_id': fields.many2one('iti.subcategory', string='المجموعه'),
    }



class iti_supplier(orm.Model):
    _name = 'iti.supplier'
    _columns = {
        'name': fields.char('الاسم'),
        'desc': fields.char('الوصف'),
        'address': fields.char('العنوان'),
        'telnum': fields.char('رقم التليفون'),
        }



class iti_product(orm.Model):
    _name = 'iti.product'

    def check_keeper(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            keeper_id = product.warehouse_id.keeper_id.id
        res[product.id] = (keeper_id == uid)
        return res

    def check_manager(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            manager_id = product.warehouse_id.manager_id.id
        res[product.id] = (manager_id == uid)
        return res


    def check_supermanager(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            super_manager_id = product.warehouse_id.super_manager_id.id
        res[product.id] = (super_manager_id == uid)
        return res


    def check_commitee_member1(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            commitee_member1_id = product.warehouse_id.commitee_member1_id.id
        res[product.id] = (commitee_member1_id == uid)
        return res

    def check_commitee_member2(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            commitee_member2_id = product.warehouse_id.commitee_member2_id.id
        res[product.id] = (commitee_member2_id == uid)
        return res

    def check_commitee_member3(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            commitee_member3_id = product.warehouse_id.commitee_member3_id.id
        res[product.id] = (commitee_member3_id == uid)
        return res
    



    def _calc_code(self, cr, uid, ids, name, arg, context=None):
        result = {}
        ids = self.search(cr, uid, [])

        products = self.browse(cr, uid, ids, context)
        for product in products:
            if (product.category_id and product.subcategory_id and product.subsubcategory_id):
                result[product.id] =  str(product.category_id.cat_id) + str(
                    product.subcategory_id.subcat_id) + str(product.subsubcategory_id.subsubcat_id)+str(product.code)

        return result



    _columns = {
        'name': fields.char('اﻻسم'),
        'price': fields.float('السعر'),
        'productdate': fields.date('تاريخ الدخول'),
        'expirdate': fields.date('تاريخ الخروج'),
        'minqty': fields.integer('اقل كمية مسموحة'),
        'maxqty': fields.integer('اكثر كمية مسموحة'),
        'qtyin': fields.integer('الكمية الداخلة'),
        'qtyout': fields.integer('الكمية الخارجة'),
        'code': fields.integer('الكود', size=2, required=True),
        'net_code': fields.function(_calc_code, string='المرجع', store=True, method=True, type='char'),
        'desc': fields.text('الوصف'),
        'category_id': fields.many2one('iti.category', string='الباب'),
        'subcategory_id': fields.many2one('iti.subcategory', string='المجموعه'),
        'subsubcategory_id': fields.many2one('iti.subsubcategory', string='القسم'),
        'supplier_id': fields.many2many('iti.supplier', string='المورد'),
        'warehouse_id': fields.many2one('iti.warehouse',string='المخزن'),
        'is_keeper': fields.function(check_keeper, type='boolean', store=False),
        'is_manager': fields.function(check_manager, type='boolean', store=False),
        'is_supermanager': fields.function(check_supermanager, type='boolean', store=False),
        'is_commitee_member1': fields.function(check_commitee_member1, type='boolean', store=False),
        'is_commitee_member2': fields.function(check_commitee_member2, type='boolean', store=False),
        'is_commitee_member3': fields.function(check_commitee_member3, type='boolean', store=False),
		'state':fields.selection(string="State",selection=[
				    ('new','جديد'),
				    ('received','استلام'),
				    ('waiting','انتظار الفحص'),
				    ('accepted','مقبول'),
				    ('keeperreg',"تسجيل امين المخزن للمنتجات "),
				    ('managerconfirm','موافقه رئيس المخازن'),
				], readonly=True),

    }


    def product_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})
        return True


    def product_received(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'received'})
        return True


    def product_WaitingForReview(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'waiting'})
        return True


    def product_approved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'accepted'})
        return True


    def product_keeper_register(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'keeperreg'})
        return True


    def product_manager_confirm(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'managerconfirm'})
         return True



class iti_employees(orm.Model):
     gender = [('f', 'female'), ('m', 'male')]
     _name = 'iti.employees'
     _columns = {
         'name': fields.char('الاسم'),
         'age': fields.integer('العمر'),
        'salary': fields.integer('المرتب'),
         'gender': fields.selection(gender, 'النوع'),
         'check': fields.boolean('الفحص'),
         'pic': fields.binary('الصورة',widget='Image'),
         'warehouse_id': fields.many2one('iti.warehouse', 'المخزن'),
         'user_system':fields.many2one("res.users","User System"),

     }


class hr_extend(orm.Model):
    _name = 'hr.employee'
    _inherit= 'hr.employee'
    _columns = {
        'emp_code':fields.char('Employee Code'),
        'committe':fields.boolean('Member in committe'),
        'warehouse_id': fields.many2one('iti.warehouse', 'المخزن'),
        'user_system':fields.many2one("res.users","User System"),

    }
    def set_committe(self,cr,uid,ids,context=None):
        pass



class iti_search(orm.Model):
    _name = 'iti.search'
    ch = [('name','اﻻسم'), ('code','الكود')]
    _columns = {
        'search': fields.char(string='اسم المنتج/كود المنتج',size=100),
        'change': fields.selection(ch,string='بحث بواسطة',size=100),
        'result': fields.text(string='النتيجة',size=500)
    }
    def func(self, cr, uid, ids, search , change , context=None):
        record = self.pool.get('iti.product').search(cr, uid, [(change,'=',search)], context=context)
        record=self.pool.get('iti.product').read(cr, uid,record , context=context)
        if record:
            v = {'result': 'اﻻسم:'+str(record[0]['name'])+',الحالة:'+str(record[0]['state'])
            +',Code:'+str(record[0]['code'])
            +',اكبر كمية مسموحة:'+str(record[0]['maxqty'])+',اقل كمية مسموحة:'+str(record[0]['minqty'])+
                           ',السعر:'+str(record[0]['price'])
            +',الوصف:'+str(record[0]['desc'])}
        else:
            v = {'result': ''}
        return {'value':v}
