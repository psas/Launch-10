# Sim Data

How to use the files in this repo.

`LV2.3.ork` is an [OpenRocket](http://openrocket.info/) file.
This was built with version 13.05. It contains all the
information to simulate a launch, like the size and mass of
the rocket.

![Open Rocket preview of LV2.3](https://raw.github.com/psas/flight_data-launch10/master/sim/OpenRocket_preview.png)

Parameters used for prelaunch sim:

 - Mass: 33.742 kg (with motor)
 - CG: 241.3 cm (from nosecone)
 - Length: 3.536 m (_without_ motor overhang)
 - Diameter: 14.0 cm
 - Motor: [Cesaroni N2850](http://www.thrustcurve.org/simfilesearch.jsp?id=1727)

**Expected Altitide: 4.3 km**


### Inertia Calcualtion From SolidWorks:

Principal axes of inertia and principal moments of inertia: ( pounds * square inches )
Taken at the center of mass.

    Ix = (0.00, -0.00,  1.00)   Px =   359.17
    Iy = (0.80, -0.60, -0.00)   Py = 96889.11
    Iz = (0.60,  0.80, -0.00)   Pz = 96889.44


Moments of inertia: ( pounds * square inches )
Taken at the center of mass and aligned with the output coordinate system.

    Lxx = 96889.23  Lxy =    -0.16  Lxz =   3.88
    Lyx =    -0.16  Lyy = 96889.32  Lyz =  -0.61
    Lzx =     3.88  Lzy =    -0.61  Lzz = 359.17


Moments of inertia: ( pounds * square inches )
Taken at the output coordinate system.

    Ixx = 768296.76     Ixy =     -0.16    Ixz = -21.25
    Iyx =     -0.16     Iyy = 768296.85    Iyz = -37.02
    Izx =    -21.25     Izy =    -37.02    Izz = 359.17

---------------------------------------------------------------

## File Descriptions:

`launch-output_sim.csv` is the OpenRocket output with the prelaunch
parameters. The csv contains the total output of the data
(all columns and events were turned on).
