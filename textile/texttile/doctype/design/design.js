// Copyright (c) 2016, pitambar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Design', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Design","cut",function(frm){
	calculate_beam_total(frm);
})

frappe.ui.form.on("Design","lasa",function(frm){
	calculate_beam_total(frm);	
})

function calculate_beam_total(frm){
	frm.doc.beam_meters = 0;
	frm.doc.beam_meters = (frm.doc.cut||1) * (frm.doc.lasa||1);
	refresh_field("beam_meters");
}