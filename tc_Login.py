import unittest

from LogIn.login import LoginFlow

tc = unittest.TestLoader().loadTestsFromTestCase(LoginFlow)

result = unittest.TextTestRunner(verbosity=9).run(tc)


print("result: %s" % result)
print("results.wasSuccessful: %s" % result.wasSuccessful())
if result.wasSuccessful():
    print("PASSED")
else:
    print("FAILED")

