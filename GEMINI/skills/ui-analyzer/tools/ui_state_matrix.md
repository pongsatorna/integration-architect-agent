# Mobile UI State Matrix

When analyzing a UI, the API contract must support the following states for every "Data Screen" to ensure a robust mobile experience.

## 1. Data Availability States
- **Success (Has Data):** The primary path.
- **Empty (No Data):** Does the UI show a specific "Empty" illustration or message?
- **Partial (Missing Fields):** Are some fields optional? How does the UI handle a `null` value?

## 2. Technical Feedback States
- **Loading (Chunked):** Does the UI use skeleton loaders? If so, does the API support partial payloads?
- **Error (Technical):** Mapping 4xx/5xx errors to user-friendly messages.
- **Error (Business):** (e.g., "Account Locked," "Insufficient Funds") - The API must return a specific `errorCode` and `userMessage`.

## 3. Interaction States
- **Refreshing:** Supports Pull-to-Refresh.
- **Pagination:** Supports `offset`/`limit` or `cursor`. Look for lists in the design.
- **Search/Filter:** Does the UI have a search bar? The API must support query parameters.

## 4. Security & Compliance
- **Masked Data:** Does the UI show asterisks (e.g., **** 1234)? The API must mask this data at the source.
- **Permissions:** Are some buttons hidden for certain users? The API should return a `permissions` or `capabilities` object.
