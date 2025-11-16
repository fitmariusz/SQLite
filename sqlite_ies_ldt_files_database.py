import sqlite3

Sqlite_db = "ies_ldt_files.db"


def create_connection(Sqlite_db):
    conn = None
    try:
        conn = sqlite3.connect(Sqlite_db)
    except sqlite3.Error as e:
        print(e)
    return conn


def table_exists(conn, table_name):
    """Check if table exists in database"""
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    )
    return cursor.fetchone() is not None


def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Check if profiles table exists
        if table_exists(conn, "profiles") == False:
            print("Creating table 'profiles'...")
            sql_create_profiles_table = """CREATE TABLE profiles (
                                                profile_index_sap text NOT NULL,
                                                profile_name text NOT NULL,
                                                width float,
                                                hight float,
                                                colors text
                                            );"""
            cursor.execute(sql_create_profiles_table)
            print("Table 'profiles' created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    # try:
    #     sql_create_covers_table = """ CREATE TABLE IF NOT EXISTS covers (
    #                                         cover_index_sap integer NOT NULL PRIMARY KEY,
    #                                         cover_name text NOT NULL,
    #                                         material text,
    #                                         cover_type text,
    #                                         light_transmittance float,
    #                                     ) """
    #     cursor = conn.cursor()
    #     cursor.execute(sql_create_covers_table)
    # except sqlite3.Error as e:
    #     print(e)
    # try:
    #     sql_create_tapes_table = """ CREATE TABLE IF NOT EXISTS tapes (
    #                                         tape_index_sap integer NOT NULL PRIMARY KEY,
    #                                         tape_name text NOT NULL,
    #                                         tape_temperaturec text,
    #                                         tape_eifficiency float,
    #                                         tape_luminance integer,
    #                                         type_control text,
    #                                         voltage float,
    #                                         current float,
    #                                         power float,
    #                                         width float,
    #                                         height float,
    #                                         ) """
    #     cursor = conn.cursor()
    #     cursor.execute(sql_create_tapes_table)
    # except sqlite3.Error as e:
    #     print(e)


def add_profile(cur):
    print("\033cAdding profile:")
    index = input("Index profile in SAP: ")
    name = input("Profile name: ")
    width = input("Width (mm):")
    height = input("Height (mm):")
    colors = input("Colors (RAL): ")
    cur.execute(
        f"INSERT INTO profiles VALUES('{index}', '{name}', {width}, {height}, '{colors}')"
    )
    # cur.execute(f"INSERT INTO profiles VALUES('s', 'rffre', 1.2, 2.2, 'fsfse')")
    cur.connection.commit()


def view_menu(cur):
    choice = "0"
    while choice != "7":
        print("\033cView Profiles - please select for :")
        print("1. All Profiles")
        print("2. By Index (Not implemented)")
        print("3. By Name (Not implemented)")
        print("4. By Width (Not implemented)")
        print("5. By Height (Not implemented)")
        print("6. By Colors (Not implemented)")
        print("7. Return to Main Menu")
        choice = input("Select an option: ")
        match choice:
            case "1":
                view_all_profiles(cur)
            case "2":
                view_profiles_by_index(cur)
            case "3":
                view_profiles_by_name(cur)
            case "4":
                view_profiles_by_width(cur)
            case "5":
                view_profiles_by_height(cur)
            case "6":
                view_profiles_by_colors(cur)
            case "7":
                return
            case _:
                print("Option not implemented yet.")


def view_all_profiles(cur):
    print("\033cAll Profiles:")
    cur.execute("SELECT * FROM profiles")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    input("Press Enter to return to the main menu...")


def view_profiles_by_index(cur):
    index = input("\033cEnter profile index to search: ")
    cur.execute(f"SELECT * FROM profiles WHERE profile_index_sap='{index}'")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with index '{index}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with index '{index}':")
        for row in rows:
            print("\033[92m" + str(row) + "\033[0m")
        input("Press Enter to return to the view menu...")


def view_profiles_by_name(cur):
    name = input("\033cEnter profile name to search: ")
    cur.execute(f"SELECT * FROM profiles WHERE profile_name='{name}'")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with name '{name}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with name '{name}':")
        for row in rows:
            print("\033[92m" + str(row) + "\033[0m")
        input("Press Enter to return to the view menu...")


def view_profiles_by_width(cur):
    width = input("\033cEnter profile width to search: ")
    cur.execute(f"SELECT * FROM profiles WHERE width={width}")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with width '{width}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with width '{width}':")
        for row in rows:
            print("\033[92m" + str(row) + "\033[0m")
        input("Press Enter to return to the view menu...")


def view_profiles_by_height(cur):
    height = input("\033cEnter profile height to search: ")
    cur.execute(f"SELECT * FROM profiles WHERE hight={height}")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with height '{height}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with height '{height}':")
        for row in rows:
            print("\033[92m" + str(row) + "\033[0m")
        input("Press Enter to return to the view menu...")


def view_profiles_by_colors(cur):
    colors = input("\033cEnter profile colors to search: ")
    cur.execute(f"SELECT * FROM profiles WHERE colors='{colors}'")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with colors '{colors}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with colors '{colors}':")
        for row in rows:
            print("\033[92m" + str(row) + "\033[0m")
        input("Press Enter to return to the view menu...")


def update_profile(cur):
    print("\033cUpdate Profile selected")
    view_all_profiles(cur)
    index = input("Enter the profile index of the profile you want to update: ")
    cur.execute(f"SELECT * FROM profiles WHERE profile_index_sap='{index}'")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with index '{index}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with index '{index}':")
        for row in rows:
            print("\033[93m" + str(row) + "\033[0m")
    print("Enter new values (leave blank to keep current value):")
    new_name = input(f"New Profile name ({rows[0][1]}): ")
    if new_name == "":
        new_name = rows[0][1]
    new_width = input(f"New Width (mm) ({rows[0][2]}): ")
    if new_width == "":
        new_width = rows[0][2]
    new_height = input(f"New Height (mm) ({rows[0][3]}): ")
    if new_height == "":
        new_height = rows[0][3]
    new_colors = input(f"New Colors (RAL) ({rows[0][4]}): ")
    if new_colors == "":
        new_colors = rows[0][4]
    cur.execute(
        f"UPDATE profiles SET profile_name='{new_name}', width={new_width}, hight={new_height}, colors='{new_colors}' WHERE profile_index_sap='{index}'"
    )
    cur.connection.commit()


def delete_profile(cur):
    print("\033cDelete Profile selected")
    view_all_profiles(cur)
    index = input("Enter the profile index of the profile you want to delete: ")
    cur.execute(f"SELECT * FROM profiles WHERE profile_index_sap='{index}'")
    rows = cur.fetchall()
    if rows == []:
        print(f"\033c\033[91mNo profiles found with index '{index}'.\033[0m")
        input("Press Enter to return to the view menu...")
        return
    else:
        print(f"\033cProfiles with index '{index}':")
        for row in rows:
            print("\033[93m" + str(row) + "\033[0m")
    confirm = input(
        f"Are you sure you want to delete profile with index '{index}'? (y/n): "
    )
    if confirm.lower() == "y":
        cur.execute(f"DELETE FROM profiles WHERE profile_index_sap='{index}'")
        cur.connection.commit()
        print(f"Profile with index '{index}' has been deleted.")
    else:
        print("Deletion cancelled.")


def menu():
    print("\033cMain Menu:")
    print("1. Add Profile")
    print("2. View Profiles")
    print("3. Update Profile")
    print("4. Delete Profile")
    print("5. Exit")
    choice = input("Select an option: ")
    return choice


def main():
    conn = create_connection(Sqlite_db)
    cur = conn.cursor()
    if conn is not None:
        create_tables(conn)
    else:
        print("Error! cannot create the database connection.")
    choice = "0"
    while choice != "5":
        choice = menu()
        match choice:
            case "1":
                add_profile(cur)
            case "2":
                view_menu(cur)
            case "3":
                update_profile(cur)
            case "4":
                delete_profile(cur)
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

    if conn:
        conn.close()


if __name__ == "__main__":
    main()
