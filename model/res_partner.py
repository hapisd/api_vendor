from odoo import api, fields, models

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()


class Partner(models.Model):
    _inherit = 'res.partner'

    # RATE LIMIT
    def check_rate_limit(self, ip):
        limit_key = f'ratelimit:{ip}'
        count = cache.get(limit_key)
        if count and count > 1:
            raise Exception('Rate limit exceeded. Try again later.')
        else:
            cache.set(limit_key, (count or 0) + 1, timeout=60)

    # SECURITY
    def _auth_api_key(self, api_key):
        if not api_key:
            raise Exception("Authorization header with API key missing")
        user_id = self.env["res.users.apikeys"]._check_credentials(
            scope="rpc", key=api_key
        )
        if not user_id:
            raise Exception("API key invalid")
        return user_id
