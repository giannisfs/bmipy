#!/usr/bin/env python
#-*-coding: utf-8 -*-

# 2010 Gianis Fysakis
# E-mail: giannisfs@gmail.com
# Released subject to the GPL 3 License

"""
    BodyMassIndexOf calculates the BMI (body mass index )
    according to "http://apps.who.int/bmi/index.jsp?introPage=intro_3.html"
    also finds how many kg someone needs to loose to become fit (Normal)
    Example:
                >>> George = BodyMassIndexOf(100,180,"George")
                >>> print George.bmi()
                        30.864
                >>> George.evaluateBMI()
                        'George Belongs to Obese Class Specifically to Class II Considered in the lowest range of Obese Class II cut-off points'
                >>> George.LoseToBeNormal()
                        {'Best': '40.06', 'Normal': '19.03'}
    .........................................................................................
    So George needs too loose at least 19 kg to become Normal
    .........................................................................................
"""
import sys

class BodyMassIndexOf():
    #BMI Classification
    _BMICLFN= {"UnderWeight": "%.3f <18.50" ,\
                  "SevereThin": "%.3f <16.00",\
                  "ModThin": "16.00 >= %.3f <= 16.99" ,\
                  "MildThin": "17.00 >= %.3f <= 18.49",\
                  "NormalRange": "18.50 >= %.3f <= 24.99",\
                  "OverWeight": "25.00 >= %3.f <=29.99",\
                  "PreObese": "25.00 >= %.3f <= 29.99",\
                  "Obese": " %.3f >= 30.00" ,\
                  "ObeseClassI":"30.00 >= %.3f <= 34.99",\
                  "ObeseClassII":"35.00 >= %.3f <= 39.99",\
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
            return  "%.3f" % (M / H ** 2)
        elif str(H).find('.') > 1 or len(str(H)) > 2:
            return  "%.3f" % (M / (H / 100.0) ** 2)
    def evaluateBMI(self):
        TheBmi="%s " %(self.name)
        
        bmi = float(self.bmi())
        test = BodyMassIndexOf._BMICLFN
        
        if eval( test["UnderWeight"] % bmi ):
            TheBmi += "Belongs to Underweight Class "
            #return "%s are Underweight " % self.name
        if eval( test["SevereThin"] % bmi ):
            TheBmi +="Specifically has Severe Thinness "
        if eval( test["ModThin"] % bmi ):
            TheBmi +="Specifically has Moderate Thinness "
        if eval( test["MildThin"] % bmi ):
            TheBmi +="Specifically has Mild  Thinness "
        if eval( test["NormalRange"] % bmi ):
            TheBmi += "Belongs to NormalRange Class "
            if 18.50 >=  bmi <= 22.99 :
                TheBmi += "with the less risk"
            else:
                TheBmi += "but with a tiny risk"
        if eval( test["OverWeight"] % bmi ):
            TheBmi += "Belongs to Overweight Class "
        if eval( test["PreObese"] % bmi ):
            TheBmi +="Specifically in Pre-obese Class "
            if 25.00 >= bmi <= 27.49:
                TheBmi +="Considered in the lowest range of Pre-obese cut-off points"
            else:
                TheBmi +="Considered in the highest range of Pre-obese cut-off points"
        if eval( test["Obese"] % bmi ):
            TheBmi += "Belongs to Obese Class "
        if eval( test["ObeseClassI"] % bmi ):
            TheBmi +="Specifically to Class I "
            if 30.00 >= bmi <= 32.49 :
                TheBmi += "Considered in the lowest range of Obese Class I cut-off points"
            else:
                TheBmi += "Considered in the highest range of Obese Class I cut-off points"
        if eval( test["ObeseClassII"] % bmi ):
            TheBmi +="Specifically to Class II "
            if 35.00 >= bmi <= 37.49 :
                TheBmi += "Considered in the lowest range of Obese Class II cut-off points"
            else:
                TheBmi += "Considered in the highest range of Obese Class II cut-off points"
        if eval( test["ObeseClassIII"] % bmi ):
            TheBmi +="Specifically to Class I  which is the most risky Class"
        return TheBmi


    def  LoseToBeNormal(self):
        bmi = float(self.bmi())
        test = BodyMassIndexOf._BMICLFN
        if not eval( test['NormalRange'] % bmi) and bmi >= 25.0:
            Best = ( self.mass * 18.50) / bmi
            Best = self.mass - Best
            Normal = ( self.mass * 24.99) / bmi
            Normal = self.mass - Normal

        return {"Best": "%.2f" % (Best), "Normal": "%.2f" % (Normal)}
            


