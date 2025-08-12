import pandas as pd
import numpy as np
import math

file_path = 'Data Science Projects/Habitable Zone Project/planet_data_base.csv'

# read in file_path
planet_db= pd.read_csv(file_path)

# List of columns
planet_db.columns

# Look here for field/column description https://github.com/OpenExoplanetCatalogue/oec_tables/blob/master/FIELDS.md
# The most important columns for us will be 'HostStarRadiusSlrRad', 'HostStarTempK','PlanetaryMassJpt'

#coefficients for a,b,c,d and S_{eff, \Odot} as given in the Kopparapu equations
RG_zero_point_one = {'SeffOdot' : 0.99, 
                     'a': 1.029 * (10 **(-4)), 
                     'b': 1.404 * (10 **(-8)), 
                     'c': -7.418 * ( 10 ** (-12)) ,
                     'd': -1.713 * ( 10**(-15)) } # mass in between 0.1 and 1 earth masses (not including 1). For Runaway Greenhouse.



RG_one_point_zero = {'SeffOdot' : 1.107, 
                     'a': 1.332 * (10 **(-4)), 
                     'b': 1.58 * (10 **(-8)), 
                     'c': -8.308 * ( 10 ** (-12)) ,
                     'd': -1.931 * ( 10**(-15)) } # mass in between 1 and 5 earth masses (not including 5). For Runaway Greenhouse.

RG_five_point_zero = {'SeffOdot' : 1.188, 
                      'a': 1.433 * (10 **(-4)), 
                      'b': 1.707 * (10 **(-8)), 
                      'c': -8.398 * ( 10 ** (-12)) ,
                      'd': -2.084 * ( 10**(-15)) }  # mass greater than or equal to 5 ear masses. For Runaway Greenhouse.

MG_all = {'SeffOdot' : 0.356, 
          'a': 6.171 * ( 10 ** (-5)), 
          'b': 1.698 * ( 10 ** (-9)), 
          'c': -3.198 * (10 ** (-12)) ,
          'd': -5.575 * (10 ** (-16))} # All masses. For Maximal Greenhouse

lum_sun = 3.828 * (10 ** (26)) # luminosity of the sun in Watts



def j_to_e_mass (j_m : float):
    """Given a planets mass is j_m-times that of Jupiter's mass, this function
    returns the number N, where the planets mass is N-times that of Earth's mass. 

    Parameters
    -------------
    j_m (float) : The mass of a given planet divided by the mass of Jupiter.

    
    Returns
    -------------
    float : The mass of the given planet divided my the mass of Earth.

    """
    e_mass = 5.9722 * (10 ** (24)) 
    j_mass = 1.8986 * (10 ** (27))
    ratio_j_to_e = (j_mass)/(e_mass)
    return j_m * ratio_j_to_e

def earth_mass(p):
    j_m = p['PlanetaryMassJpt']
    j_e = j_to_e_mass(j_m)
    p['Planetary_Mass_Earth'] = j_e
    return p

def lum(p):
    """ From a row p in planet_db, this function calculates the luminosity of the 
    host star associated to this row. 

    Parameters
    ------------
    p : a row in planet_db

    Return
    ------------
    float : The luminosity (in solar units) to the host star associated to p.
    
    """
    star_rad = p['HostStarRadiusSlrRad']  # This is already in solar units.
    star_temp = p['HostStarTempK'] / 5800   # We normalize here by 5800 to put into solar units.
    if (pd.isna(star_rad)) or (pd.isna(star_temp)):
        p['Luminosity_of_Host_Star'] = np.nan
    else: 
        L = (star_rad**2)*(star_temp**4)
        p['Luminosity_of_Host_Star'] = L
    return p
    


def RG_coeff_setup(p):
    """ Given a row in planet_db, this function returns the coefficients to be used in the Kopparapu formula 
    for the Running Greenhouse solar efficiency S_eff as determined by the mass of the planet associated to this row.

    Parameters
    ------------
    p : 
        a row in planet_db
    
    Returns
    ------------
    dict : 
        a dictionary whose keys are the coefficients in Kopparapu's formula for 
        the Running Greenhouse solar efficiency and whose values 
        are the appropriate floats to be used in place of their respective coefficients.
        In particular ['SeffOdot', 'a', 'b', 'c', 'd'] 
        are the keys of the dictionary and the values of these keys 
        are the corresponding floats to be employed in Kopparapu's formula.
        
    
    """
    planet_jup_mass = p['PlanetaryMassJpt']
    mass = j_to_e_mass(planet_jup_mass)
    if (0.1 <= mass < 1):
        return RG_zero_point_one.copy()
    elif (1 <= mass < 5):
        return RG_one_point_zero.copy()
    elif ( 5<= mass ):
        return RG_five_point_zero.copy()
    else:
        return None
    

def MG_coeff_setup(p):
    """ Given a row in planet_db, this function returns the coefficients to be used in the Kopparapu formula 
    for the Maximum Greenhouse solar efficiency S_eff as determined by the mass of the planet associated to this row.

    Parameters
    ------------
    p : 
        a row in planet_db
    
    Returns
    ------------
    dict : 
        a dictionary whose keys are the coefficients in Kopparapu's formula for 
        the Maximum Greenhouse solar efficiency and whose values 
        are the appropriate floats to be used in place of their respective coefficients.
        In particular ['SeffOdot', 'a', 'b', 'c', 'd'] 
        are the keys of the dictionary and the values of these keys 
        are the corresponding floats to be employed in Kopparapu's formula.
    """
    planet_jup_mass = p['PlanetaryMassJpt']
    mass = j_to_e_mass(planet_jup_mass)
    if (0.1 <= mass):
        return MG_all
    else: 
        return None

    


