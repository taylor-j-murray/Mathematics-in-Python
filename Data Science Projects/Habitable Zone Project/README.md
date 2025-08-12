> **Author**: Taylor Murray  
> **Language**: Python 3.10  
> **Tools**: Standard Python Libraries, Pandas
> **Focus**: Data Science, Astrology, Habitable Zones of Planets, the Kopparapu Formulae

# Exoplanets and the Habitable Zone of their Stars (Version 1.0)

## Overview:

Using a [database of known exoplanets](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue), licensed by MIT, we create a new
database indicating whether or not a given planet lies in the habitable zone (HZ) of its star system (see the methodology below) **while taking into account the eccentricity** of the planet's orbit. Our new database includes new features whose values were used in determining the habitable zone of a planets star system.


## Concepts Used:
* A [database of known exoplanets](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue) licensed by MIT.
* [The Kopparapu Formulae](https://arxiv.org/pdf/1404.5292).
* Data Manipulation with Pandas.



## Methodology (Using the Kopparapu Formulae):
In the paper ['Habitable Zones Around Main-Sequence Stars: Dependence on Planetary Mass'](https://arxiv.org/pdf/1404.5292), Kopparapu and co-authors propose formulae in determining the habitable zones of stars depending on planetary mass. To do this, they use the equations 

```math
S_{eff} = S_{eff \odot} + aT_* + bT_*^2 + cT_*^3 + dT_*^4   
```
```math
D = \sqrt{\left( \frac{L/ L_\odot}{S_{eff}}\right)}
```

where 

* $1600 K \leq T_{eff} \leq 7200 K$,
* The planet in question has a mass in between 0.1 and 5 Earth masses,
* $S_{eff}$ is the solar efficiency of a given star,
* $S_{eff \odot}$ is the solar efficiency of our sun,
* $T_* = T_{eff} - 5780 K$, where $T_{eff}$ is the effective temperature (in Kelvin) of a given star,
* $a,b,c,d$ are coefficients determined by the planets mass and whether you are looking for the maximal or minimal radius of the habitable zone displayed below,
* $D$ is the corresponding habitable zone distance,
* $L$ is the luminosity of a given star in Watts, and $L_\odot$ is the luminosity of our sun in Watts.



|                                                 | Mass of Planet in Earth masses | $S_{eff \odot}$ | a | b | c | d |
|-------------------------------------------------|--------------------------------|----------------|---|---|---|---|
| Runaway Greenhouse (to find minimal HZ distance in AU)| 0.1 | 0.99 | $1.029 \times 100^{-4}$| $1.404 \times 10^{-8}$ | $-7.418\times 10^{-12}$ | $-1.713\times 10^{-15}$|
| Runaway Greenhouse (to find minimal HZ distance in AU) | 1.0 | 1.107| $1.332 \times 100^{-4}$| $1.58\times 10^{-8}$ | $-8.308 \times 10^{-12}$ | $-1.931\times 10^{-15}$|
| Runaway Greenhouse (to find minimal HZ distance in AU)| 5.0 | 0.356 | $1.188\times 100^{-4}$| $1.707 \times 10^{-8}$ | $-8.398\times 10^{-12}$ | $-2.084\times 10^{-15}$|
| Maximal Greenhouse (to find maximal HZ distance in AU)| 0.1 | 0.356 |  $6.171\times 10^{-5}$ |  $1.698 \times 10^{-9}$ | $-3.198 \times 100^{-12}$ | $-5.575 \times 10^{-16}$ |
| Maximal Greenhouse (to find maximal HZ distance in AU)| 1.0 | 0.356 |  $6.171\times 10^{-5}$ |  $1.698 \times 10^{-9}$ | $-3.198 \times 100^{-12}$ | $-5.575 \times 10^{-16}$ |  
| Maximal Greenhouse (to find maximal HZ distance in AU)| 5.0 | 0.356 |  $6.171\times 10^{-5}$ |  $1.698 \times 10^{-9}$ | $-3.198 \times 100^{-12}$ | $-5.575 \times 10^{-16}$| 
          


**Important Note**: in `habitablezone.py` the author applies the following conventions

* If a planet's mass is between 0.1 and 1.0 (not including the latter) Earth masses, we use the coefficients for 0.1 earth masses in Kopparapu Formula.
* If a planet's mass is between 1.0 and 5.0 (not including the latter) Earth masses, we use the coefficients for 1 earth masses in Kopparapu Formula.
* If a planet's mass is greater than or equal to 5.0 Earth masses, we use the coefficients for 5 earth masses in Kopparapu Formula. Here the results may be wildely off if the planet's mass is much larger than 5 earth masses.


### Using the Kopparapu Formulae

Suppose you have a planet P in a star system with the following attributes:

* $T_{eff} = 4000K$.
* P has a mass of 2 earth masses.
* $L/L_{\odot} = 1.032$ (note that units are not given since this is normalized).

To find the minimal HZ distance, we set

* $S_{eff \odot} = 1.107$
* $a = 1.332 \times 100^{-4}$
* $b = 1.58\times 10^{-8}$ 
* $c = -8.308 \times 10^{-12}$
* $d = -1.931\times 10^{-15}$

and calculate $ T_* = -1780 K$ and $S_{eff} = 1.05916$. Finally, we find that our minimal HZ distance is $D = 0.9885289428749514 AU$


## Project Structure:

 The CSV file `Habitable_Zone_data.csv` is the data base indicating whether or not a given planet lies in the habitable zone (HZ) of its star system. The code that creates this new database is in `habitablezone.py`.

### Features of Habitable_Zone_data.csv
* Planet_Identifier - 'A label for an exoplanet'
* Planetary_Mass_Earth - the mass of the planet in earth masses
* 'Luminosity_of_Host_Star' - the luminosity of the host star in solar units (normalized)
* 'Runaway_Greenhouse_S_eff' - the solar efficiency of the host star for the minimal HZ distance given the planets mass
* 'Maximum_Greenhouse_S_eff' - the solar efficiency of the host star for the maximal HZ distance given the planets mass
* 'Runaway_Greenhouse' - the minimal HZ distance for the host star in AU
* 'Maximum_Greenhouse' - the maximal HZ distance for the host star in AU
* 'IsInHabitableZone' - Indicates if the planet lies in its stars habitable zone.

### Structure of `habitablezone.py`

Below are the functions used and defined in `habitablezone.py`
*  `j_to_e_mass`: converts a planets mass in Jupiter masses to earth masses

* `lum`: calculates a stars luminosity in solar units given its radius and temperature.

* `RG_coeff_setup`: selects the proper coefficients for the Kopparapu formula for runaway greenhouse.

* `def MG_coeff_setup(p)`: selects the proper coefficients for the Kopparapu formula for maximal greenhouse.

* `RG_S_eff`: returns the Runaway Greenhouse solar efficiency as determined by the mass of the planet associated to this row.

* `RG_radius`: returns the minimal distance for the planet's (associated to this row) habitable zone with respect to its host star. 

* `MG_S_eff`: returns the Maximum Greenhouse solar efficiency as determined by the mass of the planet associated to this row.

* `MG_radius`: returns the maximum distance for the planet's (associated to this row) habitable zone with respect to its host star. 

* `in_HZ`: returns a boolean whether indicating whether or not a planet is in its star systems habitable zone. **Takes into account the eccentricity of its orbit**.








