from odoo import models, fields, api

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
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments")
    rating = fields.Integer(string='Rating', default=0)

    @api.constrains('feedback')
    def _check_feedback_not_empty(self):
        if not self.feedback.strip():
            raise ValueError("Feedback message cannot be empty.")



