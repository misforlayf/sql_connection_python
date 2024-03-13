




DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-76NBGCK\SQLEXPRESS'
DATABASE_NAME = 'trial_database'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""