bind = '0.0.0.0:8000'
workers = 3
static_root = 'static/'
static_files = True
forwarded_allow_ips = "*"  # Allow all forwarded IPs
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')