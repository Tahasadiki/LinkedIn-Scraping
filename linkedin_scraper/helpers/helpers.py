def save_to_file(data,file_path):
    try:
        with open(file_path,"w") as f:
            for item in data[:-1]:
                f.write(f"{item}\n")
        return True
    except Exception as e:
        print(f"[ERROR WRITING FILE] {e}")
        return False

def read_file(file_path):
    try:
        with open(file_path,"r") as f:
            proxies= [line.rstrip('\n') for line in f if line!='\n'] 
    except Exception as e:
        print(f"[ERROR WRITING FILE] {e}")
        proxies=None
    return proxies

class GoogleQuery:
    def __init__(self,q='',num=None,arguments=None):
        self.q = q
        self.num = num
        self.arguments = arguments