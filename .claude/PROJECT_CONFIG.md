# Project Configuration: TourCRM Backend

## Project Overview
- **Framework**: Django 4.2
- **API Framework**: Django Rest Framework (DRF)
- **Database**: MySQL
- **Auth Strategy**: JWT (SimpleJWT)
- **Task Queue**: None (Currently synchronous)
- **Testing**: Django standard `TestCase`

## ORM Rules
- Always use `select_related` and `prefetch_related` to avoid N+1 queries in ViewSets and Serializers.
- Use `QuerySet` methods for complex logic to keep models slim.
- Ensure all models have proper `Meta` classes with `verbose_name` and `ordering`.

## Serializer Standards
- Use `serializers.ModelSerializer` for standard CRUD operations to leverage DRF's built-in validation.
- Explicitly define `fields` in Meta; do not use `'__all__'` in production code to prevent over-exposure.
- Use `SerializerMethodField` only when necessary for performance reasons.

## Testing Philosophy
- Target 90% coverage for business logic located in `services.py` or model methods.
- Use `setUpTestData` for performance optimization in test classes.
- Each app should have its own `tests/` directory or `tests.py` file.

## Architecture & Constraints
- **Negative Constraint**: Do NOT put business logic in `views.py`. Views should handle request parsing and response formatting.
- **Service Layer**: Implement business logic in `apps/<app_name>/services.py` or similar service modules.
- **Signals**: Use signals sparingly. Prefer explicit service calls for side effects.
- **Environment**: All configuration must be environment-variable driven via `django-environ`.

## Path Aliases & Registry
- Root: `e:/projects/tourcrm-backend/`
- Apps: `e:/projects/tourcrm-backend/apps/`
- Config: `e:/projects/tourcrm-backend/config/`
