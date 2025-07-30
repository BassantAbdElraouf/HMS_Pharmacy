from odoo import models, fields, api

class PharmacyPrescriptionLine(models.Model):
    _name = 'pharmacy.prescription.line'
    _description = 'Prescription Line'

    prescription_id = fields.Many2one('pharmacy.prescription', string="Prescription")
    product_id = fields.Many2one('product.product', string="Medicine", domain="[('type','=','medicine')]", required=True)
    quantity = fields.Float(string="Quantity", required=True)
    cost = fields.Float(string="Unit Cost", related='product_id.standard_price', readonly=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('cost', 'quantity')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.cost * rec.quantity