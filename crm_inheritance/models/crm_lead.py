# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.depends('check_ids')
    def checklist_progress(self):
        total_len = self.env['check.list'].search_count([])
        for rec in self:
            if total_len != 0:
                check_list_len = len(rec.check_ids)
                rec.progress = (check_list_len * 100) / total_len
            else:
                rec.progress = 0

    check_ids = fields.Many2many('check.list', string="List")

    progress = fields.Float(compute=checklist_progress, string="Progress",  default=0.0)





class CheckList(models.Model):
    
    _name = "check.list"
    _description = "Checklist"

    name = fields.Char(string='Name', required=True)

