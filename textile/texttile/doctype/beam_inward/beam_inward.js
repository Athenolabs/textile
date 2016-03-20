// Copyright (c) 2016, pitambar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Beam Inward', {
	refresh: function(frm) {

	}
});

cur_frm.add_fetch("design_no","quality","quality")
cur_frm.add_fetch("design_no","cut","cut")
cur_frm.add_fetch("design_no","lasa","lasa")
cur_frm.add_fetch("design_no","beam_meters","beam_meter")

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