# rd-pizzeria-test

Private test repo for the RubberDuck GitHub App (dev app only). Copied from the Rubber Duck Pizzeria demo in RubberDuck-com/rubberduck-use-case-playground (MIT, see LICENSE). The app contains intentional vulnerabilities; do not deploy it.

## Review helpers

list_reviews is capped (50 by default) and covered by tests/test_db.py.
Run the tests with python -m pytest tests -q from the repo root.
