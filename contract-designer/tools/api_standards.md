# Mobile API Design Standards

## 1. Global Response Envelope
All mobile API responses MUST be wrapped in this standard envelope. The actual business data goes inside the `data` object.

```json
{
  "meta": {
    "timestamp": "2026-06-11T08:30:00Z",
    "requestId": "uuid-v4-string"
  },
  "data": {}, 
  "errors": []
}