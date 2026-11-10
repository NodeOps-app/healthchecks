from __future__ import annotations

from hc.test import BaseTestCase


class SandcastleNoopTestCase(BaseTestCase):
    def test_it_adds_numbers(self) -> None:
        self.assertEqual(1 + 1, 2)
