import streamlit as st
from io import StringIO 
import pandas as pd 
from sklearn.model_selection import train_test_split
import pickle
model = pickle.load(open("model.sav", "rb"))
from sklearn.preprocessing import MinMaxScaler


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    

    # To read file as string:
    string_data = stringio.read()
    

    # Can be used wherever a "file-like" object is accepted:
    df1 = pd.read_csv(uploaded_file)
    print(df1.head())
    st.write(df1)
    
    


## code body 
    ## Preprocessing
    df1.drop(columns =[ 'Unnamed: 0'], inplace = True)
    df1.Churn = df1.Churn.map({'Yes': 1, 'No': 0}).astype(int)
    catCols = ["gender","Partner","Dependents","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies", "Contract","PaperlessBilling","PaymentMethod"]
    numCols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df_F = pd.get_dummies(df1, columns=catCols)
    scaler = MinMaxScaler()
    df_F[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(df_F[['tenure', 'MonthlyCharges', 'TotalCharges']])
    X = df_F.drop(['Churn','customerID'],axis=1)
    y = df_F.Churn   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=56)


    df_F['Churn_Probability'] = model.predict_proba(df_F[X_train.columns])[:,1]
    df_P = df_F[['customerID', 'Churn_Probability']].head(10)

    
    df = pd.merge(df1, df_P, how = 'left', on = ['customerID'])
    
## 
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
    st.write(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
    )