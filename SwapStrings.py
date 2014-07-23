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

		else:
			view = self.view
			selection = view.sel()

			for region in selection:
				if region.a == region.b:
					# use entire line if regions is only a point
					region = view.line(region)

				regionStr = view.substr(region)

				swapToken = self.generateSwapToken(regionStr, stringA, stringB)

				if len(stringB) > len(stringA):
					# ensures that swapping is correct even if stringA is in stringB
					stringA, stringB = stringB, stringA

				regionStr = regionStr \
					.replace(stringA, swapToken) \
					.replace(stringB, stringA) \
					.replace(swapToken, stringB)

				view.replace(edit, region, regionStr)


	def generateSwapToken(self, regionStr, stringA, stringB):

		# requirements:
		# swapToken must not be in regionStr, stringA and stringB
		# TODO: regionStr, stringA and stringB must not be in swapToken

		swapToken = "tmp_token"
		while swapToken in regionStr + stringA + stringB:
			swapToken += "4b5c7fb7"

		return swapToken


	def onConfirm(self, swapString):

		a, b = swapString.split("<>")
		self.view.run_command("swap_strings", dict(stringA=a, stringB=b))

