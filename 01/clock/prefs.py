# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import sys
sys.path.append('lib')

import webapp2

from models import models


class PrefsPage(webapp2.RequestHandler):
	def post(self):
		userprefs = models.get_userprefs()
		try:
			tz_offset = float(self.request.get('tz_offset'))
			userprefs.tz_offset = tz_offset
			userprefs.put()
		except ValueError:
			# User entered a value that wasn't a float. Ignore for now.
			pass

		self.redirect('/')


application = webapp2.WSGIApplication([('/prefs', PrefsPage)],
                                      debug=True)
