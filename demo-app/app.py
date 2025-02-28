from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Initialize Tracer
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Exporter Configuration
otlp_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

# Flask App
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    with tracer.start_as_current_span("hello-span"):
        return "Hello, OpenTelemetry!"

@app.route("/process")
def process():
    with tracer.start_as_current_span("process-span") as span:
        span.set_attribute("custom.attribute", "demo-processing")
        return "Processing completed!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
