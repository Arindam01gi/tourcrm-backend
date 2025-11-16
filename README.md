 ## Folder structure of this app
 tourcrm-bakend/
│
├── config/                     ← core/settings folder
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py            ← shared settings
│   │   ├── dev.py             ← development configs
│   │   ├── prod.py            ← production configs
│   │   └── celery.py          ← celery config (future)
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                       ← utilities used across all apps
│   ├── models.py               ← abstract models (timestamps, soft delete)
│   ├── permissions.py          ← RBAC helpers
│   ├── mixins.py               ← pagination / role mixins
│   ├── utils.py                ← helpers
│   └── exceptions.py
│
├── apps/
│   ├── accounts/               ← Users + Auth + JWT + Workspace membership
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── organization.py
│   │   │   ├── membership.py
│   │   │   └── role.py
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── leads/
│   │   ├── models/
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── itinerary/
│   │   ├── models/
│   │   ├── services/           ← itinerary generation logic
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── estimation/
│   │   ├── models/
│   │   ├── services/           ← price engine
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── followups/
│   │   ├── models/
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── tasks.py            ← celery tasks for reminders
│   │   └── urls.py
│   │
│   ├── reports/
│   │   ├── models/
│   │   ├── analytics/          ← aggregation queries
│   │   ├── views/
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   └── integrations/
│       ├── meta_api/
│       │   ├── views.py        ← meta webhook handler
│       │   ├── services.py
│       │   ├── urls.py
│       │   └── admin.py
│       └── pdf/
│           ├── services.py
│           └── templates/      ← Django templates for pdf
│
├── static/
├── media/
├── requirements.txt
└── manage.py
