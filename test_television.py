import pytest
from television import *
# ignore unresolved reference
tv = Television()


def test_init():
    assert tv._Television__status is False
    assert tv._Television__muted is False
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL


def test_power():
    tv.power()
    assert tv._Television__status is True
    tv.power()
    assert tv._Television__status is False


def test_mute():
    tv.mute()
    assert tv._Television__muted is False
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._Television__muted is True
    tv.mute()
    assert tv._Television__muted is False
    tv.volume_down()
    tv.power()
    tv.mute()
    assert tv._Television__muted is False
    tv.power()


def test_channel_up():
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    assert tv._Television__channel == 2
    tv.channel_up()
    assert tv._Television__channel == 3
    tv.channel_up()
    assert tv._Television__channel == 0
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 0
    tv.power()


def test_channel_down():
    tv.channel_down()
    assert tv._Television__channel == 3
    tv.channel_down()
    assert tv._Television__channel == 2
    tv.channel_down()
    assert tv._Television__channel == 1
    tv.channel_down()
    assert tv._Television__channel == 0
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == 0
    tv.power()


def test_volume_up():
    assert tv._Television__volume == 0
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.mute()
    tv.volume_up()
    assert tv._Television__muted is False
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == 2


def test_volume_down():
    tv.volume_down()
    assert tv._Television__volume == 1
    tv.mute()
    tv.volume_down()
    assert tv._Television__muted is False
    assert tv._Television__volume == 0
    tv.volume_down()
    assert tv._Television__volume == 0
