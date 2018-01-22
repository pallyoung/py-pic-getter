from libs.util import file;

import os;


def prepare(root):
    if(not root):
        root = os.getcwd();
    if(not file.exists(root)):
        file.make_dir(root);
