import sublime, sublime_plugin

class SwapBulletsCommand(sublime_plugin.TextCommand):

	def run(self, edit, bulletA=None, bulletB=None):

		if not bulletA and not bulletB:
			inputView = sublime.active_window().show_input_panel(
				"Specify the bullets which shall be swapped. <> functions as a separator.",
				"\"<>'",
				self.onConfirm,
				None,
				None
			)
			inputView.run_command("select_all")

		else:
			view = self.view
			selection = view.sel()
			bulletA, bulletB = self.ensureOrder(bulletA, bulletB)

			for region in selection:
				if region.a == region.b:
					# use entire line if regions is only a point
					region = view.line(region)

				regionStr = view.substr(region)

				if bulletB == "":
					regionStr = regionStr.replace(bulletA, "")
				else:
					swapToken = self.generateSwapToken(regionStr, bulletA, bulletB)

					regionStr = regionStr \
						.replace(bulletA, swapToken) \
						.replace(bulletB, bulletA) \
						.replace(swapToken, bulletB)

				view.replace(edit, region, regionStr)


	def ensureOrder(self, bulletA, bulletB):

		# ensures that len(bulletA) >= len(bulletB)
		# this is important for the edge case in which bulletA is a substring of bulletB

		if len(bulletB) > len(bulletA):
			bulletA, bulletB = bulletB, bulletA

		return bulletA, bulletB


	def generateSwapToken(self, regionStr, bulletA, bulletB):

		# requirements derived by the three replacements:
		# 1: uncritical since bulletA >= bulletB.
		# 2: bulletB must not be in swapToken.
		# 3: swapToken must not be in bulletA and not in regionStr.
		# 	 mind that bulletA is not necessarily a substring of regionStr.

		#	choose swapToken so that bulletB cannot be in swapToken
		swapToken = bulletB[:-1]

		while swapToken in bulletA + regionStr:
			# extend swapToken with a character so that it isn't bulletB
 			swapToken += chr(ord(bulletB[-1]) + 1 % 255)

		return swapToken


	def onConfirm(self, swapBullet):

		if "<>" not in swapBullet:
			sublime.status_message("No <> was found for swapping bullet.")
			return

		(a, b) = swapBullet.split("<>")
		self.view.run_command("swap_bullets", dict(bulletA=a, bulletB=b))

