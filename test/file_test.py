import libs.util.file as file;

test_dir = r'test/test';
file.make_dir(test_dir);
print(file.list_dir('./'));
file.rm(r'test');
print(file.list_dir('./'));