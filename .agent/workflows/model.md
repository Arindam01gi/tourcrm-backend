---
description: Create a new Django model. Suggest fields, help with meta classes, and generate migration command.
---

# /model

Create a new Django model in the specified app.

## Workflow
1.  **Analyze Request**: Identify the app and the purpose of the model.
2.  **Suggest Fields**: Propose field types (CharField, ForeignKey, etc.) based on the requirements.
3.  **Define Meta**: Include proper `verbose_name`, `verbose_name_plural`, and `ordering`.
4.  **Implement**: Write the code to the app's `models.py` or a new file in `models/`.
5.  **Migration**: Prompt the user to run `python manage.py makemigrations` and `python manage.py migrate`.

// turbo
6.  **Verify**: Check for field naming consistency and index suggestions.
