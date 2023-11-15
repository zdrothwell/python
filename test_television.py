import pytest
from television import Television
# ignore unresolved reference


class TestTelevision:

    @pytest.fixture
    def tv(self):
        return Television()

    def test_init(self, tv):
        assert tv._Television__status is False
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL
        assert tv._Television__stored == 0

    def test_power(self, tv):
        tv.power()
        assert tv._Television__status is True

    def test_mute(self, tv):
        tv.mute()
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME

    def test_channel_up(self, tv):
        tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self, tv):
        tv.channel_down()
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_volume_up(self, tv):
        tv.volume_up()
        assert tv._Television__volume == Television.MIN_VOLUME

        tv.mute()
        tv.volume_up()
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME

    def test_volume_down(self, tv):
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME

        tv.mute()
        tv.volume_down()
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME

    def test_str(self, tv):
        assert str(tv) == 'Power = False, Channel = 0, Volume = 0.'
