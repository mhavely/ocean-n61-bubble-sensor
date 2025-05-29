# Bubble Sensor User Manual

To turn on the bubble sensor, connect your microcontroller to Thonny via WebREPL. Once connected, use the “sample” function (defined in Python code file “main.py”, see public GitHub repository 
“ocean-n61-bubble-sensor” for more information) by defining how many reps you want to take. For a five-minute deployment, 
you will want 100 samples (plus at least 20 buffer samples before and after deployment to give you 1 minute to deploy and retrieve).
To retrieve data from sensor, download "test_data2.csv" from microcontroller once sample function has stopped (note:
sample function may also be manually stopped by hitting ctrl + c at any time, but should only be done when the microcontroller
light is visibly off (meaning no sampling is occuring)).
