class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize a Television instance"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the television"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television"""
        if self.__status is True:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by 1.
        This also makes the channel loop back
        to the minimum channel if it goes over"""
        if self.__status is True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by 1.
        This also makes the channel loop back
        to the maximum channel if it goes under"""

        if self.__status is True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by 1.
        If the TV is muted, it unmutes
        then adds to the volume"""
        if self.__status is True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by 1.
        This also unmutes the TV just like
        volume_up and decreases the volume"""
        if self.__status is True:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns a string of the TV's current status"""
        if self.__muted is True:
            return "Power = {}, Channel = {}, Volume = {}".format(self.__status, self.__channel, Television.MIN_VOLUME)
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'
