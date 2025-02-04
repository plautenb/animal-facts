# Animal Facts Testing Project

## Test Cases

| Test Case ID        | Description                                                                   | Input Params                             | Expected Output                                                     | Status  |
|---------------------|-------------------------------------------------------------------------------|------------------------------------------|---------------------------------------------------------------------|---------|
| test_get_one_fact   | Check if one fact about animal was received and text of response is not empty | None                                     | 200 OK, reponse                                                     | ✅ Pass |
| test_get_many_facts | Check if getting many facts about specific animal works                       | animal = ["cat", "dog"], amount = [2, 3] | 200 OK, correct number of facts, correct type of animal in response | ✅ Pass |

### Notes:
- ✅ Pass → Test case passed successfully
- ❌ Fail → Test case failed, needs fixing
