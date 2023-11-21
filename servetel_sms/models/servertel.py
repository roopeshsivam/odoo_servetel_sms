from odoo.exceptions import UserError     # type: ignore
from odoo import api, fields, models, tools, _    # type: ignore
import datetime as dt
import logging
import requests
_logger = logging.getLogger(__name__)

class ServerTel(models.Model):
    _name = 'servertel.account'
    _description = 'Servertel SMS'

    
    name = fields.Char('Name', required=True)
    servetel_username = fields.Char('Username', required=True)
    servetel_password = fields.Char('Password', required=True)
    message = fields.Text('Default Message')

    def auth_sms(self):
        url = "https://api.servetel.in/v1/auth/login"
        payload = {
            "email": self.servetel_username,
            "password": self.servetel_password
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.text

    def send_message(self, phone, message):
        # Code for error message if message length greater than 160 characters.
        url = "https://api.servetel.in/v1/send_sms"
        payload = {
            "customer_number": phone,
            "message": message
        }

        headers = {
            "accept": "application/json",
            "Authorization": self.auth_sms(),
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)

  
        raise UserError(response.text)



class Company(models.Model):
    _inherit = 'res.company'

    servertel_id = fields.Many2one('servertel.account', string='Servertel Account')
    servetel_username = fields.Char('Username')
    servetel_password = fields.Char('Password')

    
