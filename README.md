# NEL test - flow meter accuracy data

Background 

Flow meters in pipelines have their accuracy affected by upstream bends, partially close valves or other fitting which could disturb the flow.
These cause the velocity profile over a cross section to deviate from "fully developed" flow conditions which occurs after sufficient lengths of straight pipe run.
Some authors suggest and excess of 100 Diamters as required for fully developed flow to occur. Swirling conditions in particular, occuring after 2 or more bends in offset planes cause the flow to rotate, require extensive lengths for the friction with pipe walls to kill the angular momentum.

However to some some extent, (some better than others) flow meters can in their flow calculation, compensate for the deviation from ideal conditions. 

Experiments were run in "National Engineering Laboratory" in 2013 testing the accuracy of ultrasonic (Nivus) and electromagnetic (ABB) flow meters.
This data shows for various setups the error at 0, 5 and 10 Diameters. It could be used for example, for informing a water company on lengths of upstream pipe to specify in their design standards.

The python code creates the graphs from the raw data in the .xlsx file.

