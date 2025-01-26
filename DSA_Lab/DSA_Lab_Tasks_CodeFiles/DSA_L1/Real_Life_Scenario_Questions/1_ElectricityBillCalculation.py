#Electricity Bill Calculation
meter_rent=1500
additional_tax=200
units_consumed=int(input("Enter the units consumed:"))
if units_consumed<=100:
    bill=units_consumed*30+meter_rent+additional_tax
elif units_consumed<=300:
    bill=units_consumed*40+meter_rent+additional_tax
else:
    bill=units_consumed*60+meter_rent+additional_tax
print("Electricity Bill:",bill)