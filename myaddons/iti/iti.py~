#! /usr/bin/env python
#encoding:UTF-8


from openerp.osv import orm, fields


class iti_students(orm.Model):
    grade = [('g', 'Good'), ('vg', 'Very Good'), ('Ex', 'Excellent')]
    _name = 'iti.student'
    _columns = {
        'name': fields.char('Name'),
        'age': fields.integer('Age'),
        'salary': fields.float('salary'),
        'faculty': fields.char('faculty'),
        'grade': fields.selection(grade, 'Grade'),
        'graduation_year': fields.selection([('2012', '2012'), ('2013', '2013'), ('2014', '2014')], 'graduation year'),
        'info': fields.html('info'),
        'memo': fields.text('Accepted'),
        'accepted': fields.boolean('Accepted'),
        'image': fields.binary('image'),
        'department_id': fields.many2one('iti.department','Department'),
        'student_idss': fields.many2many('iti.skills', string='Student Skills')

    }


class iti_department(orm.Model):
    department = [('os', 'Open Source'), ('sd', 'System Developer')]
    _name = 'iti.department'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('Description'),
        'department': fields.selection(department, 'Department'),
        'student_ids': fields.one2many('iti.student', 'department_id', 'Department'),
        'skill_id':fields.one2many('iti.skills','department_skill',string='Skills')
    }
class iti_skills(orm.Model):
    _name = 'iti.skills'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('Description'),
        'department_skill':fields.many2one('iti.department',string='Department ID')


    }


class hr_extend(orm.Model):
    _inherit = 'hr.employee'
    _columns = {
        'emp_code': fields.char('Employee Code')

    }
class iti_warehouse(orm.Model):
    _name = "iti.warehouse"

    _columns = {
        'name':fields.char('name'),
        'address': fields.char("Address"),
       'keeper_id': fields.many2one('res.users', "Keeper"),
        'manager_id': fields.many2one('res.users', "Manager"),
        'super_manager_id': fields.many2one('res.users', "Super Manager", domain="[('id','=','ref('ourwarehouse.group_iti_warehouse_supermanager')')]"),

    }


#class iti_category(orm.Model):
 #   _name = "iti.category"

 #   _columns = {
 #       'name': fields.char("name"),
 #       'discription': fields.char("discription"),
 #     	'code':fields.integer("code"),
        # 'sub_category':fields.one2many('iti.subcategory', string="sub_category"),
    }



class workflowtest(orm.Model):
    _name = "workflowtest"


    _columns = {
        'name': fields.char("Name", required=True),
        'qty': fields.integer("Quantity"),
        'state': fields.selection([
            ('new','New'),
            ('assigned','Assigned'),
            ('negotiation','Negotiation'),
            ('won','Won'),
            ('lost','Lost')], 'Status', readonly=True, select=True)
            }


    def mymod_new(self, cr, uid, ids):
     self.write(cr, uid, ids, {'state': 'new'})
     return True

    def mymod_assigned(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'assigned'})
         return True

    def mymod_negotiation(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'negotiation'})
         return True

    def mymod_won(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'won'})
         return True

    def mymod_lost(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'lost'})
         return True








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
                result[product.id] = str(product.code) + str(product.category_id.cat_id) + str(
                    product.subcategory_id.subcat_id) + str(product.subsubcategory_id.subsubcat_id)

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
        'net_code': fields.function(_calc_code, string='المرجع', store=True),
        'desc': fields.text('الوصف'),
        'category_id': fields.many2one('iti.category', string='الباب'),
        'subcategory_id': fields.many2one('iti.subcategory', string='المجموعه'),
        'subsubcategory_id': fields.many2one('iti.subsubcategory', string='القسم'),
        'supplier_id': fields.many2many('iti.supplier', string='الممول'),

    }


