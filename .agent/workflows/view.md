---
description: Create a new API view (or ViewSet). Check for serializers and permission classes.
---

# /view

Create a new DRF API View or ViewSet.

## Workflow
1.  **Analyze Pattern**: Check existing ViewSets in `apps/` to match styling.
2.  **Serializer Check**: Determine if a new Serializer is needed or if an existing one can be reused.
3.  **Define Permissions**: Suggest `IsAuthenticated` or custom permissions based on the use case.
4.  **Implement**: Write the ViewSet code.
5.  **Routes**: Update the app's `urls.py` with the new route.

// turbo
6.  **Refactor**: Ensure business logic is delegated to the service layer.
