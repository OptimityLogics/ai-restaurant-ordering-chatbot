import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / "workflow.json"


class WorkflowExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = WORKFLOW_PATH.read_text(encoding="utf-8")
        cls.workflow = json.loads(cls.raw)
        cls.nodes = cls.workflow.get("nodes", [])
        cls.node_names = {node.get("name") for node in cls.nodes}

    def test_export_is_valid_json(self):
        self.assertIsInstance(self.workflow, dict)

    def test_workflow_has_expected_core_nodes(self):
        expected = {"AI Agent", "WhatsApp Trigger", "get_inventory", "get_faq", "Take-orders"}
        self.assertTrue(expected.issubset(self.node_names))

    def test_node_names_are_present_and_unique(self):
        names = [node.get("name") for node in self.nodes]
        self.assertTrue(all(isinstance(name, str) and name.strip() for name in names))
        self.assertEqual(len(names), len(set(names)))

    def test_node_ids_are_present_and_unique(self):
        ids = [node.get("id") for node in self.nodes]
        self.assertTrue(all(isinstance(node_id, str) and node_id for node_id in ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_connections_reference_known_nodes(self):
        connections = self.workflow.get("connections", {})
        for source, connection_groups in connections.items():
            self.assertIn(source, self.node_names, f"Unknown source node: {source}")
            for groups in connection_groups.values():
                for group in groups:
                    for connection in group:
                        self.assertIn(connection.get("node"), self.node_names)

    def test_no_common_secret_patterns(self):
        patterns = [
            r"AIza[0-9A-Za-z_-]{30,}",
            r"gh[pousr]_[A-Za-z0-9_]{20,}",
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        ]
        for pattern in patterns:
            self.assertIsNone(re.search(pattern, self.raw), f"Possible secret matched: {pattern}")

    def test_workflow_has_connections(self):
        self.assertTrue(self.workflow.get("connections"))


if __name__ == "__main__":
    unittest.main()
