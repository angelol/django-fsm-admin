# django-fsm-2-admin

Mixin and template tags to integrate [django-fsm-2](https://github.com/pfouque/django-fsm-2) state transitions into the Django Admin.

> [!IMPORTANT]
> This project is a fork of [django-fsm-admin](https://github.com/gadventures/django-fsm-admin), actively maintained and enhanced. 
> It utilizes [django-fsm-2](https://github.com/pfouque/django-fsm-2) for state transitions in the Django Admin interface.

# Installation

```bash
pip install django-fsm-2-admin
```

Or from GitHub:

```bash
pip install -e git://github.com/coral-li/django-fsm-2-admin.git#egg=django-fsm-2-admin
```

# Usage

1. Add ``fsm_admin`` to your ``INSTALLED_APPS``.

2. In your ``admin.py`` file, use ``FSMTransitionMixin`` to add behaviour to your ModelAdmin. ``FSMTransitionMixin`` should be before ``ModelAdmin``, the order is important.

It assumes that your workflow state field is named ``state``, however you can override it or add additional workflow state fields with the attribute ``fsm_field``.

```python
from fsm_admin.mixins import FSMTransitionMixin

class YourModelAdmin(FSMTransitionMixin, admin.ModelAdmin):
      # The name of one or more FSMFields on the model to transition
      fsm_field = ['wf_state',]

admin.site.register(YourModel, YourModelAdmin)
```

3. By adding ``custom=dict(admin=False)`` to the transition decorator, one can disallow a transition to show up in the admin interface. This specially is useful, if the transition method accepts parameters without default values, since in **django-fsm-2-admin** no arguments can be passed into the transition method.

```python
@transition(
   field='state',
   source=['startstate'],
   target='finalstate',
   custom=dict(admin=False),
)
def do_something(self, param):
   # will not add a button "Do Something" to your admin model interface
```

By adding ``FSM_ADMIN_FORCE_PERMIT = True`` to your configuration settings, the above restriction becomes the default. Then one must explicitly allow that a transition method shows up in the admin interface.

```python
@transition(
      field='state',
      source=['startstate'],
      target='finalstate',
      custom=dict(admin=True),
)
def proceed(self):
      # will add a button "Proceed" to your admin model interface
```

This is useful, if most of your state transitions are handled by other means, such as external events communicating with the API of your application.

# Try the example

```bash
git clone git@github.com:coral-li/django-fsm-2-admin.git
cd django-fsm-2-admin
uv venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
python setup.py develop
cd example
python manage.py migrate
python manage.py createsuperuser --username admin
python manage.py runserver
```
