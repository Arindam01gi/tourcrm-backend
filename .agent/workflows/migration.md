---
description: Help with complex migrations, data scripts, or safe field renaming.
---

# /migration

Assist with complex Django database migrations.

## Workflow
1.  **Analyze Change**: Understand the schema change (e.g., renaming a field, adding a unique constraint).
2.  **Safety Check**: Identify potential data loss risks.
3.  **Generate Plan**: Suggest a multi-step migration if needed (e.g., add new field -> migrate data -> remove old field).
4.  **Data Scripts**: Support writing `RunPython` operations for data migrations.
5.  **Command**: Provide the command to run the migration.

// turbo
6.  **Backup**: Remind the user to back up the database before running complex migrations.
