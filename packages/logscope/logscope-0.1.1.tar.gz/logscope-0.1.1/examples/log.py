from logscope import logger

# Create a logger with default settings
log = logger()

# Log some messages
log("Starting application")
log("Processing data", {"count": 100})

def example_function():
    log("Running example function")

example_function()