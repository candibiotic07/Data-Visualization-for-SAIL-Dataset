
import pandas as pd
import numpy as np 

# #reading csv files for 1st hour
# df1=pd.read_csv("ALL000_2021-11-02_00.04.32.csv")
# df2=pd.read_csv("ALL001_2021-11-02_00.09.32.csv")
# df3=pd.read_csv("ALL002_2021-11-02_00.14.32.csv")
# df4=pd.read_csv('ALL003_2021-11-02_00.19.32.csv')
# df5=pd.read_csv('ALL004_2021-11-02_00.24.32.csv')
# df6=pd.read_csv('ALL005_2021-11-02_00.29.32.csv')
# df7=pd.read_csv('ALL006_2021-11-02_00.34.32.csv')
# df8=pd.read_csv('ALL007_2021-11-02_00.39.32.csv')
# df9=pd.read_csv('ALL008_2021-11-02_00.44.32.csv')
# df10=pd.read_csv('ALL009_2021-11-02_00.49.32.csv')
# df11=pd.read_csv('ALL010_2021-11-02_00.54.32.csv')
# df12=pd.read_csv('ALL011_2021-11-02_00.59.32.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL012_2021-11-02_01.04.32.csv")
# df14=pd.read_csv("ALL013_2021-11-02_01.09.32.csv")
# df15=pd.read_csv("ALL014_2021-11-02_01.14.32.csv")
# df16=pd.read_csv('ALL015_2021-11-02_01.19.32.csv')
# df17=pd.read_csv('ALL016_2021-11-02_01.24.32.csv')
# df18=pd.read_csv('ALL017_2021-11-02_01.29.32.csv')
# df19=pd.read_csv('ALL018_2021-11-02_01.34.32.csv')
# df20=pd.read_csv('ALL019_2021-11-02_01.39.32.csv')
# df21=pd.read_csv('ALL020_2021-11-02_01.44.32.csv')
# df22=pd.read_csv('ALL021_2021-11-02_01.49.32.csv')
# df23=pd.read_csv('ALL022_2021-11-02_01.54.32.csv')
# df24=pd.read_csv('ALL023_2021-11-02_01.59.32.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL024_2021-11-02_02.04.32.csv")
# df26=pd.read_csv("ALL025_2021-11-02_02.09.32.csv")
# df27=pd.read_csv("ALL026_2021-11-02_02.14.32.csv")
# df28=pd.read_csv('ALL027_2021-11-02_02.19.32.csv')
# df29=pd.read_csv('ALL028_2021-11-02_02.24.32.csv')
# df30=pd.read_csv('ALL029_2021-11-02_02.29.32.csv')
# df31=pd.read_csv('ALL030_2021-11-02_02.34.32.csv')
# df32=pd.read_csv('ALL031_2021-11-02_02.39.32.csv')
# df33=pd.read_csv('ALL032_2021-11-02_02.44.32.csv')
# df34=pd.read_csv('ALL033_2021-11-02_02.49.32.csv')
# df35=pd.read_csv('ALL034_2021-11-02_02.54.32.csv')
# df36=pd.read_csv('ALL035_2021-11-02_02.59.32.csv')



# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_00_04_32-02_59_32.csv')

# merged_df1.dtypes


