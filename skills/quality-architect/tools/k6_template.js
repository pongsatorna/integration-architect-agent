// Standard K6 Load Test Template
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 20 }, // Ramp-up to 20 users
    { duration: '3m', target: 20 }, // Stay at 20 users
    { duration: '1m', target: 0 },  // Ramp-down to 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests must be below 500ms
    http_req_failed: ['rate<0.01'],   // Error rate must be less than 1%
  },
};

export default function () {
  const url = __ENV.BASE_URL || 'http://localhost:8080';
  const res = http.get(`${url}/path/to/endpoint`);
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'body matches schema': (r) => r.json() !== null,
  });

  sleep(1);
}
