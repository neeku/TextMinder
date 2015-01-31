
# Root of this REST API and version
# Follow Semantic Versioning 2.0.0 Standard - http://semver.org/
API_ROOT = '/api/0.0.1'

# Cors policy used by all REST APIs
# See: http://en.wikipedia.org/wiki/Cross-origin_resource_sharing
CORS_POLICY = {
    'origins': ('*',),      # Allow from all sites
    'headers': ('Content-Type') ,            # Allowed headers
    'expose_all_headers': True, # FIXME: Set for development only!!!
    'max_age': 42,
    'credentials': True,    # Client needs to send credentials
}
