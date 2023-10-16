# config


# Add a note in the README about the breaking change in 2.0

# Improve the default config so it works out of the box for dev

# Adjust timeout and retry settings based on production observations

# Support both YAML and JSON config formats for flexibility

# Add integration test that covers the full flow from request to response

# Fix the ordering of middleware so auth runs before the handler

# Simplify the dependency injection so it's easier to mock in tests

# Implement retry logic for the API client when the remote returns 5xx

# Simplify the config merge logic so overrides are predictable

# Support loading config from multiple files with later overriding earlier

# Update dependencies and resolve compatibility warning from pytest

# Simplify the CLI by merging the two similar subcommands into one

# Correct the formula used for calculating the backoff delay

# Adjust the queue size to prevent drops under burst traffic

# Update documentation to reflect the new API and usage examples

# Implement a small in-memory cache for the config to avoid re-reading

# Support environment-specific overrides via separate config files

# Support both YAML and JSON config formats for flexibility

# Support config reload without restart via SIGHUP or file watch
