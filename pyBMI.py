#!/usr/bin/env python

#    2010 Giannis Fysakis
#    E-mail: giannisfs@gmail.com
#    Released subject to the GPL 3 License
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
    BodyMassIndexOf calculates the BMI (body mass index )
    according to http://apps.who.int/bmi/index.jsp?introPage=intro_3.html .
    Prints out within which classes someone belongs to ,and finds how many kg
    someone needs to lose to become fit (Normal).
    Example:
        >>> George = BodyMassIndexOf(100,180,"George")
        >>> George.bmi()
        '30.86'
        >>> George.evaluateBMI()
        'George Belongs to Obese Class Specifically to Class I Considered in the lowest range of Obese Class I cut-off points'
        >>> George.LoseWeight()
        {'Minimum': '19.02', 'Maximum': '40.05', 'Mean': '27.93'}
        >>> George.willWeighAfterDiet()
        {'Afer a Maximum diet ': '59.95', 'Afer a Minimum diet ': '80.98', 'Afer a Mean diet ': '72.07'}
        
    .........................................................................................
    So George have to lose 19 kg to enter the Normal range (with bmi 24.99)
    .........................................................................................
"""

import sys

class BodyMassIndexOf():
    #BMI Classification
    _BMICLFN= {"UnderWeight": "%.3f <18.50" ,\
                  "SevereThin": "%.3f <16.00",\
                  "ModThin": "16.00 <= %.3f <= 16.99" ,\
                  "MildThin": "17.00 <= %.3f <= 18.49",\
                  "NormalRange": "18.50 <= %.3f <= 24.99",\
                  "OverWeight": "25.00 <= %3.f <=29.99",\
                  "PreObese": "25.00 <= %.3f <= 29.99",\
                  "Obese": " %.3f >= 30.00" ,\
                  "ObeseClassI":"30.00 <= %.3f <= 34.99",\
                  "ObeseClassII":"35.00 <= %.3f <= 39.99",\
                  "ObeseClassIII":"%.3f >= 40.00"
                  }
    
    def __init__(self,mass,height,name):
        try :
            mass = float(mass)
            height = float(height)          
        except (ValueError,TypeError):
            raise ValueError("Please Only Real Numbers no nonexistance or imaginary ,complex etc ...!!!")
        
        if mass < 1 or mass > 500:
            sys.stderr.write("No human is less than 1 kg or bigger than 500 kg")
            exit()
        elif str(mass).index('.') > 3 or str(height).index('.') > 3:
            sys.stderr.write("Accepted only Kg for mass and m and cm for Height")
            exit()
        elif height > 280 or height < 1:
            sys.stderr.write("Nobody has these dimensions...")
            exit()

        
        self.mass = mass
        self.height = height
        self.name = name
    
    def bmi(self):
        
        M = self.mass  
        H = self.height
        #To distinguish cm from meters one possible way is...
        if str(H).find('.') == 1 or len(str(H)) == 1:
            return  "%.2f" % (M / H ** 2)
        elif str(H).find('.') > 1 or len(str(H)) > 2:
            return  "%.2f" % (M / (H / 100.0) ** 2)
    def evaluateBMI(self):
        TheBmi="%s " %(self.name)
        
        bmi = float(self.bmi())
        test = BodyMassIndexOf._BMICLFN
        
        if eval( test["UnderWeight"] % bmi ):
            TheBmi += "Belongs to Underweight Class "
        if eval( test["SevereThin"] % bmi ):
            TheBmi +="has Severe Thinness "
        if eval( test["ModThin"] % bmi ):
            TheBmi +="has Moderate Thinness "
        if eval( test["MildThin"] % bmi ):
            TheBmi +="has Mild  Thinness "
        if eval( test["NormalRange"] % bmi ):
            TheBmi += "Belongs to NormalRange Class "
            if 18.50 <=  bmi <= 22.99 :
                TheBmi += "with the least risk"
            else:
                TheBmi += "with a very small risk"
        if eval( test["OverWeight"] % bmi ):
            TheBmi += "Belongs to Overweight Class "
        if eval( test["PreObese"] % bmi ):
            TheBmi +="Specifically in Pre-obese Class "
            if 25.00 <= bmi <= 27.49:
                TheBmi +="Considered in the lowest range of Pre-obese cut-off points"
            else:
                TheBmi +="Considered in the highest range of Pre-obese cut-off points"
        if eval( test["Obese"] % bmi ):
            TheBmi += "Belongs to Obese Class "
        if eval( test["ObeseClassI"] % bmi ):
            TheBmi +="Specifically to Class I "
            if 30.00 <= bmi <= 32.49 :
                TheBmi += "Considered in the lowest range of Obese Class I cut-off points"
            else:
                TheBmi += "Considered in the highest range of Obese Class I cut-off points"
        if eval( test["ObeseClassII"] % bmi ):
            TheBmi +="Specifically to Class II "
            if 35.00 <= bmi <= 37.49 :
                TheBmi += "Considered in the lowest range of Obese Class II cut-off points"
            else:
                TheBmi += "Considered in the highest range of Obese Class II cut-off points"
        if eval( test["ObeseClassIII"] % bmi ):
            TheBmi +="Specifically to Class I  which is the most risky Class"
        return TheBmi


    def  LoseWeight(self):
        bmi = float(self.bmi())
        #test = BodyMassIndexOf._BMICLFN
        if bmi >= 18.50 :
            Max = ( self.mass * 18.50) / bmi
            Max = self.mass - Max
            if Max < 0 : Max = 0
            
            Mean = (self.mass * 22.24) / bmi
            Mean = self.mass - Mean
            if Mean < 0 : Mean = 0
            Min = ( self.mass * 24.99) / bmi
            Min = self.mass - Min
            if Min < 0 : Min = 0
            
        elif bmi < 18.50:
            return "No need to lose weight"
            
        return {"Maximum": "%.2f" % (Max),"Mean":"%.2f"% (Mean) ,"Minimum":"%.2f" % (Min)}
            
    def willWeighAfterDiet(self):
        dietTargets = self.LoseWeight()
        res = {}
        M = self.mass
        bmi = float(self.bmi())
        for k,v in dietTargets.iteritems():

            res["Afer a "+ k + " diet "] = "%.2f" % ( M - float(v) )
        return res
