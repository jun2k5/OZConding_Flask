from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operation on boards', url_prefix="/board")


# API List
# /borad/
# 전체 게시글 불러오기 (GET)
# 게시글 작성 (POST)
@board_blp.route('/')
class BoardList(MethodView):



#/borad/<int: board_id>
#하나의 게시글 불러오기 (GET)
#특정 게시글 수정하기 (PUT)
#특정 게시글 삭제하기 (DELETE)








