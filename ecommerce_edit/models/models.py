from odoo import api, fields, models, _
import re

class Websitlocation(models.Model):
    _name = 'pickup.locations'
    _description = 'pickup locations desc'
    name=fields.Char('Pickup Locations')
    code=fields.Char('Location Code')

    date_ids = fields.One2many('pickup.dates', 'location_id','dates',store=True)
    
    #dates_format = fields.Text(string="Layout in Reports",
    #   help="Display format to use for addresses belonging to this country.\n\n"
    #       "You can use python-style string pattern with all the fields of the address "
    #         "(for example, use '%(street)s' to display the field 'street') plus"
    #         "\n%(state_name)s: the name of the state"
    #         "\n%(pickup_name)s: the code of the state"
    #         "\n%(pickup_locations)s: the name of the country"
    #         "\n%(country_code)s: the code of the country",
    #   default='%(street)s\n%(street2)s\n%(city)s %(pickup_name)s %(zip)s\n%(pickup_locations)s')

    #@api.multi
    #def get_dates_fields(self):
    #   self.ensure_one()
    #  return re.findall(r'\((.+?)\)', self.dates_format)


class Websitdates(models.Model):
    _name = 'pickup.dates'
    _description = 'pickup dates desc'
    name=fields.Char('Pickup Name')
    location_id = fields.Many2one('pickup.locations', 'location')



class ecommerce_edit(models.Model):
    _inherit = 'res.partner'
        
    location_id = fields.Many2one('pickup.locations', 'location')   
    date_id = fields.Many2one('pickup.dates', 'date')
    reseller_id = fields.Integer()
    





class ResLocations(models.Model):    
    _inherit = 'pickup.locations'

    def get_website_sale_locations(self, mode='billing'):
        return self.sudo().search([])

    def get_website_sale_dates(self, mode='billing'):
        return self.sudo().date_ids