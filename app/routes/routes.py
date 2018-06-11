from flask import Blueprint,jsonify,request
from app import db
from app.models.post import PostModel
from sqlalchemy.exc import IntegrityError


api = Blueprint('api', 'api', url_prefix='/api')

@api.route('', methods=['GET', 'POST'])
def echo():
    d = {
        "echo":"hello sendbird"
    }
    
    return jsonify(d)
    

@api.route('/posts', methods=['POST'])
def create_post():

    json_data = request.get_json(force=True)

    # check validation

    try:
        post = PostModel(title=json_data["title"])
        db.session.add(post)
        db.session.commit()

        ret_data = {
            "title": json_data["title"]
        }

        return jsonify(ret_data) 

    except IntegrityError as e:
        print(e)


@api.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = []
        posts_query = PostModel.query

        for post in posts_query:
            posts.append(serialize_post(post))

        return jsonify(posts) 

    except IntegrityError as e:
        print(e)


@api.route('/posts/<id>', methods=['POST'])
def get_post(id):
    # validate id
    post = PostModel.query.filter(PostModel.id == id).first()
    return jsonify(serialize_post(post)) 


@api.route('/posts', methods=['PATCH'])
def update_post():
    json_data = request.get_json(force=True)

    # check validation

    try:
        post = PostModel.query.filter(PostModel.id == json_data["id"]).first()
        post.title = json_data["title"]
        
        db.session.commit()

        post = PostModel.query.filter(PostModel.id == json_data["id"]).first()
        return jsonify(serialize_post(post)) 

    except IntegrityError as e:
        print(e)



@api.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
    # check validation

    try:
       # validate id
        post = PostModel.query.filter(PostModel.id == id).first()

        db.session.delete(post)
        db.session.commit()

        return jsonify(serialize_post(post)) 

    except IntegrityError as e:
        print(e)

def serialize_post(post):
    return {
        'id': post.id,
        'title': post.title,
        'created_at': post.created_at.isoformat()
    }

