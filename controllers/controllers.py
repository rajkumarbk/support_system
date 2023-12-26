from odoo import http
from odoo.http import request
import base64

class UserAuthenticationController(http.Controller):

    @http.route('/ticket_raise_form', type="http", auth='public', website=True)
    def user_authentication_form(self, **kw):
        return request.render('support_sys.ticket_raise_form', {})

    @http.route('/ticket_view', type='http', auth='public', website=True)
    def list_tickets(self, **kwargs):
        tickets = request.env["ticket.raise"].sudo().search([])

        data = []
        for ticket in tickets:
            photo = ticket.photo.decode('utf-8') if ticket.photo else None
            data.append({
                'ticket_type': ticket.ticket_type,
                'employee': ticket.employee,
                'message': ticket.message,
                'priority':ticket.priority,
                'req_date': ticket.req_date,
                'photo': photo,
            })
        return http.request.render(
            "support_sys.portal_my_invoices",
            {"records": data}
        )

    @http.route('/ticket_raise', type='http', auth='public', website=True)
    def authenticate_user(self, **post):
        ticket_type = post.get('ticket_type')
        employee = post.get('employee')
        message = post.get('message')
        priority= post.get('priority')
        req_date = post.get('req_date')
        photo = post.get('photo')

        if photo:
            # If a photo is uploaded, convert it to base64
            photo_base64 = base64.b64encode(photo.read())
        else:
            photo_base64 = None

        # Create the ticket record
        ticket_env = request.env['ticket.raise'].sudo()
        ticket_env.create({
            'ticket_type': ticket_type,
            'employee': employee,
            'message': message,
            'photo': photo_base64,
            'req_date': req_date,
            'priority':priority,
        })

        # Redirect to the ticket view
        return request.redirect('/ticket_view')