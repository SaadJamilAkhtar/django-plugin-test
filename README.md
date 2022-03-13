# Plugin Enabled Django Architecture
The application is aimed to create a plugin enabled architecture in django framework  

# Test 1 (Success)
First successful plugin integration test

## Work Flow:

1. index(view) calls method load_plugin from settings.py
2. load_plugin() takes plugin name as argument
3. load_plugin add Django app (Plugin) to INSTALLED_APPS list and launch a plugin_loaded signal
4. plugin_loaded signal is received by urls.py and urls file of loaded plugin is added to main urls


# Test 2 (Success)
Adding plugins placed within a python package

# Test 3 (Success)
Uploading plugins (zipped) to required directory

# Test 4 (Success)
Unzip installed plugins to required directory

# Test 5 (Pending... [Status failure])
add plugin code to application

## Test 5 update ( [status success])
Added code dynamically to application through plugins

## Test 6
mounting plugin on server startup complete

## Test 7 (Pending... [Status failure])
mounting and unmounting plugin

## Test 7 ([Status Pass])
mounting and unmounting plugin

## Test 8 
add plugin templates to application

## Test 9 
add config file in plugins
___
` In Progress `

