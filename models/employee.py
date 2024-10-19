from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    feedback_ids = fields.One2many(
        'employee.feedback',
        'employee_id',
        string='Feedback'
    )