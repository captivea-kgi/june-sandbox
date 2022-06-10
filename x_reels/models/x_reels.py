# Copyright (C) 2022 Commonwealth Fusion System. https://cfs.energy
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


# EHI-8: HTS XReels model creation
class HTSReel(models.Model):
    _name = "x.reels"
    _description = "CFS HTS Reel"

    x_reels_case = fields.Many2one(
        "stock.location", string="Case", help="The Case this reel is in"
    )
    x_reels_manufacturer = fields.Many2one(
        "res.partner",
        string="Manufacturer",
        help="The Original Manufacturer of this reel",
        domain=[("company_type", "=", "company")],
    )
    x_reels_shipmentdate = fields.Date(string="Shipment Date")
    x_reels_manufacturingcode = fields.Char(string="Manufacturing Code")
    x_reels_originalinside = fields.Float(string="Original Bare Inside")
    x_reels_originaloutside = fields.Float(string="Original Bare Outside")
    x_reels_averageic = fields.Float(string="Average IC")
    x_reels_platersm = fields.Float(string="Platers Length (m)")
    x_reels_mfgm = fields.Float(string="MFG Length (m)")
    x_reels_qastatus = fields.Selection(
        string="QA Status",
        selection=[
            ("production_ready", "Production Ready"),
            ("passed_accepted_bare", "Passed Accepted Bare"),
            ("passed_accepted_out_plating", "Passed Accepted Out For Plating"),
            ("insufficient_data_bare", "Insufficient Data Bare"),
        ],
    )
    x_reels_length = fields.Float(string="Length")
    x_reels_passedqa = fields.Selection(
        string="Passed QA", selection=[("yes", "Yes"), ("no", "No")]
    )
    x_reels_bareinsiderevision = fields.Float(string="Bare Inside (if revision)")
    x_reels_bareoutsiderevision = fields.Float(string="Bare Outside (if revision)")
    x_reels_mitnumber = fields.Char(string="MIT Number")
    x_reels_serialnumber = fields.Many2one(
        "stock.production.lot", string="Serial Number"
    )
    x_reels_originalposition = fields.Integer(string="Original End Position")
    x_reels_substrate = fields.Integer(string="Substrate")
    x_reels_originalthickness = fields.Float(string="Original Thickness")
    x_reels_highlow = fields.Selection(
        string="High or Low", selection=[("high", "High"), ("low", "Low")]
    )
    x_reels_bareplated = fields.Selection(
        string="Bare or Plated", selection=[("bare", "Bare"), ("plated", "Plated")]
    )
    x_reels_samplingdate = fields.Date(string="Sampling Date")
    x_reels_thickness = fields.Float(string="Thickness")
    x_reels_location = fields.Many2one("stock.location", string="Location")
    x_reels_lengthstatus = fields.Selection(
        string="Length Status", selection=[("pristine", "Pristine")]
    )
    x_reels_platedm = fields.Float(string="Plated Outside (m)")
    x_reels_platersft = fields.Float(string="Plater's Length (m)")
    x_reels_platersmcomputed = fields.Float(
        string="Plater's Length (m)", compute="_compute_x_reels_platersmcomputed"
    )
    x_reels_differencelength = fields.Float(
        string="% Difference in Length", compute="_compute_x_reels_differencelength"
    )
    x_reels_verifiedserial = fields.Boolean(string="Verified Length & Serial #")
    x_reels_htspass = fields.Boolean(string="HTS Inspection Pass")
    x_reels_includeshipment = fields.Boolean(string="Include In Next Shipment")
    x_reels_cfslength = fields.Float(string="CFS Verified Lengths")

    def _compute_x_reels_platersmcomputed(self):
        for platerscomputed in self:
            platerscomputed.x_reels_platersmcomputed = self.x_reels_platersft * 3.28084

    def _compute_x_reels_differencelength(self):
        for differencelength in self:
            differencelength.x_reels_differencelength = (
                self.x_reels_mfgm / self.x_reels_platersm
            )
