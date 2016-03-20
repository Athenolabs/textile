# -*- coding: utf-8 -*-
# Copyright (c) 2015, pitambar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class FabricDispatchDetail(Document):
	def validate(self):
		if(self.pick_value != self.total_pick):
			frappe.throw(_("Pick value & Total pick must be equal"))

	def on_submit(self):
		self.make_stock_entry()

	def on_cancel(self):
		self.cancel_stock_entry()

	def make_stock_entry(self):
		"""create stock entry for fabric dispatch detail"""
		se = frappe.new_doc("Stock Entry")
		se.posting_date = self.dispatch_date
		se.purpose = "Material Issue"
		se.fabric_despatch_detail = self.name
		bt = self.get("weft_yarn")
		for item in bt:
			bt_row = se.append("items")
			bt_row.item_code = item.weft_yarn
			bt_row.qty = item.yarn_value
			# bt_row.basic_rate = item.rate
			bt_row.s_warehouse = "Stores - S"
		se.submit()

	def cancel_stock_entry(self):
		stock_entries = frappe.db.sql("""select name from `tabStock Entry` where fabric_despatch_detail='%s'"""%(self.name))
		if(stock_entries):
			for se in stock_entries:
				stock_e = frappe.get_doc("Stock Entry",se[0])
				stock_e.cancel()


@frappe.whitelist()
def get_beam_values(beam_inward):
	return frappe.db.sql("""select weft_yarn, yarn_value from `tabConsumption Yarn` where parent = '%s'"""%(beam_inward),as_dict=1)

