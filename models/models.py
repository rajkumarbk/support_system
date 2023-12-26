
from odoo import models, fields, api
from datetime import datetime


class support_sys(models.Model):
    _name = 'support_sys.support_sys'
    _description = 'support_sys.support_sys'



    c_id = fields.Integer(string='ID')
    name = fields.Char(string='Client Name')
    image = fields.Binary("Client Image")
    # message = fields.Text(string='Message', required=True)
    issue_description = fields.Char(string='Issued Description')
    support_type = fields.Selection([
        ('ordinary', 'Ordinary'),
        ('vip', 'VIP')
    ], string='Support Type', default='ordinary', help='Select the support type')
    assigned_employee = fields.Char(string='Name of Employee')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ], string='Status', default='new')
    month_field = fields.Date(
        string='Date',
        widget='Date',
        help='Select a month',
        default=datetime.now().date()
    )
class Ticket(models.Model):
    _name = 'ticket.raise'
    _description = 'ticket'

    # name = fields.Char(string='Name')
    ticket_id = fields.Char(string='Ticket Number')
    ticket_type = fields.Selection([('complain', 'Complain'), ('feedback', 'Feedback'), ('request', 'Request'), ('query', 'Query')],
                                   string='Choose a Ticket')
    employee = fields.Selection([('DeerWalk', 'DeerWalk'), ('Techrida', 'Techrida'), ('TalentConnect', 'TalentConnect'), ('TukiLogic', 'TukiLogic'), ('EkSolution', 'EkSolution')],
                                string='Choose an Employer')
    message = fields.Text(string='Message', required=True)
    priority=fields.Selection([('urgent', 'Urgent'), ('high', 'High'), ('medium', 'Meduium'), ('low', 'Low')],
                                   string='Choose a Priority')
    photo = fields.Binary(string='photo')
    req_date = fields.Date(string='Requested date', required=True)
    # photo_filename = fields.Char(string='photo Filename')
    @api.model
    def create(self,vals):
        print("Sequence",vals)
        vals['ticket_id'] = self.env['ir.sequence'].next_by_code("ticket.raise")
        return super(Ticket,self).create(vals)


class Employee(models.Model):
    _name='employee.details'
    _description='employee'

    
    employee_name=fields.Char()
    contact= fields.Char()
    address = fields.Char()
    department=fields.Char()
    position = fields.Char()
    salary=fields.Integer()
    date_joined=fields.Date()


   
    
    class Expense(models.Model):
        _name='employee.expense'
        _description='employee'

        expense_date = fields.Date(string='Expense Date', default=fields.Date.today())
        amount = fields.Float(string='Amount')
        description = fields.Text(string='Description')
        status = fields.Selection([
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ], string='Status', default='draft')
        expense_category = fields.Selection([
            ('meals', 'Meals'),
            ('travel', 'Travel'),
            ('accommodation', 'Accommodation'),
            ('other', 'Other'),
        ], string='Expense Category')

        starting_location = fields.Char(string='Starting Location')
        ending_location = fields.Char(string='Ending Location')
        bill_image = fields.Binary("Bill Image")

    

    def submit_ticket(self):
        # Add logic to handle ticket submission
        # You can process the form data and perform any necessary actions here
        return {'type': 'ir.actions.act_window_close'}
    

    