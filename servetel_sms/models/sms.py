from odoo.exceptions import UserError     # type: ignore
from odoo import api, fields, models, tools, _    # type: ignore
import datetime as dt
import logging
import requests
_logger = logging.getLogger(__name__)



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def send_message(self):
        action = self.env.ref('servetel_sms.action_servetel_message').read()[0]
        action['context'] = {
            'default_message' : self.company_id.servertel_id.message,
            'default_phone' : self.partner_id.phone or self.partner_id.mobile,
            'default_servertel_id' : self.company_id.servertel_id.id} 
        return action
        

class MessageWizard(models.TransientModel):
    _name = 'wizard.servetel.message'

    message = fields.Text('Message')
    phone = fields.Char('Phone')
    servertel_id = fields.Many2one('servertel.account', string='servertel')
    def send_message(self):
        self.servertel_id.send_message(self.phone, self.message)
