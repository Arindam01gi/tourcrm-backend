---
description: Analyze current file and generate tests in tests/ using Django TestCase.
---

# /test

Generate unit or integration tests for the current code.

## Workflow
1.  **Analyze Code**: Scan the current file (Service, View, or Model).
2.  **Identify Test Cases**: List happy paths, edge cases, and failure scenarios.
3.  **Generate Test**: Write the test class using Django's `TestCase` or `APITestCase`.
4.  **Identify Fixtures**: Use `setUpTestData` for shared state.
5.  **Implementation**: Add tests to `tests.py` or the `tests/` directory of the app.

// turbo
6.  **Run Tests**: Suggest running `python manage.py test` to verify.
