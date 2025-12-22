from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

# 엔드포인트 구현...

@blp.route("/")
class BookList(MethodView):

    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books
    
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        new_data["id"] = len(books) + 1
        books.append(new_data)
        return new_data
    
@blp.route("/<int:book_id>")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        return book
    
    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def post(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(new_data)
        return book
    
    @blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        books = [book for book in books if book['id'] != book_id]
        return ''


