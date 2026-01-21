# Project Configuration: TourCRM Backend

## Project Overview
- **Framework**: Django 4.2+
- **API Engine**: Django Rest Framework (DRF)
- **Database**: MySQL (using `mysqlclient`)
- **Authentication**: JWT (SimpleJWT)
- **Primary Apps**: `apps.accounts`, `apps.itinerary`

## Backend Architecture Standards

### ORM and Database
- **N+1 Prevention**: Always use `select_related()` for ForeignKey/OneToOne and `prefetch_related()` for ManyToMany/Reverse relationships.
- **Indexing**: All fields used in `filter()`, `exclude()`, or `order_by()` must have a database index unless they are primary keys.
- **Migrations**: Never use `RunPython` without a `reverse_code` function unless it's strictly impossible.

### API Standards (DRF)
- **Serializers**: Prefer `serializers.ModelSerializer` for standard CRUD. Use manual `serializers.Serializer` for complex data transformations or aggregate reports.
- **Views**: Use Class-Based Views (CBVs) or ViewSets. Function-Based Views (FBVs) are discouraged unless for very simple webhooks.
- **Payloads**: Use camelCase for JSON keys (configured via DRF settings if applicable, otherwise manual).
- **Permissions**: Every view must have explicit `permission_classes`. Default is `IsAuthenticated`.

### Business Logic (The Services Layer)
- **Negative Constraint**: Do NOT put business logic in `views.py` or `models.py`.
- **Services**: All business logic (external API calls, complex calculations, multi-model updates) must reside in `services.py` modules within each app.
- **Slim Views, Fat Services**: Views should only handle request validation, calling services, and returning responses.

### Testing Philosophy
- **Standard**: Django `TestCase`.
- **Target**: 90% coverage for business logic in `services.py`.
- **Patterns**: Strictly follow the **AAA (Arrange-Act-Assert)** pattern.
- **Isolation**: Use `mock` for external network calls and heavy IO operations.

## Path Aliases and Registry
- **Root**: `e:/projects/tourcrm-backend/`
- **Apps Root**: `apps/`
- **Config**: `config/`
- **Migrations**: `apps/<app_name>/migrations/`
