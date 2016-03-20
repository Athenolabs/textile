# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "textile"
app_title = "TextTile"
app_publisher = "pitambar"
app_description = "Managing in out of fabrics"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pitambar.hatwar@gmail.com"
app_version = "0.0.1"
app_license = "gpl"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/textile/css/textile.css"
# app_include_js = "/assets/textile/js/textile.js"

# include js, css files in header of web template
# web_include_css = "/assets/textile/css/textile.css"
# web_include_js = "/assets/textile/js/textile.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "textile.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "textile.install.before_install"
# after_install = "textile.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "textile.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"textile.tasks.all"
# 	],
# 	"daily": [
# 		"textile.tasks.daily"
# 	],
# 	"hourly": [
# 		"textile.tasks.hourly"
# 	],
# 	"weekly": [
# 		"textile.tasks.weekly"
# 	]
# 	"monthly": [
# 		"textile.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "textile.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "textile.event.get_events"
# }

fixtures = ["Custom Field"]
