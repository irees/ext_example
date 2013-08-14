from emen2.web.view import View

# Use the decorators provided by the View class
# to register view classes with the web server.

# View.register will register this class and decorated methods.
@View.register
class ExampleView(View):

	# View.add_matcher takes a regular expression, or several regular expressions,
	# and associates this view and method in the web server. So, in this example,
	# 		http://localhost:8080/exampple
	#  would cause this view to be loaded, and the main() method run.
	
	@View.add_matcher(r'^/example/$')
	def main(self):
		# You can set self.title here, or using the title block
		# in the template.
		self.title = "Example view"

		# Set self.template to designate the template used.
		self.template = "/example/example"
		
		# self.ctxt is a dictionary that is passed to the template renderer.
		self.ctxt["message"] = "This is an example template."
	
		
	# Note: multiple regular expressions can be registered for a view.
	
	@View.add_matcher(r'^/example/(?P<name>\w+)/edit/$', r'^/example/new/$')
	def edit_real(self, name=None, folder_description=None):
		# Title and template
		self.title = "Example form"
		self.template = "/example/example.edit"

		# Add a key to the template context.
		self.ctxt["name"] = name
		
		# Get a record to edit, or create a new record.
		# The Database Handle is available as: 
		# 	self.db
		if name:
			rec = self.db.record.get(name)
			rec['name_folder'] = 'Test'
		else:
			rec = self.db.record.new(rectype="folder")
	
		# If the form was submitted, save the record.
		if self.request_method == 'post':
			# Set the value in the record..
			rec['folder_description'] = folder_description

			# ... commit the record.
			rec = self.db.record.put(rec)

			# Use a redirect to avoid clients double-POSTing.
			self.redirect('%s/example/%s/edit/'%(self.ctxt['EMEN2WEBROOT'], rec.name))
			return
			
		self.ctxt['rec'] = rec