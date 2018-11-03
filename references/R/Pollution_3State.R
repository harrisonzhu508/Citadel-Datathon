# Script to investigate pollution in worst states 

chem <- read.csv("/Users/BenjaminHillyard/Desktop/chemicals.csv")

# California 
cali_chem <- subset(chem, state == "California")
summary(cali_chem)
cali_chem_harm <- subset(cali_chem, contaminant_level == "Greater than MCL")
summary(cali_chem_harm)
with(cali_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, California", ylab = "Number of water systems", xlab = "Pollutants"))


# Florida 
flori_chem <- subset(chem, state == "Florida")
summary(flori_chem)
flori_chem_harm <- subset(flori_chem, contaminant_level == "Greater than MCL")
summary(flori_chem_harm)
with(flori_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, Florida", ylab = "Number of water systems", xlab = "Pollutants"))

# Connecticut
conni_chem <- subset(chem, state == "Connecticut")
summary(conni_chem)
conni_chem_harm <- subset(conni_chem, contaminant_level == "Greater than MCL")
summary(conni_chem_harm)
with(conni_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, Connecticut", ylab = "Number of water systems", xlab = "Pollutants"))


with(conni_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, Connecticut", ylab = "Number of water systems", xlab = "Pollutants"))
with(flori_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, Florida", ylab = "Number of water systems", xlab = "Pollutants"))
with(cali_chem_harm, plot(chemical_species, main = "Number of water systems contaminated by above mean pollutant levels, California", ylab = "Number of water systems", xlab = "Pollutants"))
par(mfrow=c(3,1)) 


