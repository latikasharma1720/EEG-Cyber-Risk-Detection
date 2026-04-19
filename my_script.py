import pandas as pd

biometric_file = "001A/001A_task2_biometrics.csv"
biometric_data = pd.read_csv(biometric_file)

biometric_data["stim_number"] = 0

stim_counter = 0
previous_value = 0

for i in range(len(biometric_data)):
    current_value = biometric_data.loc[i, "stimulus"]

    if current_value == 5 and previous_value != 5:
        stim_counter += 1

    if current_value == 5:
        biometric_data.loc[i, "stim_number"] = stim_counter

    previous_value = current_value

print("First 20 rows where stimulus = 5:")
print(biometric_data[biometric_data["stimulus"] == 5].head(20))

print("\nUnique stim_number values:")
print(biometric_data["stim_number"].unique())

print("\nStim_number counts:")
print(biometric_data["stim_number"].value_counts().sort_index())

print("\nLast 20 rows where stim_number > 0:")
print(biometric_data[biometric_data["stim_number"] > 0][["stimulus", "stim_number"]].tail(20))

print("\nTotal stimuli detected:", stim_counter)

biometric_data.to_csv("001A/001A_task2_biometrics_with_stim_number.csv", index=False)