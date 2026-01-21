---
description: Help with complex migrations. Assist in data-migration scripts or renaming fields safely without downtime.
---

# Workflow: Complex Migrations

Use this workflow for data transformations or schema changes that require manual intervention.

## Steps
1. **Define Strategy**: If renaming a field, consider the "Expand and Contract" pattern to avoid downtime.
2. **Data Migration**: Create an empty migration:
   ```bash
   python manage.py makemigrations --empty <app_name>
   ```
3. **Write Logic**:
   - Implement the `RunPython` logic.
   - **Crucial**: Always implement the `reverse_code` argument to ensure rollback capability.
4. **Performance**: If processing large datasets, use batching (e.g., `queryset.iterator()` and `bulk_update`).
5. **Verification**: Run migrations locally and check data integrity.