# #
# # part 2
# # concatentaion_HMD_3hours_03:04:32-05:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL036_2021-11-02_03.04.32.csv")
# df2=pd.read_csv("ALL037_2021-11-02_03.09.33.csv")
# df3=pd.read_csv("ALL038_2021-11-02_03.14.33.csv")
# df4=pd.read_csv('ALL039_2021-11-02_03.19.33.csv')
# df5=pd.read_csv('ALL040_2021-11-02_03.24.33.csv')
# df6=pd.read_csv('ALL041_2021-11-02_03.29.33.csv')
# df7=pd.read_csv('ALL042_2021-11-02_03.34.33.csv')
# df8=pd.read_csv('ALL043_2021-11-02_03.39.33.csv')
# df9=pd.read_csv('ALL044_2021-11-02_03.44.33.csv')
# df10=pd.read_csv('ALL045_2021-11-02_03.49.33.csv')
# df11=pd.read_csv('ALL046_2021-11-02_03.54.33.csv')
# df12=pd.read_csv('ALL047_2021-11-02_03.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL048_2021-11-02_04.04.33.csv")
# df14=pd.read_csv("ALL049_2021-11-02_04.09.33.csv")
# df15=pd.read_csv("ALL050_2021-11-02_04.14.33.csv")
# df16=pd.read_csv('ALL051_2021-11-02_04.19.33.csv')
# df17=pd.read_csv('ALL052_2021-11-02_04.24.33.csv')
# df18=pd.read_csv('ALL053_2021-11-02_04.29.33.csv')
# df19=pd.read_csv('ALL054_2021-11-02_04.34.33.csv')
# df20=pd.read_csv('ALL055_2021-11-02_04.39.33.csv')
# df21=pd.read_csv('ALL056_2021-11-02_04.44.33.csv')
# df22=pd.read_csv('ALL057_2021-11-02_04.49.33.csv')
# df23=pd.read_csv('ALL058_2021-11-02_04.54.33.csv')
# df24=pd.read_csv('ALL059_2021-11-02_04.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL060_2021-11-02_05.04.33.csv")
# df26=pd.read_csv("ALL061_2021-11-02_05.09.33.csv")
# df27=pd.read_csv("ALL062_2021-11-02_05.14.33.csv")
# df28=pd.read_csv('ALL063_2021-11-02_05.19.33.csv')
# df29=pd.read_csv('ALL064_2021-11-02_05.24.33.csv')
# df30=pd.read_csv('ALL065_2021-11-02_05.29.33.csv')
# df31=pd.read_csv('ALL066_2021-11-02_05.34.33.csv')
# df32=pd.read_csv('ALL067_2021-11-02_05.39.33.csv')
# df33=pd.read_csv('ALL068_2021-11-02_05.44.33.csv')
# df34=pd.read_csv('ALL069_2021-11-02_05.49.33.csv')
# df35=pd.read_csv('ALL070_2021-11-02_05.54.33.csv')
# df36=pd.read_csv('ALL071_2021-11-02_05.59.33.csv')



# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_03_04_32-05_59_32.csv')

# merged_df1.dtypes


# #
# # part 3
# # concatentaion_HMD_3hours_06:04:32-08:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL072_2021-11-02_06.04.33.csv")
# df2=pd.read_csv("ALL073_2021-11-02_06.09.33.csv")
# df3=pd.read_csv("ALL074_2021-11-02_06.14.33.csv")
# df4=pd.read_csv('ALL075_2021-11-02_06.19.33.csv')
# df5=pd.read_csv('ALL076_2021-11-02_06.24.33.csv')
# df6=pd.read_csv('ALL077_2021-11-02_06.29.33.csv')
# df7=pd.read_csv('ALL078_2021-11-02_06.34.33.csv')
# df8=pd.read_csv('ALL079_2021-11-02_06.39.33.csv')
# df9=pd.read_csv('ALL080_2021-11-02_06.44.33.csv')
# df10=pd.read_csv('ALL081_2021-11-02_06.49.33.csv')
# df11=pd.read_csv('ALL082_2021-11-02_06.54.33.csv')
# df12=pd.read_csv('ALL083_2021-11-02_06.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL084_2021-11-02_07.04.33.csv")
# df14=pd.read_csv("ALL085_2021-11-02_07.09.33.csv")
# df15=pd.read_csv("ALL086_2021-11-02_07.14.33.csv")
# df16=pd.read_csv('ALL087_2021-11-02_07.19.33.csv')
# df17=pd.read_csv('ALL088_2021-11-02_07.24.33.csv')
# df18=pd.read_csv('ALL089_2021-11-02_07.29.33.csv')
# df19=pd.read_csv('ALL090_2021-11-02_07.34.33.csv')
# df20=pd.read_csv('ALL091_2021-11-02_07.39.33.csv')
# df21=pd.read_csv('ALL092_2021-11-02_07.44.33.csv')
# df22=pd.read_csv('ALL093_2021-11-02_07.49.33.csv')
# df23=pd.read_csv('ALL094_2021-11-02_07.54.33.csv')
# df24=pd.read_csv('ALL095_2021-11-02_07.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL096_2021-11-02_08.04.33.csv")
# df26=pd.read_csv("ALL097_2021-11-02_08.09.33.csv")
# df27=pd.read_csv("ALL098_2021-11-02_08.14.33.csv")
# df28=pd.read_csv('ALL099_2021-11-02_08.19.33.csv')
# df29=pd.read_csv('ALL100_2021-11-02_08.24.33.csv')
# df30=pd.read_csv('ALL101_2021-11-02_08.29.33.csv')
# df31=pd.read_csv('ALL102_2021-11-02_08.34.33.csv')
# df32=pd.read_csv('ALL103_2021-11-02_08.39.33.csv')
# df33=pd.read_csv('ALL104_2021-11-02_08.44.33.csv')
# df34=pd.read_csv('ALL105_2021-11-02_08.49.33.csv')
# df35=pd.read_csv('ALL106_2021-11-02_08.54.33.csv')
# df36=pd.read_csv('ALL107_2021-11-02_08.59.33.csv')



# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_06_04_32-08_59_32.csv')

# merged_df1.dtypes


# #
# # part 4
# # concatentaion_HMD_3hours_09:04:32-11:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL108_2021-11-02_09.04.33.csv")
# df2=pd.read_csv("ALL109_2021-11-02_09.09.33.csv")
# df3=pd.read_csv("ALL110_2021-11-02_09.14.33.csv")
# df4=pd.read_csv('ALL111_2021-11-02_09.19.33.csv')
# df5=pd.read_csv('ALL112_2021-11-02_09.24.33.csv')
# df6=pd.read_csv('ALL113_2021-11-02_09.29.33.csv')
# df7=pd.read_csv('ALL114_2021-11-02_09.34.33.csv')
# df8=pd.read_csv('ALL115_2021-11-02_09.39.33.csv')
# df9=pd.read_csv('ALL116_2021-11-02_09.44.33.csv')
# df10=pd.read_csv('ALL117_2021-11-02_09.49.33.csv')
# df11=pd.read_csv('ALL118_2021-11-02_09.54.33.csv')
# df12=pd.read_csv('ALL119_2021-11-02_09.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL120_2021-11-02_10.04.33.csv")
# df14=pd.read_csv("ALL121_2021-11-02_10.09.33.csv")
# df15=pd.read_csv("ALL122_2021-11-02_10.14.33.csv")
# df16=pd.read_csv('ALL123_2021-11-02_10.19.33.csv')
# df17=pd.read_csv('ALL124_2021-11-02_10.24.33.csv')
# df18=pd.read_csv('ALL125_2021-11-02_10.29.33.csv')
# df19=pd.read_csv('ALL126_2021-11-02_10.34.33.csv')
# df20=pd.read_csv('ALL127_2021-11-02_10.39.33.csv')
# df21=pd.read_csv('ALL128_2021-11-02_10.44.33.csv')
# df22=pd.read_csv('ALL129_2021-11-02_10.49.33.csv')
# df23=pd.read_csv('ALL130_2021-11-02_10.54.33.csv')
# df24=pd.read_csv('ALL131_2021-11-02_10.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL132_2021-11-02_11.04.33.csv")
# df26=pd.read_csv("ALL133_2021-11-02_11.09.33.csv")
# df27=pd.read_csv("ALL134_2021-11-02_11.14.33.csv")
# df28=pd.read_csv('ALL135_2021-11-02_11.19.33.csv')
# df29=pd.read_csv('ALL136_2021-11-02_11.24.33.csv')
# df30=pd.read_csv('ALL137_2021-11-02_11.29.33.csv')
# df31=pd.read_csv('ALL138_2021-11-02_11.34.33.csv')
# df32=pd.read_csv('ALL139_2021-11-02_11.39.33.csv')
# df33=pd.read_csv('ALL140_2021-11-02_11.44.33.csv')
# df34=pd.read_csv('ALL141_2021-11-02_11.49.33.csv')
# df35=pd.read_csv('ALL142_2021-11-02_11.54.33.csv')
# df36=pd.read_csv('ALL143_2021-11-02_11.59.33.csv')



# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_09_04_32-11_59_32.csv')

# merged_df1.dtypes


