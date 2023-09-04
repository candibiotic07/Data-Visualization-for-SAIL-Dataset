import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





#
#part1
#

df=pd.read_csv('concatentaion_1Drive_3hours_00_04_32-02_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')

#plotting all features w.r.t. Time in a single image
df.plot(subplots=True, figsize=(10,12))
plt.savefig('24.png')
plt.show()



#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})



#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 00:04:32.850 - 02:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_0-3.png')

plt.plot(SPD_FBK)
plt.title('SPD_FBK 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')
plt.savefig('SPD_FBK_0-3.png')

plt.plot(ARM_CUR)
plt.title('ARM_CUR 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')
plt.savefig('ARM_CUR_0-3.png')

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')
plt.savefig('ARM_VOLT_0-3.png')

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')
plt.savefig('Billet_temp_Dstrand_0-3.png')

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 00:04:32-02:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')
plt.savefig('Billet_temp_All_strand_0-3.png')





#
#part2
#

df=pd.read_csv('concatentaion_1Drive_3hours_03_04_32-05_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')



#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})



#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 03:04:32.850 - 05:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_3-6.png')

plt.plot(SPD_FBK)
plt.title('SPD_FBK 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')

plt.plot(ARM_CUR)
plt.title('ARM_CUR 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 03:04:32-05:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')



#
#part3
#

df=pd.read_csv('concatentaion_1Drive_3hours_06_04_32-08_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')



#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})



#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 06:04:32.850 - 08:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_6-9.png')
plt.close()

plt.plot(SPD_FBK)
plt.title('SPD_FBK 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')
plt.savefig('SPD_FBK_6-9.png')
# plt.show()
plt.close()

plt.plot(ARM_CUR)
plt.title('ARM_CUR 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')
plt.savefig('ARM_CUR_6-9.png')
# plt.show()
plt.close()

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')
plt.savefig('ARM_vOLT_6-9.png')
# plt.show()
plt.close()

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')
plt.savefig('Billet_D_6-9.png')
# plt.show()
plt.close()

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 06:04:32-08:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')
plt.savefig('Billet_ALL_6-9.png')
# plt.show()
plt.close()

#
#part4
#

df=pd.read_csv('concatentaion_1Drive_3hours_09_04_32-11_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')



#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})



#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 09:04:32.850 - 11:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_9-12.png')
plt.close()

plt.plot(SPD_FBK)
plt.title('SPD_FBK 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')
plt.savefig('SPD_FBK_9-12.png')
plt.close()

plt.plot(ARM_CUR)
plt.title('ARM_CUR 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')
plt.savefig('ARM_CUR_9-12.png')
plt.close()

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')
plt.savefig('ARM_VOLT_9-12.png')
plt.close()

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')
plt.savefig('Billet_Temp_D_9-12.png')
plt.close()

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 09:04:32-11:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')
plt.savefig('Billet_Temp_ALL_9-12.png')
plt.close()


#
#part5
#

df=pd.read_csv('concatentaion_1Drive_3hours_12_04_32-14_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')


#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})



#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 12:04:32.850 - 14:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_12-15.png')

plt.plot(SPD_FBK)
plt.title('SPD_FBK 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')

plt.plot(ARM_CUR)
plt.title('ARM_CUR 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 12:04:32-14:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')


#
#part6
#

df=pd.read_csv('concatentaion_1Drive_3hours_15_04_32-17_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')

 

#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})

 
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 15:04:32.850 - 17:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_15-18.png')

plt.plot(SPD_FBK)
plt.title('SPD_FBK 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')

plt.plot(ARM_CUR)
plt.title('ARM_CUR 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 15:04:32-17:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')


#
#part7
#

df=pd.read_csv('concatentaion_1Drive_3hours_18_04_32-20_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')

 
#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})

 

#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 18:04:32.850 - 20:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')

plt.plot(SPD_FBK)
plt.title('SPD_FBK 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')

plt.plot(ARM_CUR)
plt.title('ARM_CUR 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 18:04:32-20:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')


#
#part8
#

df=pd.read_csv('concatentaion_1Drive_3hours_21_04_32-23_59_32.csv')

df=df.drop('Unnamed: 0',axis=1)
df["time"]= pd.to_datetime(df["time"])
df=df.set_index('time')

 

#renaming columns as they show error while plotting
df = df.rename(columns = {"1D_SPD_REF":"SPD_REF"})
df = df.rename(columns = {"1D_SPD_FBK":"SPD_FBK"})
df = df.rename(columns = {"1D_ARM_CUR":"ARM_CUR"})
df = df.rename(columns = {"1D_ARM_VOLT":"ARM_VOLT"})
df = df.rename(columns = {"Billet Temp. D strand":"Billet_Temp_D_strand"})
df = df.rename(columns = {"Billet Temp. ALL strnd":"Billet_Temp_ALL_strnd"})

 

#resampling rows based on 3 minute, by taking average value for 3 minute entries.
SPD_REF = df.SPD_REF.resample('3T').mean()
SPD_FBK = df.SPD_FBK.resample('3T').mean()
ARM_CUR = df.ARM_CUR.resample('3T').mean()
ARM_VOLT = df.ARM_VOLT.resample('3T').mean()
Billet_Temp_D_strand = df.Billet_Temp_D_strand.resample('3T').mean()
Billet_Temp_ALL_strnd = df.Billet_Temp_ALL_strnd.resample('3T').mean()





#plotting data from 21:04:32.850 - 23:59:32.850
plt.plot(SPD_REF)
plt.title('SPD_REF 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_REF')
plt.savefig('SPD_REF_21-24.png')
plt.close()

plt.plot(SPD_FBK)
plt.title('SPD_FBK 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('SPD_FBK')
plt.savefig('SPD_FBK_21-24.png')
plt.close()

plt.plot(ARM_CUR)
plt.title('ARM_CUR 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_CUR')
plt.savefig('ARM_CUR_21-24.png')
plt.close()

plt.plot(ARM_VOLT)
plt.title('ARM_VOLT 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('ARM_VOLT')
plt.savefig('ARM_VOLT_21-24.png')
plt.close()

plt.plot(Billet_Temp_D_strand)
plt.title('Billet_Temp_D_strand 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_D_strand')
plt.savefig('Billet Temp_D_21-24.png')
plt.close()

plt.plot(Billet_Temp_ALL_strnd)
plt.title('Billet_Temp_ALL_strnd 21:04:32-23:59:32')
plt.xlabel('Time')
plt.ylabel('Billet_Temp_ALL_strnd')
plt.savefig('Billet Temp_ALL_21-24.png')
plt.close()
