class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__stored = 0

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status is True:
            if self.__muted is False:
                self.__muted = True
                self.__stored = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        if self.__status is True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status is True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__stored
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1
            else:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__stored
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1
            else:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
