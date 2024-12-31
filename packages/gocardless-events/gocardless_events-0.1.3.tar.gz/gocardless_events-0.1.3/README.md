# gocardless event schemas

> This is an unofficial library. GoCardless provide the [gocardless-pro python library](https://pypi.org/project/gocardless-pro/).
> The reason this exists is because that library is not typed.

Type-safe Python models for for all GoCardless events (using Pydantic).

This is a Python implementation of the Event Actions in the [GoCardless docs](https://developer.gocardless.com/api-reference#event-actions).

Since we only use Python 3.13+ this library doesn't support older versions, but
PRs are welcome.

## Why does this exist

GoCardless' docs are good, but they don't publish an OpenAPI spec or JSON schemas for
their events. Their Python client library is untyped, so deserialization of the events
is not type-safe.

## How it's made

We pulled all the event specs from the GoCardless docs site as HTML, cleaned
them, preproccessed them into a JSON pseudo-schema, and then generated Pydantic
models from that schema.
