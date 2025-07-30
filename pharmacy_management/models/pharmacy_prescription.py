from odoo import models, fields, api

class PharmacyPrescription(models.Model):
    _name = 'pharmacy.prescription'
    _description = 'Pharmacy Prescription'

    name = fields.Char(default="New", readonly=True)
    patient_id = fields.Many2one('res.users', string="Patient", required=True)
    date_prescribed = fields.Date(default=fields.Date.today)
    medicine_ids = fields.One2many('pharmacy.prescription.line', 'prescription_id', string="Medicines")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('dispensed', 'Dispensed')
    ], default='draft', string="Status")

    total_cost = fields.Float(string="Total Cost", compute="_compute_total_cost", store=True)

    @api.depends('medicine_ids.subtotal')
    def _compute_total_cost(self):
        for rec in self:
            rec.total_cost = sum(line.subtotal for line in rec.medicine_ids)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_dispense(self):
        for rec in self:
            rec.state = 'dispensed'
