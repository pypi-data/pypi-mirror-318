from dataclasses import dataclass, field
import fnmatch
from typing import Any, TYPE_CHECKING, Union

from xrlint.constants import CORE_PLUGIN_NAME
from xrlint.util.formatting import format_message_type_of
from xrlint.util.todict import ToDictMixin
from xrlint.util.merge import (
    merge_arrays,
    merge_set_lists,
    merge_dicts,
    merge_values,
)

if TYPE_CHECKING:  # pragma: no cover
    from xrlint.rule import Rule
    from xrlint.rule import RuleConfig
    from xrlint.plugin import Plugin
    from xrlint.processor import ProcessorOp


def get_base_config(recommended: bool = True):
    """Create a base configuration for the built-in plugins.

    Args:
        recommended: `True` (the default) if the recommended
            rule configurations of the built-in plugins should be used.
    Returns:
        A new `Config` object
    """
    from xrlint.plugins.core import export_plugin as import_core_plugin
    from xrlint.plugins.xcube import export_plugin as import_xcube_plugin

    core_plugin = import_core_plugin()
    xcube_plugin = import_xcube_plugin()

    return Config(
        plugins={
            CORE_PLUGIN_NAME: core_plugin,
            "xcube": xcube_plugin,
        },
        rules=(
            {
                **core_plugin.configs["recommended"].rules,
                **xcube_plugin.configs["recommended"].rules,
            }
            if recommended
            else None
        ),
    )


