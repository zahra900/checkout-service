# Checkout Service

Checkout Service is responsible for handling the checkout flow for ticket reservations.
It validates users, manages inventory reservation, handles idempotency, and coordinates payment processing.

This service is designed to be **stateless**, **idempotent**, and **safe under concurrency**.

---

## Responsibilities

- Validate user eligibility
- Check availability and reserve tickets
- Enforce rate limiting
- Ensure idempotent checkout requests
- Persist checkout state
- Trigger asynchronous post-checkout tasks

---

## High-Level Flow

1. Client sends checkout request with `idempotency_key`
2. Rate limit is checked (Redis)
3. User and event validation
4. Ticket availability is verified
5. Reservation is created (transactional)
6. Checkout state is stored
7. Background worker handles async steps (payment, notifications)

---

## Architecture

- **API**: FastAPI
- **Database**: PostgreSQL
- **Cache / Rate limiting / Idempotency**: Redis
- **Async processing**: Background worker
- **Diagram**: `/docs/architecture.puml`

---

## API Endpoint

### `POST /checkout`

**Request**
```json
{
  "user_id": "uuid",
  "event_id": "uuid",
  "quantity": 2,
  "idempotency_key": "string"
}
