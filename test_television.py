import pytest
from television import Television


class TestTelevision:
    def tv(self):
        return Television()
    def test_init(self):
        return

    def test_power(self):

        assert False

    def test_mute(self):
        assert False

    def test_channel_up(self):
        assert False

    def test_channel_down(self):
        assert False

    def test_volume_up(self):
        assert False

    def test_volume_down(self):
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0.'
