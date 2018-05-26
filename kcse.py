import csv
import numpy as np 
import operator

def countAs():
    # reading the kcse exam sheet
    with open('KCSE_Exam_Results_2006_to_2010.csv', 'rt') as f:
        rows = csv.DictReader(f)
        schools_array = []
        for row in rows:
            grade_column_data = row['Grade attained']
            school_names_column_data = row['School Name']
            if grade_column_data == 'A':
                # append all schools with A's in the schools array
                schools_array.append(school_names_column_data)
                
                # create a numpy array as numpy is the best for working with arrays
                all_school_with_as =  np.array(schools_array)
        
        # unique list of all schools with a, the index of this schools, the unique count of As for this schools
        schools_array, school_index, as_count = np.unique(all_school_with_as, return_index=True, return_counts = True)
        
        # array of the schools with As
        schools_with_as = all_school_with_as[school_index]

        # create a dictionary to store schools and their number of As
        key, value = schools_with_as, as_count
        school_dict = dict(zip(key, value))

        # sort the schools so that the one with the most As appear first
        sorted_schools = sorted(school_dict.items(), key = operator.itemgetter(1), reverse=True)

        # print the sorted dictionary
        print(sorted_schools)

        # save the dictionary in a file
        with open('schools_with_as_kcse.txt', 'w') as file:
            count = 0
            for school in sorted_schools:
                count = count + 1
                file.write(str(count) + '  ' + str(school[0]) + "\t" + str(school[1]) +"\n")

countAs()

