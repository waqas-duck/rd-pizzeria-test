# rd-pizzeria-test

Private test repo for the RubberDuck GitHub App (dev app only). Copied from the Rubber Duck Pizzeria demo in RubberDuck-com/rubberduck-use-case-playground (MIT, see LICENSE). The app contains intentional vulnerabilities; do not deploy it.

## Kiosk service

kiosk/ holds the Express front for in-store kiosks (npm start, port 5100).
Set KITCHEN_URL when the Flask app is not on 127.0.0.1:5000.
