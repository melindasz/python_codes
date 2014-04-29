Learn to Program: The Fundamentals // Assignment 1

A1 Problem Domain: Coordinated Universal Time

The problem domain for this assignment involves time zones, and in particular Coordinated Universal Time (UTC), which is "the primary time standard by which the world regulates clocks and time" [Wikipedia]. As you know, there are many different time zones in the world. Wikipedia has a nice map of the time zones.

As of this writing, there are 40 time zones. One of them, UTC+00:00, is considered to be in the "middle" of the other time zones. All time zones have names, such as UTC+02:00, that indicate the number of hours and minutes they are away from UTC+00:00. For example, the Philippines are in time zone UTC+08:00 because clocks there are set 8 hours later than in time zone UTC+00:00. If it's noon in time zone UTC+00:00, it's 20:00 in time zone UTC+08:00.

Representing hours, minutes, and seconds using a float

In this assignment, we are sometimes going to represent hours and minutes and seconds together as a float. 1 hour will be represented as 1.0, 1 hour and 30 minutes as 1.5, and so on.
======================================================================================================

Function descriptions:

seconds_difference:
(number, number) -> number	 The parameters are times in seconds. Return how many seconds later the second time is than the first. Please note: in a1.py, we have provided the completed docstring for this function, including example function calls with the expected return values.

hours_difference:
(number, number) -> float	 The parameters are times in seconds. Return how many hours later the second time is than the first. 

to_float_hours:
(int, int, int) -> float	 The first parameter is a number of hours, the second parameter is a time in minutes (between 0 and 59, inclusive), and the third parameter is a time in seconds (between 0 and 59, inclusive). Return the combined time as a float value. 

get_hours:
(int) -> int	 The parameter is a number of seconds since midnight. Return the number of hours that have elapsed since midnight, as seen on a 24-hour clock. 

get_minutes:
(int) -> int	 The parameter is a number of seconds since midnight. Return the number of minutes that have elapsed since midnight as seen on a clock. (This means that the return value should be in the range 0 to 59, inclusive.)

get_seconds:
(int) -> int	 The parameter is a number of seconds since midnight. Return the number of seconds that have elapsed since midnight as seen on a clock. (This means that the return value should be in the range 0 to 59, inclusive.)

time_to_utc:
(number, float) -> float	 The first parameter is a UTC offset specifying a time zone and the second parameter is a time in that time zone. Return the equivalent UTC+0 time. 

time_from_utc:
(number, float) -> float	 The first parameter is a UTC offset specifying a time zone and the second parameter is a time in time zone UTC+0. Return the equivalent time in the time zone specified by utc_offset. 

======================================================================================================================
Fun stuff: a Graphical User Interface!

The course provided a graphical user interface (GUI) that shows four clocks and allows you to choose time zones to display. 