def RG_S_eff(p):
    """ Given a row in planet_db this function returns the Runaway Greenhouse solar efficiency as determined by 
    the mass of the planet associated to this row.

    Parameters
    ------------
    p : 
        a row in planet_db

    Returns
    ------------
    float: 
        the Runaway Greenhouse solar efficiency for the planet associated to row p
    """
    Seff ='Runaway_Greenhouse_S_eff' 
    if RG_coeff_setup(p) == None:
        p[Seff] = np.nan
    elif pd.isna(p['HostStarTempK']):
        p[Seff] = np.nan
    elif p['HostStarTempK'] < 2600 or p['HostStarTempK'] >= 7200:
        p[Seff] = np.nan
    else: 
        Teff = p['HostStarTempK']
        T = Teff - 5780
        coeff = RG_coeff_setup(p)
        S = coeff['SeffOdot'] + coeff['a']*T + coeff['b']*(T ** 2) + coeff['c']*(T**3) + coeff['d']*(T**4)
        p[Seff] = S 
    return p

def RG_radius(p):
    """
    Given a row in planet_db this function returns the minimal distance for the planet's (associated to this row) 
    habitable zone with respect to its host star. 

    Parameters

    ------------
    p :
        a row in planet_db

    Returns

    ------------

    float: 
        the minimal distance for the planet's (associated to this row) 
        habitable zone with respect to its host star. 
    """
    L = p['Luminosity_of_Host_Star']
    S = p['Runaway_Greenhouse_S_eff']
    if  pd.isna(S) or pd.isna(L):
        p['Runaway_Greenhouse'] = np.nan
    else:
        d = math.sqrt((L)/S)
        p['Runaway_Greenhouse'] = d
    return p


def MG_S_eff(p):
    """ Given a row in planet_db this function returns the Maximum Greenhouse solar efficiency as determined by 
    the mass of the planet associated to this row.

    Parameters
    ------------
    p : 
        a row in planet_db

    Returns
    ------------
    float: 
        the Maximum Greenhouse solar efficiency for the planet associated to row p
    """
    Seff = 'Maximum_Greenhouse_S_eff'
    if MG_coeff_setup(p) == None:
        p[Seff] = np.nan
    elif pd.isna(p['HostStarTempK']):
        p[Seff] = np.nan
    elif p['HostStarTempK'] < 2600 or p['HostStarTempK'] >= 7200:
        p[Seff] = np.nan
    else: 
        Teff = p['HostStarTempK']
        T = Teff - 5780
        coeff = MG_coeff_setup(p)
        S = coeff['SeffOdot'] + coeff['a']*T + coeff['b']*(T ** 2) + coeff['c']*(T**3) + coeff['d']*(T**4)
        p[Seff] = S 
        return p


def MG_radius(p):
    """
    Given a row in planet_db this function returns the maximum distance for the planet's (associated to this row) 
    habitable zone with respect to its host star. 

    Parameters

    ------------
    p : a row in planet_db

    Returns

    ------------

    float: 
        the maximum distance for the planet's (associated to this row) 
        habitable zone with respect to its host star. 
    """
    L = p['Luminosity_of_Host_Star']
    S = p['Maximum_Greenhouse_S_eff']
    if  pd.isna(S) or pd.isna(L) :
        p['Maximum_Greenhouse'] = np.nan
    else:
        d = math.sqrt((L)/S)
        p['Maximum_Greenhouse'] = d
    return p



def in_HZ(p):
    """ This function indicates whether or not a planet in a given row in the its solar systems habitable zone.

    Parameters:
    --------------
    p : a row in planet_db

    Returns:

    -------------

    bool:
        If the planet in row p is in the HZ of its solar system, this function return the boolean True. Otherwise, this function
        returns the boolean False.
    """
    RG = p['Runaway_Greenhouse']
    MG = p['Maximum_Greenhouse']
    a = p['SemiMajorAxisAU']
    e = p['Eccentricity']
    if pd.isna(RG) or pd.isna(MG) or pd.isna(a) or pd.isna(e):
        p['Is_In_Habitable_Zone'] = np.nan
    elif a < RG or a > MG:
        p['Is_In_Habitable_Zone'] = False
    else:
        b = a*(np.sqrt(1-e**2)) # define b here to save computational power. No need to find it if a<RG or a>MG
        if b < RG: 
            p['Is_In_Habitable_Zone'] = False
        else:
            p['Is_In_Habitable_Zone'] = True
    return p



func_list = [earth_mass,lum, RG_S_eff, MG_S_eff, RG_radius, MG_radius, in_HZ]
for func in func_list:
    planet_db = planet_db.apply(func, axis =1) # creates new columns using the functions in func_list

planet_db_new = planet_db.loc[:,['PlanetIdentifier',
                'Planetary_Mass_Earth',
                'Eccentricity',
                'SemiMajorAxisAU',
                'HostStarRadiusSlrRad',
                'HostStarTempK',
                'Luminosity_of_Host_Star',
                'Runaway_Greenhouse_S_eff',
                'Maximum_Greenhouse_S_eff',
                'Runaway_Greenhouse',
                'Maximum_Greenhouse',
                'Is_In_Habitable_Zone']] #creates new database with selected columns
planet_db_new = planet_db_new.rename(columns = {'PlanetIdentifier': 'Planet_Identifier',
                                        'HostStarRadiusSlrRad' : 'Host_Star_Radius_Solar',
                                        'HostStarTempK' : 'Host_Star_Temperature_Kelvin',
                                        'SemiMajorAxisAU' : 'Semi_Major_Axis_AU'}) # renames columns in new database 



planet_db_new.to_csv('Data Science Projects/Habitable Zone Project/Habitable_Zone_data.csv') # writes to indicated csv file



