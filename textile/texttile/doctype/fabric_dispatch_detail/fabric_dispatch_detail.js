// Copyright (c) 2016, pitambar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fabric Dispatch Detail', {
	// meters: function(frm){
	// 	frm.doc.fold_less = parseInt(frm.doc.meters/100) || 0;
	// 	refresh_field("fold_less");
	// },

	meters: function(frm){
		refresh_total_meters(frm);
	},

	fold_less: function(frm){
		refresh_total_meters(frm);
	},
});

function refresh_total_meters(frm){
	frm.doc.total_meters=0;
	if(frm.doc.fold_less==0)
	{
		frm.doc.total_meters = frm.doc.meters;
	}
	else
	{
		frm.doc.total_meters = (frm.doc.meters || 1)-((frm.doc.meters || 1) * (frm.doc.fold_less|| 1));	
	}
	refresh_field("total_meters");
}

frappe.ui.form.on("Consumption Yarn","yarn_value",function(frm){
	refresh_consumption_item(frm);
});

frappe.ui.form.on("Consumption Yarn", "weft_yarn_remove", function(frm) {
	refresh_consumption_item(frm);
});

function refresh_consumption_item(frm){
	frm.doc.total_pick = 0;
	$.each(frm.doc["weft_yarn"] || [], function(i, wy) {
		frm.doc.total_pick += wy.yarn_value;
	});
	refresh_field("total_pick");
}
cur_frm.add_fetch("beam_inward","quality","quality");
cur_frm.add_fetch("beam_inward","design_no","design_no");
// cur_frm.add_fetch("beam_inward","weft_yarn","weft_yarn");

frappe.ui.form.on('Fabric Dispatch Detail',"beam_inward",function(frm){
	frappe.call({
		method: "textile.texttile.doctype.fabric_dispatch_detail.fabric_dispatch_detail.get_beam_values",
		args: { "beam_inward": frm.doc.beam_inward},
		callback: function(r) {
			total_pick=0;
			if(r.message) {
				$.each(r.message, function(field, value) {
					row = frappe.model.add_child(frm.doc, "Consumption Yarn", "weft_yarn");
					row.weft_yarn = r.message[field]['weft_yarn'];
					row.yarn_value = r.message[field]['yarn_value'];
					total_pick+=r.message[field]['yarn_value'];
				})
				frm.set_value('total_pick',total_pick)
				refresh_field('weft_yarn')
			}
		}
	});
});