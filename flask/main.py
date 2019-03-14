from flask import Flask, request, Response
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['flask_service']['collection_name']


def check_exist(link):
    """
    this function check if record is exist in db or not for cache staff

    IMPORTANT:
        This method is just an simple example of using mongodb in flask and not for your'e production project

    :param link: the url of request video, example

    :return:
        - dictionary of video info if found in db
        - False if not exist in db
    """
    query = db.find_one({'link': link})
    if query:
        video = query
        del video['_id']
    else:

        video = {
            'label': 'label'
        }

        db.insert_one(video)
        del video['_id']
    return video


@app.route("/")
def hello():

    return Response('', headers={'Content-Type': 'application/json'}, status=200)


app.run(port=5001)
