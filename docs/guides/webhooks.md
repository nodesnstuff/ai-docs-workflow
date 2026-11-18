# Receive webhooks

Parcelo can notify your application when a parcel changes status.

## Register an endpoint

Send your endpoint URL to the Parcelo support team. Endpoints must use HTTPS.

## Payload

Parcelo sends a `POST` request with a JSON body:

```json
{
  "event": "parcel.status_changed",
  "tracking_id": "PCL-1001",
  "status": "out_for_delivery"
}
```

## Respond to a webhook

Return any `2xx` status code within 5 seconds to acknowledge the event.
