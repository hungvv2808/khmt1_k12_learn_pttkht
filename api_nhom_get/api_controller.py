
from odoo import http, _
from odoo.http import request
from odoo.addons.lc_rest_api.controllers.controllers import validate_token, generate_response, getRequestIP, serialization_data, toUserDatetime, _args, permission_check

class ApiGetData(http.Controller):
    #Lay danh muc san pham
    @validate_token
    @http.route(['/api/get/category/', '/api/get/category/<product_category>'], methods=['GET'], type='http', auth='none', csrf=False)
    def model_product_category_config(self, access_token, product_category=None, **kw):
        if not permission_check('product.category', 'read'):
            return generate_response(data={
                'success': False,
                'msg': "Create permission denied"
            })
        if not product_category:
            try:
                _domain, _fields, _offset, _limit, _order = _args(kw)
                data = request.env['product.category'].search_read(fields=['id', 'name', 'parent_id'], offset=_offset, limit=_limit, order=_order)
                code = request.env['product.template'].search_read(fields=['default_code'], offset=_offset, limit=_limit, order=_order)
                
                return generate_response(data={
                    'success': True,
                    'msg': "success",
                    'data': serialization_data(data),
                    'code': serialization_data(code),
                    'data_count': len(data),
                    'code_count': len(code),
                })
            except Exception as e:
                return generate_response(data={
                    'success': False,
                    'msg': "{}".format(e)
                })
        else:
            try:
                product_category = int(product_category)
                data = request.env['product.category'].search_read(domain=[('id', '=', product_category)])
                return generate_response(data={
                    'success': True,
                    'msg': "success",
                    'data': serialization_data(data, restrict=['customer_facing_display_html', 'session_ids'])
                })
            except Exception as e:
                return generate_response(data={
                    'success': False,
                    'msg': "{}".format(e)
                })
    #Lay danh sach tin tuc
    @validate_token
    @http.route(['/api/get/blog/', '/api/get/blog/<blog_post>'], methods=['GET'], type='http', auth='none', csrf=False)
    def model_blog_post_config(self, access_token, blog_post=None, **kw):
        if not permission_check('blog.post', 'read'):
            return generate_response(data={
                'success': False,
                'msg': "Create permission denied"
            })
        if not blog_post:
            try:
                _domain, _fields, _offset, _limit, _order = _args(kw)
                data = request.env['blog.post'].search_read(fields=['id', 'name', 'subtitle'], offset=_offset, limit=_limit, order=_order)
                return generate_response(data={
                    'success': True,
                    'msg': "success",
                    'data': serialization_data(data),
                    'data_count': len(data)
                })
            except Exception as e:
                return generate_response(data={
                    'success': False,
                    'msg': "{}".format(e)
                })
        else:
            try:
                blog_post = int(blog_post)
                data = request.env['blog.post'].search_read(domain=[('id', '=', blog_post)])
                return generate_response(data={
                    'success': True,
                    'msg': "success",
                    'data': serialization_data(data, restrict=['customer_facing_display_html', 'session_ids'])
                })
            except Exception as e:
                return generate_response(data={
                    'success': False,
                    'msg': "{}".format(e)
                })