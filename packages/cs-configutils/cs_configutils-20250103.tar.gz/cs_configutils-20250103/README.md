Utility functions and classes for .ini style configuration files.

*Latest release 20250103*:
Import and requirement update for recent changes elsewhere.

## <a name="ConfigSectionWatcher"></a>Class `ConfigSectionWatcher(collections.abc.Mapping)`

A class for monitoring a particular clause in a config file.

*`ConfigSectionWatcher.__init__(self, config, section, defaults=None)`*:
Initialise a `ConfigSectionWatcher` to monitor a particular section
of a config file.
`config`: path of config file or `ConfigWatcher`
`section`: the section to watch
`defaults`: the defaults section to use, default 'DEFAULT'

*`ConfigSectionWatcher.__getitem__(self, key)`*:
#### Mapping methods.

*`ConfigSectionWatcher.as_dict(self)`*:
Return the config section as a `dict`.

*`ConfigSectionWatcher.keys(self)`*:
Return the keys of the config section.

*`ConfigSectionWatcher.path`*:
The pathname of the config file.

## <a name="ConfigWatcher"></a>Class `ConfigWatcher(collections.abc.Mapping)`

A monitor for a windows style `.ini` file.
The current `SafeConfigParser` object is presented as the `.config` property.

*`ConfigWatcher.__getitem__(self, section)`*:
Return the `ConfigSectionWatcher` for the specified section.

*`ConfigWatcher.as_dict(self)`*:
Construct and return a dictionary containing an entry for each section
whose value is a dictionary of section items and values.

*`ConfigWatcher.config`*:
Live configuration.

*`ConfigWatcher.path`*:
The path to the config file.

*`ConfigWatcher.section_keys(self, section)`*:
Return the field names for the specified section.

*`ConfigWatcher.section_value(self, section, key)`*:
Return the value of [section]key.

## <a name="HasConfigIni"></a>Class `HasConfigIni`

Class for objects with a `config.ini` file.
A section of the config is designated "our" configuration
and its fields parsed into a `TagSet`;
in particular the field values use the `TagSet` transcription syntax.

The default implementation is expected to be mixed into a
class with a `.pathto(rpath)` method, such as one which
inherits from `HasFSPath`.

The mixin provides the following attributes:
* `config`: an on demand property which is a `TagSet` made
  from the configuration file section
* `config_ini`: the relative path to the configuration file
* `configpath`: the full pathname of the configuration file
* `config_flush()`: update the configuration file if the tags
  have been modified

*`HasConfigIni.__init__(self, section, config_ini=None)`*:
Initialise the configuration.

*`HasConfigIni.config`*:
The configuration as a `TagSet`.

*`HasConfigIni.config_flush(self)`*:
Save the current configuration to the `config.ini` file if `self.__modified`.

*`HasConfigIni.configpath`*:
The path to the `config.ini` file.

*`HasConfigIni.info_dict(self, d=None)`*:
Return an informational `dict` containing salient information
about this `HasCOnfigIni`, handy for use with `pprint()`.

## <a name="load_config"></a>`load_config(config_path, parser=None)`

Load a configuration from the named `config_path`.

If `parser` is missing or `None`, use `SafeConfigParser` (just
`ConfigParser` in Python 3).
Return the parser.

# Release Log



*Release 20250103*:
Import and requirement update for recent changes elsewhere.

*Release 20220606*:
HasConfigIni: new info_dict() method (name subject to change) to return a descriptive dict, part of a new scheme I'm trying out to report summary data from commands.

*Release 20220430*:
New HasConfigIni mixin for classes keeping some configuration in a .ini config file section.

*Release 20210306*:
Fix imports from collections.abc.

*Release 20190101*:
Internal changes.

*Release 20160828*:
Update metadata with "install_requires" instead of "requires".

*Release 20150118*:
Initial PyPI release.
