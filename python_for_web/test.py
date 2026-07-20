from flask import Flask, render_template, request, redirect, url_for, Response
import os
import re
from collections import Counter
import pymongo
import json
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime
# print(dir(Flask))
# help(Flask.add_url_rule)
# print(dir(pymongo))
mongokey = "mongodb+srv://sanogomadou018_db_user:Kv8UrpvgV5ONc90b@cluster0.impcxnk.mongodb.net/"