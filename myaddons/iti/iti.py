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
        'warehouse_id': fields.many2one('iti.warehouse',string='warehouse_id'),
		'state':fields.selection(string="State",selection=[
				    ('new','New'),
				    ('received','Received'),
				    ('waiting','Waiting For Review'),
				    ('accepted','Accepted'),
				    ('keeperreg','Keeper Registration'),
				    ('managerconfirm','Manager Confirmation'),
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
