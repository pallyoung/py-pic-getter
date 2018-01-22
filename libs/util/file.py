import os;


def exists(path):
    return os.path.exists(path);

def is_file(path):
    return os.path.isfile(path);

def is_dir(path):
    return os.path.isdir(path);

def list_dir(path):
    return os.listdir(path);

def remove(path):
    return os.remove(path);
def remove_dir(path):
    os.rmdir(path);

def rm(path):
    path=os.path.relpath(path);
    if(not exists(path)):
        return;
    if(is_file(path)):
        remove(path);
    else:
        dirs = list_dir(path);
        for dir in dirs:
            rm(os.path.relpath(r'%s%s%s' % (path,os.path.sep,dir)));
        remove_dir(path);


def make_dir(path):
        path = os.path.realpath(path);
        path_list = path.split(os.path.sep);
        cur_path = '';
        if(exists(path)):
            rm(path);
        for sub_path in path_list:
            cur_path = os.path.join(r'%s%s%s' % (cur_path,os.path.sep,sub_path));
            if(not exists(cur_path)):
                os.mkdir(cur_path);
def open_file(path,mode='w', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    dir = os.path.dirname(path);
    if(not exists(dir)):
        make_dir(dir);
    return open(path,mode,encoding=encoding, errors=errors, newline=newline, closefd=closefd);

def recur(path,callback):
    if(exists(path)):
        callback(path);
        if(is_dir(path)):
            dir_path = list_dir(path);
            for sub_path in dir_path:
                recur(os.path.join('%s%s' % (path, sub_path)),callback);








