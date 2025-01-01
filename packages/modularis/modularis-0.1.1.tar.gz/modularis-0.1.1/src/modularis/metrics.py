from prometheus_client import Counter, Histogram, Gauge
import time
from typing import Dict, Any
from .response import Response

class MetricsCollector:
    def __init__(self):
        self.requests_total = Counter(
            'modularis_requests_total',
            'Total number of HTTP requests made',
            ['method', 'status']
        )
        
        self.request_duration_seconds = Histogram(
            'modularis_request_duration_seconds',
            'HTTP request duration in seconds',
            ['method']
        )
        
        self.active_requests = Gauge(
            'modularis_active_requests',
            'Number of currently active HTTP requests',
            ['method']
        )
        
        self._start_times: Dict[str, float] = {}

    def start_request(self, method: str, url: str) -> str:
        request_id = f"{method}:{url}:{time.time()}"
        self._start_times[request_id] = time.time()
        self.active_requests.labels(method=method).inc()
        return request_id

    def record_request(self, method: str, url: str, response: Response):
        request_id = f"{method}:{url}:{self._start_times.get(method, 0)}"
        duration = time.time() - self._start_times.get(request_id, time.time())
        
        self.requests_total.labels(
            method=method,
            status=str(response.status)
        ).inc()
        
        self.request_duration_seconds.labels(
            method=method
        ).observe(duration)
        
        self.active_requests.labels(method=method).dec()
        
        self._start_times.pop(request_id, None)

    def get_metrics(self) -> Dict[str, Any]:
        return {
            'total_requests': self.requests_total._value.sum(),
            'average_duration': self.request_duration_seconds._sum.sum() / max(self.request_duration_seconds._count.sum(), 1),
            'active_requests': self.active_requests._value.sum()
        }
