# Case Study: Assertions Passed but the External-App Test Hung

## Incident

Control assertions passed, but the client connection was closed without waiting for protocol-level shutdown. A live socket/handle remained, so the test process did not exit naturally.

A separate startup failure in the same integration was caused by the machine/display environment rather than the application code itself.

## Correction

The lifecycle gate was split into independent checks:

1. process started
2. application ready
3. control command succeeded
4. state was read back
5. client disconnected cleanly
6. application/process shut down as intended
7. sockets/handles/orphans were absent

Environment-specific startup workarounds were kept process-scoped rather than applied globally.

## General Rule

> Assertion success does not prove lifecycle completion.

Startup, readiness, control, disconnect, shutdown, and cleanup are separate engineering facts.
