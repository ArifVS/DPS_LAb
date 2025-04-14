import pandas as pd

# Sample data (Original)c
data = {
    'Name': ['Arjun Mehta', 'Simran Kaur', 'Rajesh Iyer', 'Pooja Nair', 'Manoj Deshmukh', 'Swati Joshi'],
    'Age': [29, 35, 42, 26, 38, 31],  # Ages to be categorized
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Blood Group': ['B+', 'O-', 'A+', 'AB+', 'B-', 'O+'],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad'],
    'Pincode': ['110045', '400076', '560078', '700032', '600054', '500072'],  # Original pincodes
    'Email': ['arjun.mehta@hotmail.com', 'simran.kaur@gmail.com', 'rajesh.iyer@gmail.com',
              'pooja.nair@yahoo.com', 'manoj.deshmukh@gmail.com', 'swati.joshi@gmail.com'],  # Original emails
    'Salary': [45000, 55000, 60000, 40000, 70000, 65000],
    'Disease': ['None', 'Asthma', 'None', 'None', 'Hypertension', 'None']
}

df = pd.DataFrame(data)

print("##Before anonymization##")
print(df)


age_bins = [20, 30, 40, 50, 60]
age_labels = ['20-30', '30-40', '40-50', '50+']


df['Age'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

df['Pincode'] = df['Pincode'].apply(lambda x: x[:-2] + 'XX')



def mask_email(email):
    username, domain = email.split('@')
    return username + '@*.com'

df['Email'] = df['Email'].apply(mask_email)

print("##After anonymization##")
print(df)
