import sublime, sublime_plugin

class SwapStringsCommand(sublime_plugin.TextCommand):

	def run(self, edit, stringA=None, stringB=None):

		if not stringA and not stringB:
			inputView = sublime.active_window().show_input_panel(
				"Specify the strings which shall be swapped. <> functions as a separator.",
				"\"<>'",
				self.onConfirm,
				None,
				None
			)
			inputView.run_command("select_all")

		else:
			view = self.view
			selection = view.sel()
			stringA, stringB = self.ensureOrder(stringA, stringB)

			for region in selection:
				if region.a == region.b:
					# use entire line if regions is only a point
					region = view.line(region)

				regionStr = view.substr(region)
				swapToken = self.generateSwapToken(regionStr, stringA, stringB)


				regionStr = regionStr \
					.replace(stringA, swapToken) \
					.replace(stringB, stringA) \
					.replace(swapToken, stringB)

				view.replace(edit, region, regionStr)


	def ensureOrder(self, stringA, stringB):

		# ensures that len(stringA) >= len(stringB)
		# this is important for the edge case in which stringA is a substring of stringB

		if len(stringB) > len(stringA):
			stringA, stringB = stringB, stringA

		return stringA, stringB


	def generateSwapToken(self, regionStr, stringA, stringB):

		# requirements derived by the three replacements:
		# 1: uncritical since stringA >= stringB.
		# 2: stringB must not be in swapToken.
		# 3: swapToken must not be in stringA and not in regionStr.
		# 	 mind that stringA is not necessarily a substring of regionStr.

		#	choose swapToken so that stringB cannot be in swapToken
		swapToken = stringB[:-1]

		while swapToken in stringA + regionStr:
			# extend swapToken with a character so that it isn't stringB
 			swapToken += chr(ord(stringB[-1]) + 1 % 255)

		return swapToken


	def onConfirm(self, swapString):

		(a, b) = swapString.split("<>")
		self.view.run_command("swap_strings", dict(stringA=a, stringB=b))

