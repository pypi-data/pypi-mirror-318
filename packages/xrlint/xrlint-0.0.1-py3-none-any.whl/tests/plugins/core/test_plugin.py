from unittest import TestCase

from xrlint.plugins.core import export_plugin


class ExportPluginTest(TestCase):

    def test_configs_complete(self):
        _plugin = export_plugin()
        self.assertEqual(
            {
                "recommended",
            },
            set(_plugin.configs.keys()),
        )

    def test_rules_complete(self):
        _plugin = export_plugin()
        self.assertEqual(
            {
                "coords-for-dims",
                "dataset-title-attr",
                "no-empty-attrs",
                "var-units-attr",
            },
            set(_plugin.rules.keys()),
        )