# #
# # part 5
# # concatentaion_HMD_3hours_12:04:32-14:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL144_2021-11-02_12.04.33.csv")
# df2=pd.read_csv("ALL145_2021-11-02_12.09.33.csv")
# df3=pd.read_csv("ALL146_2021-11-02_12.14.33.csv")
# df4=pd.read_csv('ALL147_2021-11-02_12.19.33.csv')
# df5=pd.read_csv('ALL148_2021-11-02_12.24.33.csv')
# df6=pd.read_csv('ALL149_2021-11-02_12.29.33.csv')
# df7=pd.read_csv('ALL150_2021-11-02_12.34.33.csv')
# df8=pd.read_csv('ALL151_2021-11-02_12.39.33.csv')
# df9=pd.read_csv('ALL152_2021-11-02_12.44.33.csv')
# df10=pd.read_csv('ALL153_2021-11-02_12.49.33.csv')
# df11=pd.read_csv('ALL154_2021-11-02_12.54.33.csv')
# df12=pd.read_csv('ALL155_2021-11-02_12.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL156_2021-11-02_13.04.33.csv")
# df14=pd.read_csv("ALL157_2021-11-02_13.09.33.csv")
# df15=pd.read_csv("ALL158_2021-11-02_13.14.33.csv")
# df16=pd.read_csv('ALL159_2021-11-02_13.19.33.csv')
# df17=pd.read_csv('ALL160_2021-11-02_13.24.33.csv')
# df18=pd.read_csv('ALL161_2021-11-02_13.29.33.csv')
# df19=pd.read_csv('ALL162_2021-11-02_13.34.33.csv')
# df20=pd.read_csv('ALL163_2021-11-02_13.39.33.csv')
# df21=pd.read_csv('ALL164_2021-11-02_13.44.33.csv')
# df22=pd.read_csv('ALL165_2021-11-02_13.49.33.csv')
# df23=pd.read_csv('ALL166_2021-11-02_13.54.33.csv')
# df24=pd.read_csv('ALL167_2021-11-02_13.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL168_2021-11-02_14.04.33.csv")
# df26=pd.read_csv("ALL169_2021-11-02_14.09.33.csv")
# df27=pd.read_csv("ALL170_2021-11-02_14.14.33.csv")
# df28=pd.read_csv('ALL171_2021-11-02_14.19.33.csv')
# df29=pd.read_csv('ALL172_2021-11-02_14.24.33.csv')
# df30=pd.read_csv('ALL173_2021-11-02_14.29.33.csv')
# df31=pd.read_csv('ALL174_2021-11-02_14.34.33.csv')
# df32=pd.read_csv('ALL175_2021-11-02_14.39.33.csv')
# df33=pd.read_csv('ALL176_2021-11-02_14.44.33.csv')
# df34=pd.read_csv('ALL177_2021-11-02_14.49.33.csv')
# df35=pd.read_csv('ALL178_2021-11-02_14.54.33.csv')
# df36=pd.read_csv('ALL179_2021-11-02_14.59.33.csv')



# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data


# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_12_04_32-14_59_32.csv')

# merged_df1.dtypes


# #
# # part 6
# # concatentaion_HMD_3hours_15:04:32-17:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL180_2021-11-02_15.04.33.csv")
# df2=pd.read_csv("ALL181_2021-11-02_15.09.33.csv")
# df3=pd.read_csv("ALL182_2021-11-02_15.14.33.csv")
# df4=pd.read_csv('ALL183_2021-11-02_15.19.33.csv')
# df5=pd.read_csv('ALL184_2021-11-02_15.24.33.csv')
# df6=pd.read_csv('ALL185_2021-11-02_15.29.33.csv')
# df7=pd.read_csv('ALL186_2021-11-02_15.34.33.csv')
# df8=pd.read_csv('ALL187_2021-11-02_15.39.33.csv')
# df9=pd.read_csv('ALL188_2021-11-02_15.44.33.csv')
# df10=pd.read_csv('ALL189_2021-11-02_15.49.33.csv')
# df11=pd.read_csv('ALL190_2021-11-02_15.54.33.csv')
# df12=pd.read_csv('ALL191_2021-11-02_15.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL192_2021-11-02_16.04.33.csv")
# df14=pd.read_csv("ALL193_2021-11-02_16.09.33.csv")
# df15=pd.read_csv("ALL194_2021-11-02_16.14.33.csv")
# df16=pd.read_csv('ALL195_2021-11-02_16.19.33.csv')
# df17=pd.read_csv('ALL196_2021-11-02_16.24.33.csv')
# df18=pd.read_csv('ALL197_2021-11-02_16.29.33.csv')
# df19=pd.read_csv('ALL198_2021-11-02_16.34.33.csv')
# df20=pd.read_csv('ALL199_2021-11-02_16.39.33.csv')
# # df21=pd.read_csv('ALL200_2021-11-02_16.44.33.csv')
# df22=pd.read_csv('ALL201_2021-11-02_16.49.33.csv')
# df23=pd.read_csv('ALL202_2021-11-02_16.54.33.csv')
# df24=pd.read_csv('ALL203_2021-11-02_16.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL204_2021-11-02_17.04.33.csv")
# df26=pd.read_csv("ALL205_2021-11-02_17.09.33.csv")
# df27=pd.read_csv("ALL206_2021-11-02_17.14.33.csv")
# df28=pd.read_csv('ALL207_2021-11-02_17.19.33.csv')
# df29=pd.read_csv('ALL208_2021-11-02_17.24.33.csv')
# df30=pd.read_csv('ALL209_2021-11-02_17.29.33.csv')
# df31=pd.read_csv('ALL210_2021-11-02_17.34.33.csv')
# df32=pd.read_csv('ALL211_2021-11-02_17.39.33.csv')
# df33=pd.read_csv('ALL212_2021-11-02_17.44.33.csv')
# df34=pd.read_csv('ALL213_2021-11-02_17.49.33.csv')
# df35=pd.read_csv('ALL214_2021-11-02_17.54.33.csv')
# df36=pd.read_csv('ALL215_2021-11-02_17.59.33.csv')


# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# # df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_15_04_32-17_59_32.csv')

# merged_df1.dtypes


# #
# # part 7
# # concatentaion_HMD_3hours_18:04:32-20:59:32.csv
# #
# #














# #reading csv files for 1st hour
# df1=pd.read_csv("ALL216_2021-11-02_18.04.33.csv")
# df2=pd.read_csv("ALL217_2021-11-02_18.09.33.csv")
# df3=pd.read_csv("ALL218_2021-11-02_18.14.33.csv")
# df4=pd.read_csv('ALL219_2021-11-02_18.19.33.csv')
# df5=pd.read_csv('ALL220_2021-11-02_18.24.33.csv')
# df6=pd.read_csv('ALL221_2021-11-02_18.29.33.csv')
# df7=pd.read_csv('ALL222_2021-11-02_18.34.33.csv')
# df8=pd.read_csv('ALL223_2021-11-02_18.39.33.csv')
# df9=pd.read_csv('ALL224_2021-11-02_18.44.33.csv')
# df10=pd.read_csv('ALL225_2021-11-02_18.49.33.csv')
# df11=pd.read_csv('ALL226_2021-11-02_18.54.33.csv')
# df12=pd.read_csv('ALL227_2021-11-02_18.59.33.csv')

# #reading csv files for 2nd hour
# df13=pd.read_csv("ALL228_2021-11-02_19.04.33.csv")
# df14=pd.read_csv("ALL229_2021-11-02_19.09.33.csv")
# df15=pd.read_csv("ALL230_2021-11-02_19.14.33.csv")
# df16=pd.read_csv('ALL231_2021-11-02_19.19.33.csv')
# df17=pd.read_csv('ALL232_2021-11-02_19.24.33.csv')
# df18=pd.read_csv('ALL233_2021-11-02_19.29.33.csv')
# df19=pd.read_csv('ALL234_2021-11-02_19.34.33.csv')
# df20=pd.read_csv('ALL235_2021-11-02_19.39.33.csv')
# df21=pd.read_csv('ALL236_2021-11-02_19.44.33.csv')
# df22=pd.read_csv('ALL237_2021-11-02_19.49.33.csv')
# df23=pd.read_csv('ALL238_2021-11-02_19.54.33.csv')
# df24=pd.read_csv('ALL239_2021-11-02_19.59.33.csv')

# #reading csv files for 3rd hour
# df25=pd.read_csv("ALL240_2021-11-02_20.04.33.csv")
# df26=pd.read_csv("ALL241_2021-11-02_20.09.33.csv")
# df27=pd.read_csv("ALL242_2021-11-02_20.14.33.csv")
# df28=pd.read_csv('ALL243_2021-11-02_20.19.33.csv')
# df29=pd.read_csv('ALL244_2021-11-02_20.24.33.csv')
# df30=pd.read_csv('ALL245_2021-11-02_20.29.33.csv')
# df31=pd.read_csv('ALL246_2021-11-02_20.34.33.csv')
# df32=pd.read_csv('ALL247_2021-11-02_20.39.33.csv')
# df33=pd.read_csv('ALL248_2021-11-02_20.44.33.csv')
# df34=pd.read_csv('ALL249_2021-11-02_20.49.33.csv')
# df35=pd.read_csv('ALL250_2021-11-02_20.54.33.csv')
# df36=pd.read_csv('ALL251_2021-11-02_20.59.33.csv')


