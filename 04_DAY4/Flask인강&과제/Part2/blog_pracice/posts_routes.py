from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route("/", methods=['GET','POST'])
    def posts():
        cursor = mysql.connection.cursor()

        #게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append({
                    'id' : post[0],
                    'title' : post[1],
                    'content' : post[2]
                })

            return jsonify(post_list)
        
        if request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message = "Title or Content cannot be empty")

            sql = "INSERT INTO posts(title, content) VALUES (%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({"msg":"successfully created post data", "title" : title, "content" : content}), 201
        
    
    #특정 게시글 조회

    @posts_blp.route("/<int:post_id>", methods=['GET', 'PUT', 'DELETE'])
    def posts(id):
        cursor = mysql.connection.cursor()
        sql = f"SELETE * FROM posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()
        if not post:
            return (404, "Not found post")
        
        if request.method == "GET":
            return ({
                'id': post[0],
                'title': post[1],
                'content': post[2]
            })

        elif request.method == "PUT":
            # data = request.json
            # title = data['title']
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, "Not found titile, contnet")

            sql = f"UPDATE posts SET title={title}, content={content} WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"msg":"Successfully updated title & content"})
        
        elif request.method == "DELETE":
            sql = f"DELETE FROM posts WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"msg":"Successfully deleted posts"})

    return posts_blp
