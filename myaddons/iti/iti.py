from openerp.osv import orm, fields


class iti_students(orm.Model):
    grade = [('g', 'Good'), ('v', 'Very good'), ('e', 'Excellent')]
    graduation_year = [('2012', '2012'), ('2013', '2013'), ('2014', '2014')]
    _name = 'iti.student'
    _columns = {
        'name': fields.char('Name'),
        'age': fields.char('Age'),
        'salary': fields.integer('Salary'),
        'faculty': fields.text('Faculty'),
        'grade': fields.selection(grade, 'Grade'),
        'graduation_year': fields.selection(graduation_year, 'Graduation_year'),
        'info': fields.html('Information'),
        'accepted': fields.boolean('Accepted'),
        'img': fields.binary('Your image'),
        'department_id':fields.many2one('iti.departments',string='DepartmentID'),
        'skills':fields.many2many('student.skills',string='Student skills') #skills_ids
    }
    # def _change_department(self,cr,uid,ids,subject):
    #     dept=self.pool.get('iti.departments').browse(cr,uid,subject)
        # if dept.skills_ids.subject==subject and dept.name=='OS':
        #     pass
        # result={
        #     'value':{}
        # }





class iti_departments(orm.Model):
    _name = 'iti.departments'
    _columns ={
        'name':fields.char('Department Name'),
        'description':fields.text('Department Description'),
        'students_ids':fields.one2many('iti.students','department_id',string='Students in department'),
        'skills_ids':fields.one2many('student.skills','department_id',string='Department skills')

    }
class student_skills(orm.Model):
     _name = 'student.skills'
     _columns = {
       'subject':fields.char('Skills'),
       'description':fields.text('Description'),
       'department_id':fields.many2one('iti.departments',string='Department ID')

     }
     _rec_name = 'subject'



class hr_extend(orm.Model):
    _inherit= 'hr.employee'
    _columns = {
        'emp_code':fields.char('Employee Code')
    }
