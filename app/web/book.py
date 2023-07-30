from flask import jsonify

from app.web import web
from app.web.helper import is_isbn_or_key
from app.web.yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        # result 是is dictionary, but not the json return to frontend
        # 可以使用 json。dumps(result), 200,{'content-type':'application/  json'}
    return jsonify(result)
