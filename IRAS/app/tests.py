from django.test import TestCase
# Create your tests here.
import tempfile
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_path = temp_file.name
print("临时文件路径:", temp_file_path)
temp_file.close()
import os
os.remove(temp_file_path)