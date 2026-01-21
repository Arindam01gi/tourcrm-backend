---
description: Help with complex migrations. Assist in data-migration scripts or renaming fields safely without downtime.
---

# /migration

Use this workflow for data transformations or schema changes that require manual intervention.

## Workflow
1. **Analyze Change**: Understand the schema change (e.g., renaming a field, adding a unique constraint).
2. **Safety Check**: Identify potential data loss risks. If renaming a field, consider the "Expand and Contract" pattern to avoid downtime.
3. **Data Migration**: Create an empty migration if logic is required:
   ```bash
   python manage.py makemigrations --empty <app_name>
   ```
4. **Write Logic**:
   - Implement the `RunPython` logic.
   - **Crucial**: Always implement the `reverse_code` argument to ensure rollback capability.
5. **Performance**: If processing large datasets, use batching (e.g., `queryset.iterator()` and `bulk_update`).
6. **Verification**: Run migrations locally and check data integrity.

// turbo
7. **Backup**: Remind the user to back up the database before running complex migrations.
