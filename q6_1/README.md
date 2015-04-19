#How many hours do drivers often work each day/week? Are there outliers?`
<b>Phase1: </b>use hadoop to generate in-car hours per day per driver.
<p>!! datetime is local datetime (with day-light saving).compute the dropoff_datetime by adding pickup_datetime to trip_time_in_secs
<b>Phase2: </b>use hadoop to generate count of different in-car hour.
<b>Phase3: </b>use pandas to generate hist, plan to replace with D3.

<b>Note: </b>Definition of "How many hours do drivers often work each day/week?" is ill-defined. It could be either from first pickup to last dropoff or total trip_time_in_secs. We can do both
