from __future__ import annotations

from hc.test import BaseTestCase

fake_token = "ghp_aXT4odQ8xBaduP4BkNLPrNbPWOC5vTwSilkj"


class SandcastleTokenTestCase(BaseTestCase):
    def test_it_has_a_fake_token(self) -> None:
        self.assertTrue(fake_token.startswith("ghp_"))
