from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class EmployeeFeedback(models.Model):
    _name = 'employee.feedback'
    _description = 'Employee Feedback'

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, default=lambda self: self.env.user.employee_id)
    feedback = fields.Text(string="Feedback", required=True)
    date_submitted = fields.Date(string="Date Submitted", default=fields.Date.today)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('action_taken', 'Action Taken')
    ], string="Status", default='pending')
    category = fields.Selection(
        [('work_environment', 'Work Environment'),
         ('management', 'Management'),
         ('team_dynamics', 'Team Dynamics')],
        string='Category',
        required=True
    )

    @api.constrains('feedback')
    def _check_feedback_not_empty(self):
        if not self.feedback.strip():
            raise ValidationError("Feedback message cannot be empty.")

    def write(self, vals):
        if 'status' in self and self.status != 'pending':
            raise UserError("You can only edit feedback if the status is 'Pending'.")
        return super(EmployeeFeedback, self).write(vals)

    def unlink(self):
        raise UserError("You cannot delete feedback.")

    class Employee(models.Model):
        _inherit = 'hr.employee'

        feedback_ids = fields.One2many(
            'employee.feedback',
            'employee_id',
            string='Feedback'
        )
