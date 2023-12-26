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
                'priority': ticket.priority,
                'message': ticket.message,
                'nepalidatepicker': ticket.nepalidatepicker,
                'photo':photo,
            })
        return http.request.render(
            "support_sys.portal_my_invoices",
            {"records": data}
        )

    @http.route('/ticket_raise', type='http', auth='public', website=True)
    def authenticate_user(self, **post):
        ticket_type = post.get('ticket_type')
        employee = post.get('employee')
        priority = post.get('priority')
        message = post.get('message')
        client_email= post.get('client_email')
        nepalidatepicker = post.get('nepalidatepicker')
        photo = post.get('photo')

        if photo:
            # If a photo is uploaded, convert it to base64
            photo_base64 = base64.b64encode(photo.read())
        else:
            photo_base64 = None

        ticket = request.env['ticket.raise'].sudo().create({
            'ticket_type': ticket_type,
            'employee': employee,
            'priority':priority,
            'message': message,
            'photo':photo_base64,
            'nepalidatepicker': nepalidatepicker,
            'client_email': client_email,  # Assign the client's email to the model's email field
        })

        # Send an email to the client
        if ticket:
            template = request.env.ref('support_sys.email_template_ticket_raise')
            if template:
                template.with_context(object=ticket).send_mail(ticket.id, force_send=True)

        # Redirect to the ticket view
        return request.redirect('/ticket_view')