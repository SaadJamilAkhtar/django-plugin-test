# Plugin Enabled Django Architecture
The application is aimed to create a plugin enabled architecture in django framework  

# Test 1
First successful plugin integration test

## Work Flow:

1. index(view) calls method load_plugin from settings.py
2. load_plugin() takes plugin name as argument
3. load_plugin add Django app (Plugin) to INSTALLED_APPS list and launch a plugin_loaded signal
4. plugin_loaded signal is received by urls.py and urls file of loaded plugin is added to main urls
=======
` In Progress `

