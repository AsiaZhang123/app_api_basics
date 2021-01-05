import os

for root,dirs,files in os.walk(".",topdown=False):
    for file in files:
        if file.endswith('.py') and file != '__init__.py':
            exec("import "+root[1:]+"."+file)