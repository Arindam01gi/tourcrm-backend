---
description: Create a new Django model. Suggest fields, help with meta classes, and immediately generate the migration command.
---

# Workflow: Create Model

Use this workflow when you need to add a new entity to the database.

## Steps
1. **Analyze Requirements**: Understand the entity's purpose and relationships.
2. **Define Model**:
   - Suggest appropriate field types (e.g., `CharField`, `ForeignKey`, `JSONField`).
   - Add `help_text` and `verbose_name`.
   - Implement `Meta` class (ordering, verbose names, unique constraints).
   - Define a string representation method `__str__`.
3. **Register in Admin**: Suggest code for `admin.py`.
4. **Generate Migration**: Provide the command:
   ```bash
   python manage.py makemigrations <app_name>
   ```
5. **Validate**: Check for missing indexes or potential N+1 relationship traps.
