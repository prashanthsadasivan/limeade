import tornado.web
from db import *
import json
from bson import json_util

class VideoSearchHandler(tornado.web.RequestHandler):
    def get(self):
        database = db_client()
        query = self.get_argument("query", default=None, strip=False)


        import re
        if query is not None:
            regxp = re.compile(query, re.IGNORECASE)
            videos = database.videos.find({ "title" : regxp }).sort( [[ '_id', -1]] )

      
      
        return_videos = []
        for video in videos:
            return_videos.append(video)


        self.write(json.dumps(return_videos, default=json_util.default))

class VideoListHandler(tornado.web.RequestHandler):
    def get(self):
        database = db_client()
        filter = self.get_argument("filter", default=None, strip=False)
        if filter == "new":
            videos = database.videos.find().sort( [['_id', -1]] )
        elif filter == "trending":
            videos = database.videos.find().sort( [['blog_hits', -1]])
    
        return_videos = []
        for video in videos:
            return_videos.append(video)


        self.write(json.dumps(return_videos, default=json_util.default))
