Hello,

This is a django boiler plate code with the following configuration:

1] the base projet is named as "base".
2] find the dependencies in requirements.txt
3] djangorestframework is listed in the settings.
4] folders for media and static are created.
5] STATIC ROOT is pointing to static.
6] STATICFILES_DIRS is set to mystatic.
7] For development, store all your assets in the given folder under mystatic.
8] You will later collectstatic at deployment and change it to the public html directory of your server.
9] The URL configuration is done for static files and media
10] Linter flake8 is included in requirements, please configure the vscode settings.json to say the following
11] The Pillow Library is also added to requirements. 
I assume you guys are familliar with virtualenviornments,
I like to have my env in project folder and have a src folder as BASE_DIR for django project
I am not pushing my enviornment to git so just make one and you will be good to go :)
however, this is personal and feel free to customize it.

#settings.json for vscode
{
    "python.pythonPath": "bin/python",
    "editor.tabSize": 4,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false
}


Cheers :D and happy coding to you all 