---
description: Analyze Django traceback errors, IntegrityErrors, or JWT issues.
---

# /debug-errors

Analyze and resolve backend errors and tracebacks.

## Workflow
1.  **Analyze Traceback**: Read the provided error message or check recent logs.
2.  **Identify Root Cause**: Determine if it's a database error (`IntegrityError`), app logic (`AttributeError`), or auth issue.
3.  **Check Context**: Inspect relevant models, views, or middleware.
4.  **Propose Fix**: Provide the code fix or configuration change.
5.  **Verify**: Suggest how to test the fix.

// turbo
6.  **Prevention**: Suggest code changes to prevent similar errors in the future (e.g., better null handling).
