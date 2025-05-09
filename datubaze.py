import sqlite3


class kommanda():

    def __init__(self,nosaukums,kapteina_steam_nosaukums, kapteina_vards, kapteina_uzvards, speletaja_1_steam_nosaukums, speletaja_1_vards, speletaja_1_uzvards, speletaja_2_steam_nosaukums, speletaja_2_vards, speletaja_2_uzvards, speletaja_3_steam_nosaukums, speletaja_3_vards, speletaja_3_uzvards, speletaja_4_steam_nosaukums, speletaja_4_vards, speletaja_4_uzvards, turnira_nosaukums):
        self.nosaukums = nosaukums

        self.kaptaina_id = kapteina_steam_nosaukums
        self.kapt_vards = kapteina_vards
        self.kapt_uzvards = kapteina_uzvards

        self.spl_1_id = speletaja_1_steam_nosaukums
        self.spl_1_vards = speletaja_1_vards
        self.spl_1_uzvards = speletaja_1_uzvards

        self.spl_2_id = speletaja_2_steam_nosaukums
        self.spl_2_vards = speletaja_2_vards
        self.spl_2_uzvards = speletaja_2_uzvards

        self.spl_3_id = speletaja_3_steam_nosaukums
        self.spl_3_vards = speletaja_3_vards
        self.spl_3_uzvards = speletaja_3_uzvards

        self.spl_4_id = speletaja_4_steam_nosaukums
        self.spl_4_vards = speletaja_4_vards
        self.spl_4_uzvards = speletaja_4_uzvards

        self.trn_nosaukums = turnira_nosaukums

    def get_nosaukums(self):
        return self.nosaukums
    
    def get_speletaji(self):
        return [self.kaptaina_id,
        self.kapt_vards ,
        self.kapt_uzvards,

        self.spl_1_id,
        self.spl_1_vards,
        self.spl_1_uzvards,

        self.spl_2_id,
        self.spl_2_vards,
        self.spl_2_uzvards,

        self.spl_3_id,
        self.spl_3_vards,
        self.spl_3_uzvards,

        self.spl_4_id,
        self.spl_4_vards,
        self.spl_4_uzvards
]

    def __str__(self):
        return str(self.nosaukums)
    
    def get_all(self):
        return [
                self.nosaukums,

                self.kaptaina_id,
                self.kapt_vards ,
                self.kapt_uzvards,

                self.spl_1_id,
                self.spl_1_vards,
                self.spl_1_uzvards,

                self.spl_2_id,
                self.spl_2_vards,
                self.spl_2_uzvards,

                self.spl_3_id,
                self.spl_3_vards,
                self.spl_3_uzvards,

                self.spl_4_id,
                self.spl_4_vards,
                self.spl_4_uzvards,

                self.trn_nosaukums
                ]


class tabula:

    def __init__(self, datu_links, turnira_nosaukums):

        self.trn_nosaukums = turnira_nosaukums
        self.conn = sqlite3.connect(datu_links)

        self.conn.execute("""CREATE TABLE IF NOT EXISTS speletaji(
                id INTEGER,
                vards TEXT,
                uzvards TEXT,
                steam_vards TEXT,
                kommandas_id INTEGER,
                PRIMARY KEY("id"),
                FOREIGN KEY (kommandas_id) REFERENCES kommandas (id)
                ) """)

        self.conn.execute("""CREATE TABLE IF NOT EXISTS kommandas(
                id INTEGER,
                nosaukums TEXT,
                kapteina_steam_vards TEXT,
                turnirs_id TEXT,
                PRIMARY KEY("id"),
                FOREIGN KEY (turnirs_id) REFERENCES turniri (id)
                )""")


        self.conn.execute("""CREATE TABLE IF NOT EXISTS turnirs(
                id INTEGER,
                nosaukums TEXT,
                pirma_vieta TEXT,
                otra_vieta TEXT,
                tresa_vieta TEXT,
                PRIMARY KEY("id")
                )""")
        
        cursor = self.conn.execute("""SELECT
        CASE
        WHEN EXISTS(SELECT nosaukums FROM turnirs WHERE nosaukums = ?) THEN 'Exists'
        ELSE 'Not_exists'
        END;""",(turnira_nosaukums,))
        paties = cursor.fetchone()

        if paties[0] == "Not_exists":
            self.conn.execute("INSERT INTO turnirs (nosaukums) VALUES (?)",(turnira_nosaukums,))
            self.conn.commit()
        

        turnira_id =self.conn.execute(f"SELECT id FROM turnirs WHERE nosaukums = ?",(turnira_nosaukums,))
        turnira_id_pag = turnira_id.fetchall()
        self.trn_id = turnira_id_pag[0][0]

    def ierakstit_kommandu(self, kommanda_viss):

        self.conn.execute("INSERT INTO kommandas (nosaukums, kapteina_steam_vards, turnirs_id) VALUES (?,?,?)",(kommanda_viss[0],kommanda_viss[1],self.trn_id))
        cursor = self.conn.execute("SELECT id FROM kommandas WHERE nosaukums = ?",(kommanda_viss[0],))
        kmd_pagaidu = cursor.fetchone()
        kommandas_id = kmd_pagaidu[0]

        self.conn.execute("INSERT INTO speletaji (vards, uzvards, steam_vards, kommandas_id) VALUES (?,?,?,?)",(kommanda_viss[2],kommanda_viss[3],kommanda_viss[1],kommandas_id))
        self.conn.execute("INSERT INTO speletaji (vards, uzvards, steam_vards, kommandas_id) VALUES (?,?,?,?)",(kommanda_viss[5],kommanda_viss[6],kommanda_viss[4],kommandas_id))
        self.conn.execute("INSERT INTO speletaji (vards, uzvards, steam_vards, kommandas_id) VALUES (?,?,?,?)",(kommanda_viss[8],kommanda_viss[9],kommanda_viss[7],kommandas_id))
        self.conn.execute("INSERT INTO speletaji (vards, uzvards, steam_vards, kommandas_id) VALUES (?,?,?,?)",(kommanda_viss[11],kommanda_viss[12],kommanda_viss[10],kommandas_id))
        self.conn.execute("INSERT INTO speletaji (vards, uzvards, steam_vards, kommandas_id) VALUES (?,?,?,?)",(kommanda_viss[14],kommanda_viss[15],kommanda_viss[13],kommandas_id))

        self.conn.commit()

    def izvadit_dalibniekus(self):
        dalibnieki = self.conn.execute("SELECT * FROM kommandas WHERE turnirs_id = ?",(self.trn_id,))
        cursor = dalibnieki.fetchall()
        return cursor[0]
    
def main():
#     kommanda1 = kommanda("Gurķīši",1111,"Kristaps","Rūtainis",2222,"Mārtiņš","Zaķis",3333,"Evards","Gleizds",4444,"Kristijāns","Ligeris",5555,"Jānis","Kazerovskis","Milzu turnīrs")
#     print(kommanda1.get_all())

    turnirs_1 = tabula("milzu_turnirs.db","Milzu turnīrs")
#     #turnirs_1.ierakstit_kommandu(kommanda1.get_all())
#     print(turnirs_1.izvadit_dalibniekus())

if __name__=="__main__":
    main()