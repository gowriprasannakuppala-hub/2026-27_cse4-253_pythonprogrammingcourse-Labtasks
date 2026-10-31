# 03/10/2026 9:41am
# valid triangle angle
Angle_1=float(input("Enter first angle : "))
Angle_2 = float(input("Enter second angle : "))
Angle_3 = float(input("Enter third angle : "))
if Angle_1>0 and Angle_2>0 and Angle_3>0 and Angle_1+Angle_2+Angle_3==180:
  print(f" {Angle_1},{Angle_2},{Angle_3} is valid")
else:
  print(f"{Angle_1},{Angle_2},{Angle_3} is not valid")
