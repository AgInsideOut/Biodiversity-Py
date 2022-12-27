import pandas as pd
from matplotlib import pyplot as plt
import os

#Change Folder Directory Path AND UNCOMMENT IT
#os.chdir(r'/Users/User/Folder_Directory_Path')

species = pd.read_csv('species_info.csv')

#Create a new DataFrame called protection_counts, which is sorted by scientific_name
species.scientific_name.nunique()
species.category.unique()
species.conservation_status.unique()

species.groupby('conservation_status').scientific_name.nunique().reset_index()

species.fillna('No Intervention', inplace=True)

protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

#Create a bar chart
#Start by creating a wide figure with figsize = (10,4)
plt.figure(figsize=(10, 4))

#Create an axes objected called ax using plt.subplot
ax = plt.subplot()

#Create a bar chart whose heights are equal to the scientific_name column of protection_counts
plt.bar(range(len(protection_counts)),protection_counts.scientific_name.values)

#Create an x-tick for each of the bars.
#Label each x-tick with the label from conservation_status in protection_counts.
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)

#Label the y-axis Number of Species.
plt.ylabel("Number of Species")

#Title the graph Conservation Status by Species
plt.title("Conservation Status by Species")
labels = [e.get_text() for e in ax.get_xticklabels()]

#Plot the graph using plt.show()
plt.show()