# #Defining a function for selecting only required columns, and removing rest
# def selectedcolumns(data):
#     data.columns=data.iloc[0]
#     data=data.iloc[2:,]
#     #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
#     data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
#     return data

# df1=selectedcolumns(df1)
# df2=selectedcolumns(df2)
# df3=selectedcolumns(df3)
# df4=selectedcolumns(df4)
# df5=selectedcolumns(df5)
# df6=selectedcolumns(df6)
# df7=selectedcolumns(df7)
# df8=selectedcolumns(df8)
# df9=selectedcolumns(df9)
# df10=selectedcolumns(df10)
# df11=selectedcolumns(df11)
# df12=selectedcolumns(df12)

# df13=selectedcolumns(df13)
# df14=selectedcolumns(df14)
# df15=selectedcolumns(df15)
# df16=selectedcolumns(df16)
# df17=selectedcolumns(df17)
# df18=selectedcolumns(df18)
# df19=selectedcolumns(df19)
# df20=selectedcolumns(df20)
# df21=selectedcolumns(df21)
# df22=selectedcolumns(df22)
# df23=selectedcolumns(df23)
# df24=selectedcolumns(df24)

# df25=selectedcolumns(df25)
# df26=selectedcolumns(df26)
# df27=selectedcolumns(df27)
# df28=selectedcolumns(df28)
# df29=selectedcolumns(df29)
# df30=selectedcolumns(df30)
# df31=selectedcolumns(df31)
# df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
# df34=selectedcolumns(df34)
# df35=selectedcolumns(df35)
# df36=selectedcolumns(df36)


# merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36], axis=0)

# merged_df1.describe()

# merged_df1.to_csv('concatentaion_HMD_3hours_18_04_32-20_59_32.csv')

# merged_df1.dtypes


# #
# # part 8
# # concatentaion_HMD_3hours_21:04:32-23:59:32.csv
# #
# #














#reading csv files for 1st hour
df1=pd.read_csv("ALL252_2021-11-02_21.04.33.csv")
df2=pd.read_csv("ALL253_2021-11-02_21.09.33.csv")
df3=pd.read_csv("ALL254_2021-11-02_21.14.33.csv")
df4=pd.read_csv('ALL255_2021-11-02_21.19.33.csv')
df5=pd.read_csv('ALL256_2021-11-02_21.24.33.csv')
df6=pd.read_csv('ALL257_2021-11-02_21.29.33.csv')
df7=pd.read_csv('ALL258_2021-11-02_21.34.33.csv')
df8=pd.read_csv('ALL259_2021-11-02_21.39.33.csv')
df9=pd.read_csv('ALL260_2021-11-02_21.44.33.csv')
df10=pd.read_csv('ALL261_2021-11-02_21.49.33.csv')
df11=pd.read_csv('ALL262_2021-11-02_21.54.33.csv')
df12=pd.read_csv('ALL263_2021-11-02_21.59.33.csv')

#reading csv files for 2nd hour
df13=pd.read_csv("ALL264_2021-11-02_22.04.33.csv")
df14=pd.read_csv("ALL265_2021-11-02_22.09.33.csv")
df15=pd.read_csv("ALL266_2021-11-02_22.14.33.csv")
df16=pd.read_csv('ALL267_2021-11-02_22.19.33.csv')
df17=pd.read_csv('ALL268_2021-11-02_22.24.33.csv')
df18=pd.read_csv('ALL269_2021-11-02_22.29.33.csv')
df19=pd.read_csv('ALL270_2021-11-02_22.34.33.csv')
df20=pd.read_csv('ALL271_2021-11-02_22.39.33.csv')
df21=pd.read_csv('ALL272_2021-11-02_22.44.33.csv')
df22=pd.read_csv('ALL273_2021-11-02_22.49.33.csv')
df23=pd.read_csv('ALL274_2021-11-02_22.54.33.csv')
df24=pd.read_csv('ALL275_2021-11-02_22.59.33.csv')

