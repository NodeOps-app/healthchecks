from __future__ import annotations

from hc.test import BaseTestCase

api_key = "9936bdd4139fb84d534192cbca3c6aa16d84afec"


class SandcastleKeyNoteTestCase(BaseTestCase):
    def test_it_has_a_placeholder_key(self) -> None:
        self.assertEqual(len(api_key), 40)
