from openerp.osv import orm, fields


class iti_warehouse(orm.Model):
    _name = "iti.warehouse"

   


class iti_product(orm.Model):
    _name = "iti.product"

    _columns = {
        'name': fields.char("Name"),
        'min':fields.integer("Min Quantity"),
        'max':fields.integer("Max Quantity"),
        'price':fields.integer("Price"),

        'state':fields.selection(string="State",selection=[
            ('new','New'),
            ('received','Received'),
            ('waiting','Waiting For Review'),
            ('accepted','Accepted'),
            ('keeperreg','Keeper Registration'),
            ('managerconfirm','Manager Confirmation'),
        ], readonly=True),
        'warehouse_id': fields.many2one("iti.warehouse", "Warehouse"),
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







