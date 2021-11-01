import streamlit as st
import sqlite3


### Übersicht ###



#############
### INPUT ###
#############
st.text_input("Tourname")

col11, col12, col13  =st.columns([1,1,1])

Rider = col11.selectbox("Rider",("Josua", "Jan", "Sven", "Phillip") )
Tour_Typ = col12.selectbox("Typ", ("🚴‍♂️","🏃‍♂️","🚵‍♂️"))
Datum = col13.date_input("Datum")

col21, col22, col23 =st.columns([1,1,1])

Distanz = col21.number_input("KM")
Pace = col22.number_input("Ø Pace")
Hoehenmeter = col23.number_input("Höhenmeter")

clicked = st.button("Kette aufziehen")

################
### Database ###
################
conn = sqlite3.connect('bikechallenge_database.db')
print("Opened database successfully")

if clicked == True:
    sql = "INSERT INTO tracks (ID,Datum,Rider,Distanz,Pace_AVG,Höhenmeter,Typ) VALUES (?, ?, ?, ?, ?, ?, ?)"
    #"select exists(SELECT * from USERS where PASSWORD = ? AND USERNAME = ?)"
    args = (9,Datum,Rider,Distanz,Pace,Hoehenmeter,Tour_Typ)
    conn.execute(sql, args)

    conn.commit()
    print("Entry succesfully added")