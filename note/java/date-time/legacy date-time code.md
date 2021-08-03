# legacy date-time code
java.util.Date, java.util.Calendar, and java.util.TimeZone and subclass java.util.GregorianCalendar
### drawbacks:
* The Calendar class was not type safe.
* Because the classes were mutable, they could not be used in multithreaded applications.
* Bugs in application code were common due to the unusual numbering of months and the lack of type safety.
 
 
### Interoperability with Legacy Code (add by 1.8)
* Calendar.toInstant() converts the Calendar object to an Instant.
* GregorianCalendar.toZonedDateTime() converts a GregorianCalendar instance to a ZonedDateTime.
* GregorianCalendar.from(ZonedDateTime) creates a GregorianCalendar object using the default locale from a ZonedDateTime instance.
* Date.from(Instant) creates a Date object from an Instant.
* Date.toInstant() converts a Date object to an Instant.
* TimeZone.toZoneId() converts a TimeZone object to a ZoneId.


### Mapping java.util Date and Time Functionality to java.time
java.util Functionality | java.time Functionality
:--- | :--- 
java.util.Date | java.time.Instant
java.util.GregorianCalendar | java.time.ZonedDateTime
java.util.TimeZone | java.time.ZoneId or java.time.ZoneOffset
GregorianCalendar with the date set to 1970-01-01 | java.time.LocalTime
GregorianCalendar with time set to 00:00. | java.time.LocalDate