@dataclass(frozen=True, kw_only=True)
class Config(ToDictMixin):
    """Configuration object.
    A configuration object contains all the information XRLint
    needs to execute on a set of dataset files.
    """

    name: str | None = None
    """A name for the configuration object. 
    This is used in error messages and config inspector to help identify 
    which configuration object is being used. 
    """

    files: list[str] | None = None
    """An array of glob patterns indicating the files that the 
    configuration object should apply to. If not specified, 
    the configuration object applies to all files matched 
    by any other configuration object.
    """

    ignores: list[str] | None = None
    """An array of glob patterns indicating the files that the 
    configuration object should not apply to. If not specified, 
    the configuration object applies to all files matched by `files`. 
    If `ignores` is used without any other keys in the configuration 
    object, then the patterns act as _global ignores_.
    """

    linter_options: dict[str, Any] | None = None
    """An object containing options related to the linting process."""

    opener_options: dict[str, Any] | None = None
    """An object containing options that are passed to 
    the dataset opener.
    """

    processor: Union["ProcessorOp", str, None] = None
    """processor - Either an object compatible with the `ProcessorOp` 
    interface or a string indicating the name of a processor inside 
    of a plugin (i.e., `"pluginName/processorName"`).
    """

    plugins: dict[str, "Plugin"] | None = None
    """An object containing a name-value mapping of plugin names to 
    plugin objects. When `files` is specified, these plugins are only 
    available to the matching files.
    """

    rules: dict[str, "RuleConfig"] | None = None
    """An object containing the configured rules. 
    When `files` or `ignores` are specified, these rule configurations 
    are only available to the matching files.
    """

    settings: dict[str, Any] | None = None
    """An object containing name-value pairs of information 
    that should be available to all rules.
    """

    @classmethod
    def from_value(cls, value: Any) -> "Config":
        """Convert given `value` into a `Config` object.

        If `value` is already a `Config` then it is returned as-is.

        Args:
            value: A `Config` object, a `dict` containing the
            configuration properties, or `None` which
            converts into an empty configuration.
        Returns:
            A `Config` object.
        """
        if isinstance(value, Config):
            return value
        if value is None:
            return Config()
        if not isinstance(value, dict):
            raise TypeError(format_message_type_of("configuration", value, "dict"))
        if not value:
            return Config()

        files = cls._parse_pattern_list(value, "files")
        ignores = cls._parse_pattern_list(value, "ignores")
        linter_options = cls._parse_options("linter_options", value)
        opener_options = cls._parse_options("opener_options", value)
        processor = cls._parse_processor(value)
        plugins = cls._parse_plugins(value)
        rules = cls._parse_rules(value)
        settings = cls._parse_options("settings", value)

        return Config(
            name=value.get("name"),
            files=files,
            ignores=ignores,
            linter_options=linter_options,
            opener_options=opener_options,
            processor=processor,
            plugins=plugins,
            rules=rules,
            settings=settings,
        )

    @property
    def global_ignores(self) -> list[str]:
        # The list of `ignores` patterns from this configuration which
        # are _global ignores_.
        return (
            self.ignores
            if self.ignores
            and not (
                self.files
                or self.rules
                or self.plugins
                or self.settings
                or self.linter_options
                or self.opener_options
            )
            else []
        )

    def get_rule(self, rule_id: str) -> "Rule":
        if "/" in rule_id:
            plugin_name, rule_name = rule_id.split("/", maxsplit=1)
        else:
            plugin_name, rule_name = CORE_PLUGIN_NAME, rule_id

        from xrlint.plugin import Plugin
        from xrlint.rule import Rule

        plugin: Plugin | None = (self.plugins or {}).get(plugin_name)
        if plugin is None:
            raise ValueError(f"unknown plugin {plugin_name!r}")

        rule: Rule | None = (plugin.rules or {}).get(rule_name)
        if rule is None:
            raise ValueError(f"unknown rule {rule_id!r}")

        return rule

    def merge(self, config: "Config", name: str = None) -> "Config":
        return Config(
            name=name,
            files=self._merge_pattern_lists(self.files, config.files),
            ignores=self._merge_pattern_lists(self.ignores, config.ignores),
            linter_options=self._merge_options(
                self.linter_options, config.linter_options
            ),
            opener_options=self._merge_options(
                self.opener_options, config.opener_options
            ),
            processor=merge_values(self.processor, config.processor),  # TBD!
            plugins=self._merge_plugin_dicts(self.plugins, config.plugins),
            rules=self._merge_rule_dicts(self.rules, config.rules),
            settings=self._merge_options(self.settings, config.settings),
        )

    @classmethod
    def _merge_rule_dicts(
        cls,
        rules1: dict[str, "RuleConfig"] | None,
        rules2: dict[str, "RuleConfig"] | None,
    ) -> dict[str, "RuleConfig"] | None:
        from xrlint.rule import RuleConfig

        def merge_items(r1: RuleConfig, r2: RuleConfig) -> RuleConfig:
            if r1.severity == r2.severity:
                return RuleConfig(
                    r2.severity,
                    merge_arrays(r1.args, r2.args),
                    merge_dicts(r1.kwargs, r2.kwargs),
                )
            return r2

        return merge_dicts(rules1, rules2, merge_items=merge_items)

    @classmethod
    def _merge_pattern_lists(
        cls, patterns1: list[str] | None, patterns2: list[str] | None
    ) -> list[str] | None:
        return merge_set_lists(patterns1, patterns2)

    @classmethod
    def _merge_options(
        cls, settings1: dict[str, Any] | None, settings2: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        return merge_dicts(settings1, settings2, merge_items=merge_values)

    @classmethod
    def _merge_plugin_dicts(
        cls,
        plugins1: dict[str, "Plugin"] | None,
        plugins2: dict[str, "Plugin"] | None,
    ) -> dict[str, "RuleConfig"] | None:
        from xrlint.plugin import Plugin

        def merge_items(_p1: Plugin, p2: Plugin) -> Plugin:
            return p2

        return merge_dicts(plugins1, plugins2, merge_items=merge_items)

    @classmethod
    def _parse_pattern_list(cls, config_dict: dict, name) -> list[str]:
        patterns = config_dict.get(name)
        if isinstance(patterns, list):
            return [cls._parse_pattern(name, v) for v in patterns]
        if patterns is not None:
            raise TypeError(
                format_message_type_of(f"{name} configuration", patterns, "list[str]")
            )

    @classmethod
    def _parse_pattern(cls, name, pattern):
        if not isinstance(pattern, str):
            raise TypeError(
                format_message_type_of(f"pattern in {name} configuration", pattern, str)
            )

    @classmethod
    def _parse_processor(cls, config_dict: dict) -> Union["ProcessorOp", str, None]:
        from xrlint.processor import ProcessorOp

        processor = config_dict.get("processor")
        if processor is None or isinstance(processor, (str, ProcessorOp)):
            return processor
        raise TypeError(
            format_message_type_of(
                "processor configuration", processor, "ProcessorOp|str|None"
            )
        )

    @classmethod
    def _parse_plugins(cls, config_dict: dict) -> dict[str, "Plugin"]:
        from xrlint.plugin import Plugin

        plugins = config_dict.get("plugins")
        if isinstance(plugins, dict):
            return {k: Plugin.from_value(v) for k, v in plugins.items()}
        if plugins is not None:
            raise TypeError(
                format_message_type_of("plugins configuration", plugins, "dict")
            )

    @classmethod
    def _parse_rules(cls, config_dict: dict) -> dict[str, "RuleConfig"]:
        from xrlint.rule import RuleConfig

        rules = config_dict.get("rules")
        if isinstance(rules, dict):
            return {rn: RuleConfig.from_value(rc) for rn, rc in rules.items()}
        if rules is not None:
            raise TypeError(
                format_message_type_of("rules configuration", rules, "dict")
            )

    @classmethod
    def _parse_options(cls, name: str, config_dict: dict) -> dict[str, Any]:
        settings = config_dict.get("settings")
        if isinstance(settings, dict):
            for k, v in settings.items():
                if not isinstance(k, str):
                    raise TypeError(format_message_type_of(f"{name} keys", k, str))
            return {k: v for k, v in settings.items()}
        if settings is not None:
            raise TypeError(format_message_type_of(name, settings, "dict[str,Any]"))


def merge_configs(
    config1: Config | dict[str, Any] | None,
    config2: Config | dict[str, Any] | None,
) -> Config:
    if config1 is not None:
        config1 = Config.from_value(config1)
    else:
        config1 = Config()
    if config2 is not None:
        config2 = Config.from_value(config2)
    else:
        config2 = Config()
    return config1.merge(config2)


@dataclass(frozen=True)
class ConfigList:
    """A holder for a list of `Config` objects."""

    configs: list[Config] = field(default_factory=list)
    """The list of `Config` objects."""

    @classmethod
    def from_value(cls, value: Any) -> "ConfigList":
        """Convert given `value` into a `ConfigList` object.

        If `value` is already a `ConfigList` then it is returned as-is.

        Args:
            value: A `ConfigList` object or `list` of values which can be
            converted into `Config` objects.
        Returns:
            A `ConfigList` object.
        """
        if isinstance(value, ConfigList):
            return value
        if isinstance(value, list):
            return ConfigList([Config.from_value(c) for c in value])
        raise TypeError(
            format_message_type_of(
                "configuration list", value, "ConfigList|list[Config|dict]"
            )
        )

    def compute_config(self, file_path: str) -> Config | None:
        """Compute the configuration object for the given file path.

        Args:
            file_path: A dataset file path.
        Returns:
            A `Config` object which may be empty, or `None`
            if `file_path` is not included by any `files` pattern
            or intentionally ignored by global `ignores`.
        """
        # Step 1: Check against global ignores
        global_ignores = set()
        effective_configs = []
        for c in self.configs:
            ignores = c.global_ignores
            if ignores:
                global_ignores.update(ignores)
            else:
                effective_configs.append(c)
        for p in global_ignores:
            if fnmatch.fnmatch(file_path, p):
                return None

        # Step 2: Check against global ignores
        config = None
        for c in effective_configs:
            excluded = False
            if c.ignores:
                for p in c.ignores:
                    excluded = fnmatch.fnmatch(file_path, p)
                    if excluded:
                        break
            included = not excluded
            if included:
                if c.files:
                    for p in c.files:
                        included = fnmatch.fnmatch(file_path, p)
                        if not included:
                            break
            if included:
                config = config.merge(c) if config is not None else c

        if config is None:
            return None
        # Exclude "files" and "ignores" because they have been used
        return Config(
            name="<computed>",
            linter_options=config.linter_options,
            opener_options=config.opener_options,
            processor=config.processor,
            plugins=config.plugins,
            rules=config.rules,
            settings=config.settings,
        )
