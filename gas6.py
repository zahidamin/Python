# Input readings
previous_reading = int(input("Please enter your previous reading: "))
current_reading = int(input("Please enter your current reading: "))
difference = current_reading - previous_reading
print("Difference:", difference)

# Input factors
factor = float(input("Factor: "))
gcv = float(input("GCV: "))
fix = float(input("Fix: "))
meter_rent = float(input("Meter Rent: "))

# Calculate hm3 and mmbtu
hm3 = (difference * factor)/100000
print("HM3:", hm3)

mmbtu = (hm3 * gcv) / 281.7385
print("MMBTU:", mmbtu)

#Gas Tarif
s1= (500/0.25)
s2= (850/0.60)
s3 = (1250/1.0) 
s4 = (1450/1.5)
s5 = (1900/2)
s6 = (3300/3)
s7 = (3800/4)
s8 = (4200)


# Determine price based on mmbtu slab
if hm3 <= 0.25:
    rate = s1
elif hm3 > 0.25 and hm3 <= 0.60:
    rate = s2
elif hm3 > 0.60 and hm3 <= 1.0:
    rate = s3
elif hm3 > 1.0 and hm3 <= 1.5:
    rate = s4
elif hm3 > 1.5 and hm3 <= 2:
    rate = s5
elif hm3 > 2.0 and hm3 <= 3:
    rate = s6
elif hm3 > 3.0 and hm3 <= 4:
    rate = s7
else:
    rate = s8

# Calculate gas charges
print("Price:",rate)

#gas_charges = (rate * mmbtu) * hm3
#print("Gas Charges:", gas_charges)

# Calculate total cost
#total = gas_charges
#print("Total without GST:", total)

# Calculate GST
gst = (rate+ meter_rent + fix) * 0.18  # GST is 18%
print("GST:", gst)

# Calculate final amount
final_amount = rate+ meter_rent + fix + gst 
print("Final Amount (with gas charges, meter rent, and GST):", final_amount)