#reading csv files for 3rd hour
df25=pd.read_csv("ALL276_2021-11-02_23.04.33.csv")
df26=pd.read_csv("ALL277_2021-11-02_23.09.33.csv")
df27=pd.read_csv("ALL278_2021-11-02_23.14.33.csv")
df28=pd.read_csv('ALL279_2021-11-02_23.19.33.csv')
df29=pd.read_csv('ALL280_2021-11-02_23.24.33.csv')
df30=pd.read_csv('ALL281_2021-11-02_23.29.33.csv')
df31=pd.read_csv('ALL282_2021-11-02_23.34.33.csv')
df32=pd.read_csv('ALL283_2021-11-02_23.39.33.csv')
# df33=pd.read_csv('ALL284_2021-11-02_23.44.33.csv')
df34=pd.read_csv('ALL285_2021-11-02_23.49.33.csv')
df35=pd.read_csv('ALL286_2021-11-02_23.54.33.csv')
df36=pd.read_csv('ALL287_2021-11-02_23.59.33.csv')


#Defining a function for selecting only required columns, and removing rest
def selectedcolumns(data):
    data.columns=data.iloc[0]
    data=data.iloc[2:,]
    #data = data.rename(columns={"Billet Temp. 'D' strand": "Billet Temp. D strand"})
    data = data[['time', 'PR15B_HMD_IN', 'S15B_HMD_IN', 'PR15_B_HMD:DI01', 'H9_HMD', 'FBLB_HMDIN', 'FBLB_HMDOUT', 'PRWZ2B_HMD', 'PRLB_HMD', 'DI1.9/ S15C_CI_HMD', 'DI1.10/ FBLC_CI_HMDI', 'DI1.11/ FBLC_CI_HMDO', 'DI1.16/ H16C_CI_HMD', 'DI12.27/HMD_FS_C', 'DI12.25/HMD_FS_A', 'DI1.15/HMD_16_STRAND_A', 'DI12.30/HMD_19_STRAND_A', 'DI12.31/HMD20_STRAND_A', 'DI12.32/HMD23_STRAND_A', 'DI1.9/S15C_CI_HMD', 'DI1.7/H16C_CI_HMD_N', 'DI1.16/H16C_CI_HMD', 'S15C_HMDHPLS', 'S15C_HMDTPLS', 'DI1.10/FBLC_CI_HMDI', 'DI1.11/FBLC_CI_HMDO', 'MILLC_HMD_TEST', 'DI1.9/S15D_CI_HMD', 'DI1.10/FBLD_CI_HMDI', 'DI1.11/FBLD_CI_HMDO', 'DI1.14/H15D_CI_HMD', 'DI1.16/H16D_CI_HMD', 'S15D_HMDHPLS', 'S15D_HMDTPLS', 'DI12.27/HMD 9_F/S D']]
    return data

df1=selectedcolumns(df1)
df2=selectedcolumns(df2)
df3=selectedcolumns(df3)
df4=selectedcolumns(df4)
df5=selectedcolumns(df5)
df6=selectedcolumns(df6)
df7=selectedcolumns(df7)
df8=selectedcolumns(df8)
df9=selectedcolumns(df9)
df10=selectedcolumns(df10)
df11=selectedcolumns(df11)
df12=selectedcolumns(df12)

df13=selectedcolumns(df13)
df14=selectedcolumns(df14)
df15=selectedcolumns(df15)
df16=selectedcolumns(df16)
df17=selectedcolumns(df17)
df18=selectedcolumns(df18)
df19=selectedcolumns(df19)
df20=selectedcolumns(df20)
df21=selectedcolumns(df21)
df22=selectedcolumns(df22)
df23=selectedcolumns(df23)
df24=selectedcolumns(df24)

df25=selectedcolumns(df25)
df26=selectedcolumns(df26)
df27=selectedcolumns(df27)
df28=selectedcolumns(df28)
df29=selectedcolumns(df29)
df30=selectedcolumns(df30)
df31=selectedcolumns(df31)
df32=selectedcolumns(df32)
# df33=selectedcolumns(df33)
df34=selectedcolumns(df34)
df35=selectedcolumns(df35)
df36=selectedcolumns(df36)


merged_df1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df34,df35,df36], axis=0)

merged_df1.describe()

merged_df1.to_csv('concatentaion_HMD_3hours_21_04_32-23_59_32.csv')

merged_df1.dtypes
