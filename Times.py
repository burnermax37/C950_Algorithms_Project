# Time class
class Time:
    """Tracks deadlines and calculates durations"""

    def __init__(self, hours, minutes):
        self.duration = (hours * 60) + minutes

    def __lt__(self, other):
        """Less than"""
        return self.duration < other.duration

    def __le__(self, other):
        """Less than or equal to"""
        return self.duration <= other.duration

    def __gt__(self, other):
        """Greater than"""
        return self.duration > other.duration

    def __ge__(self, other):
        """Greater than or equal to"""
        return self.duration >= other.duration

    def __eq__(self, other):
        """Equal to"""
        return self.duration == other.duration

    def __ne__(self, other):
        """Not equal to"""
        return self.duration != other.duration

    def __str__(self):
        """To String"""
        if self >= Time(24, 0):
            return "EOD"

        hours = self.duration // 60
        minutes = self.duration % 60
        ampm = "AM"

        if hours >= 12:
            ampm = "PM"
            if hours > 12:
                hours -= 12

        return "{:02d}:{:02d} {}".format(int(hours), int(minutes), ampm)

    def copy(self):
        """Return new time object with same duration as self"""
        out = Time(0, 0)
        out.duration = self.duration
        return out

    # Note that methods of time object class have constant space and time complexity.


def time_string_to_object(time_string):
    """Method converts time as hh:mm am//pm into time as minutes since start of day"""
    # Constant space and time complexity, as input size does not vary.

    # If time string is acronym for 'End of Day', return 24:00
    if time_string == 'EOD':
        return Time(24, 0)
    else:
        # Split off portion of string with hours and minutes
        space_boundary = time_string.find(" ")
        colon_boundary = time_string.find(":")

        # Convert numeric strings to integer values
        hours = int(time_string[0:colon_boundary])
        minutes = int(time_string[colon_boundary + 1: space_boundary])

        if time_string[-2] == 'P':  # If time is PM
            if (hours != 12) or (minutes != 0):  # If not 12:00 PM
                hours += 12
        elif (hours == 12) and (minutes == 0):  # If 12:00 AM
            hours -= 12

        # Return time object using extracted hours and minutes
        return Time(hours, minutes)
