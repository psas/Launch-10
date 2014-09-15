# ARTS 2 Telemetry

The [ARTS 2](http://lokiresearch.com/arts.asp) flight computer is a small,
comercial off the shelf flight computer that records vertical acceleration
and barometric pressure and uses the data to fire the parachute deployment
charges.

This directory has data from this flight:

 - `PSAS_Launch_2013-06-30.odf`: Raw binary file format from the ARTS board
 - `PSAS_Launch_2013-06-30_raw_data.csv`: csv of raw data (ADC values)
 - `PSAS_Launch_2013-06-30_interpertated_data.csv`: csv of flight data converted using ARTS software into units

## Interpertated Data

The format for the `PSAS_Launch_2013-06-30_interpertated_data.csv`:

 - column, value
 - 0, Time from launch in seconds
 - 1, Acceleration in g
 - 2, Velocity in feet per second
 - 3, Altitude in feet (integrated from accelerometer)
 - 4, Altitude in feet (from pressure data)
