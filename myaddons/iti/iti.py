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

