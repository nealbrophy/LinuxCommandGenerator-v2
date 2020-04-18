import os
import pymongo
from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get('MONGO_URI')
DBS_NAME = "linuxCmdGen"
COLLECTION_NAME = "distros"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = {
    "distro_name": "debian",
    "distro_logo":"<i class=\"fl-debian sideLogo\" aria-hidden=\"true\"></i>",
    "appImageLauncher":["go to <a href=\"https://github.com/TheAssassin/AppImageLauncher/releases\" target=\"_blank\">https://github.com/TheAssassin/AppImageLauncher/releases</a> and download the appropriate <code>.deb</code> file. Then execute the below in terminal.",
                        "sudo dpkg -i appimagelauncher_*.deb"],
    "atom":["execute the below in terminal (<code>cmd+t</code> or <code>ctrl+alt+t</code> on most distros).",
            "sudo add-apt-repository ppa:webupd8team/atom && \nsudo apt-get update && \nsudo apt-get install -y atom"]
        }

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)