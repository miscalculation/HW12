import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = str(now)
   
    if not entries:
        next_id = 0
    else:
        seq = [element["id"] for element in entries]
        next_id = int(max(seq))
        next_id += 1
   
    entry = {"id": str(next_id), "author": name, "text": text, "timestamp": time_string}
    
    entries.insert(0, entry) 
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
    
    return None

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id

    new_entries = [element for element in entries if element.get('id', '') != GUESTBOOK_ENTRIES_FILE(id)]
    entries = new_entries
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
    
    return None
   

def post_edit(id, message):
    global entries, GUESTBOOK_ENTRIES_FILE

    modify_entries = [element for element in entries if element.get('id', '') == str(id)]
    
    for modify in modify_entries:
        author = modify["author"]
        timestamp = modify["timestamp"]
    
    new_entries = [element for element in entries if element.get('id', '') != str(id)]
    entries = new_entries
    entry = {"id": str(id), "author": author, "text": message, "timestamp": timestamp}
    entries.insert(0, entry) 
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
    


        
    return None


# init()
# get_entries()
# add_entry("ro", "hi hi")