from openerp.osv import fields, orm


class workflowtest(orm.Model):
    _name = "workflowtest"


    _columns = {
        'name': fields.char("Name", required=True),
        'quantity': fields.Integer("Quantity"),
        'state': fields.selection([
            ('new','New'),
            ('mangConfirm','Manager Confirm'),
            ('assigned','Assigned'),
            ('comitAccept','Accepted')
            ], 'Stage', readonly=True),
            }


    def mymod_new(self, cr, uid, ids):
     self.write(cr, uid, ids, {'state': 'new'})
     return True

    
    def mymod_mangConfirm(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'mangConfirm'})
         return True


     def mymod_assigned(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'assigned'})
         return True
    

    def mymod_comitAccept(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'comitAccept'})
         return True

    #def mymod_lost(self, cr, uid, ids):
     #    self.write(cr, uid, ids, {'state': 'lost'})
      #   return True

