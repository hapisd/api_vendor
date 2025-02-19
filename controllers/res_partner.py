import json
import logging
from xmlrpc import client

from odoo import http, SUPERUSER_ID, models, fields
from odoo.http import Response, request
from odoo.tools import config, date_utils

_logger = logging.getLogger(__name__)


class ResPartner(http.Controller):
    model_name = 'res.partner'

    # CREATE
    @http.route('/vendor', auth='public', type='json', methods=['POST'], csrf=False)
    def create(self, **kwargs):
        try:
            # RATE LIMIT
            api_key = request.httprequest.headers.get("Authorization")
            request.uid = request.env[self.model_name]._auth_api_key(api_key)

            # SECURITY
            user_ip = request.httprequest.remote_addr
            request.env[self.model_name].check_rate_limit(user_ip)

            # DATA
            data = {
                'name': kwargs.get('name'),
                'street': kwargs.get('street'),
                'city': kwargs.get('city'),
                'zip': kwargs.get('zip'),
                'phone': kwargs.get('phone'),
                'mobile': kwargs.get('mobile'),
                'email': kwargs.get('email'),
                'company_type': 'company',
                'supplier_rank': 1,
            }
            resource = request.env[self.model_name].sudo().create(data)
            return {'status': 'success', 'id': resource.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    # READ
    @http.route('/vendor/<int:vendor_id>', auth='public', type='http', methods=['GET'], csrf=False)
    def get(self, vendor_id, **kwargs):
        try:
            # RATE LIMIT
            api_key = request.httprequest.headers.get("Authorization")
            request.uid = request.env[self.model_name]._auth_api_key(api_key)

            # SECURITY
            user_ip = request.httprequest.remote_addr
            request.env[self.model_name].check_rate_limit(user_ip)
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

        vendor = request.env[self.model_name].sudo().browse(vendor_id)
        headers = {'content-type': 'application/json'}
        if vendor.exists():
            data = {
                'id': vendor.id,
                'name': vendor.name,
                'street': vendor.street,
                'city': vendor.city,
                'zip': vendor.zip,
                'phone': vendor.phone,
                'mobile': vendor.mobile,
                'email': vendor.email
            }
            return Response(json.dumps(data, default=date_utils.json_default), headers=headers)
        else:
            return Response(json.dumps({'status': 'error', 'message': 'Vendor not found'}, default=date_utils.json_default), headers=headers)

    @http.route('/vendors', auth='public', type='http', methods=['GET'], csrf=False)
    def get_all(self, **kwargs):
        try:
            # RATE LIMIT
            api_key = request.httprequest.headers.get("Authorization")
            request.uid = request.env[self.model_name]._auth_api_key(api_key)

            # SECURITY
            user_ip = request.httprequest.remote_addr
            request.env[self.model_name].check_rate_limit(user_ip)
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

        vendors = request.env[self.model_name].sudo().search([])
        headers = {'content-type': 'application/json'}
        data = [{
                'id': vendor.id,
                'name': vendor.name,
                'street': vendor.street,
                'city': vendor.city,
                'zip': vendor.zip,
                'phone': vendor.phone,
                'mobile': vendor.mobile,
                'email': vendor.email
        } for vendor in vendors]
        return Response(json.dumps(data, default=date_utils.json_default), headers=headers)

    # UPDATE
    @http.route('/vendor/<int:vendor_id>', auth='public', type='json', methods=['PUT'], csrf=False)
    def write(self, vendor_id, **kwargs):
        try:
            # RATE LIMIT
            api_key = request.httprequest.headers.get("Authorization")
            request.uid = request.env[self.model_name]._auth_api_key(api_key)

            # SECURITY
            user_ip = request.httprequest.remote_addr
            request.env[self.model_name].check_rate_limit(user_ip)
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

        vendor = request.env[self.model_name].sudo().browse(vendor_id)
        if vendor.exists():
            vendor.write({
                'name': kwargs.get('name', vendor.name),
                'street': kwargs.get('street', vendor.street),
                'city': kwargs.get('city', vendor.city),
                'zip': kwargs.get('zip', vendor.zip),
                'phone': kwargs.get('phone', vendor.phone),
                'mobile': kwargs.get('mobile', vendor.mobile),
                'email': kwargs.get('email', vendor.email),
            })
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Vendor not found'}

    # DELETE
    @http.route('/vendor/<int:vendor_id>', auth='public', type='json', methods=['DELETE'], csrf=False)
    def unlink(self, vendor_id, **kwargs):
        try:
            # RATE LIMIT
            api_key = request.httprequest.headers.get("Authorization")
            request.uid = request.env[self.model_name]._auth_api_key(api_key)

            # SECURITY
            user_ip = request.httprequest.remote_addr
            request.env[self.model_name].check_rate_limit(user_ip)
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

        vendor = request.env[self.model_name].sudo().browse(vendor_id)
        if vendor.exists():
            vendor.unlink()
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Vendor not found'}

