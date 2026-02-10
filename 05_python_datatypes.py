const_results = [
  { "testName": "LoginTest", "status": "PASS" },
  { "testName": "PaymentTest", "status": "FAIL" },
  { "testName": "LoginTest", "status": "FAIL" },
  { "testName": "SearchTest", "status": "PASS" },
  { "testName": "PaymentTest", "status": "PASS" }
]

status_map = {}
flaky_tests = []

# collect statuses per test
for result in const_results:
    name = result["testName"]
    status = result["status"]
    if name  in status_map and status_map[name] != status:
        flaky_tests.append(name)
    else:
        status_map[name] = status

print(flaky_tests)