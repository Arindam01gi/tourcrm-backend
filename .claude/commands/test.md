---
description: Analyze the current file and generate a corresponding test in `tests/`. Use Django TestCase and mock any database or network calls where appropriate.
---

# Workflow: Generate Tests

Use this workflow to ensure business logic is verified and stable.

## Steps
1. **Analyze Target**: Identify the functions/classes to test (usually in `services.py` or `serializers.py`).
2. **Setup Fixtures**: Use factories or `setUp` to prepare the test state.
3. **Write Test Cases**:
   - Follow the **AAA** pattern (Arrange, Act, Assert).
   - Test "Happy Path" (success cases).
   - Test "Edge Cases" (validation errors, empty lists, etc.).
4. **Mocking**: Use `unittest.mock` to intercept external API calls or non-deterministic behavior.
5. **Execution**: Provide the command:
   ```bash
   python manage.py test <app_name>
   ```
