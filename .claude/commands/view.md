---
description: Create a new API view (or ViewSet). Check if it needs a new serializer or specific permission classes based on project patterns.
---

# Workflow: Create API View

Use this workflow to expose a new endpoint via DRF.

## Steps
1. **Identify Pattern**: Is this a standard CRUD operation (use `ModelViewSet`) or a specialized action (use `@action` or a custom `APIView`)?
2. **Serializer Check**: 
   - Check if an existing serializer in `serializers.py` can be reused.
   - If not, create a new one following project naming conventions (e.g., `<Model>Serializer`).
3. **Draft View**:
   - Inherit from appropriate DRF class.
   - Set `queryset`, `serializer_class`, and `permission_classes`.
4. **URL Routing**: Add the route to the app's `urls.py`.
5. **Validation**: Ensure business logic is delegated to a service in `services.py` if complex.
