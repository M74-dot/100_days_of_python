import pandas

student_dict = {
    "students": ["Lily", "Mili", "Chily"],
    "score": [56, 76, 78]
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# loop through dataframe
for (key,value) in student_df.items():
    # print(key)
    pass

# loop through row of dataframe
for (index, row) in student_df.iterrows():
    # print(row.students)
    pass