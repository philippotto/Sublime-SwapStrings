import sublime
from unittest import TestCase

version = sublime.version()

class TestSwapStrings(TestCase):

	def setUp(self):

		self.view = sublime.active_window().new_file()


	def tearDown(self):

		if self.view:
			self.view.set_scratch(True)
			self.view.window().run_command("close_file")


	def assertSimpleSwap(self, testStr, expectedStr, stringA, stringB):

		self.view.run_command("insert", {"characters": testStr})
		self.view.run_command("swap_strings", dict(stringA = stringA, stringB = stringB))

		contentRegion = sublime.Region(0, self.view.size())
		bufferContent = self.view.substr(contentRegion)

		self.assertEqual(bufferContent, expectedStr)


	def testSimpleSwap(self):

		testStr = "aaa bbb aaa"
		expectedStr = "bbb aaa bbb"
		self.assertSimpleSwap(testStr, expectedStr, "a", "b")


	def testHalfEmptySwap(self):

		testStr = "aaa bbb aaa"
		expectedStr = " bbb "
		self.assertSimpleSwap(testStr, expectedStr, "a", "")


	def testSubstringSwap(self):

		testStr = "abc abcd abc"
		expectedStr = "abcd abc abcd"
		self.assertSimpleSwap(testStr, expectedStr, "abc", "abcd")

