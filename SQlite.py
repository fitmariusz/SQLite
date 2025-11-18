def query_add_profile(cur, index, name, width, height, colors):
    cur.execute(
        f"INSERT INTO profiles VALUES('{index}', '{name}', {width}, {height}, '{colors}')"
    )
    cur.connection.commit()


def query_profiles_by_index(cur, index):
    cur.execute(f"SELECT * FROM profiles WHERE profile_index_sap='{index}'")
    rows = cur.fetchall()
    return rows


def query_profiles_by_name(cur, name):
    cur.execute(f"SELECT * FROM profiles WHERE profile_name='{name}'")
    rows = cur.fetchall()
    return rows


def query_profiles_by_width(cur, width):
    cur.execute(f"SELECT * FROM profiles WHERE width={width}")
    rows = cur.fetchall()
    return rows


def query_profiles_by_height(cur, height):
    cur.execute(f"SELECT * FROM profiles WHERE hight={height}")
    rows = cur.fetchall()
    return rows


def query_profiles_by_colors(cur, colors):
    cur.execute(f"SELECT * FROM profiles WHERE colors='{colors}'")
    rows = cur.fetchall()
    return rows


def query_update_profile(cur, index, new_name, new_width, new_height, new_colors):
    cur.execute(
        f"UPDATE profiles SET profile_name='{new_name}', width={new_width}, hight={new_height}, colors='{new_colors}' WHERE profile_index_sap='{index}'"
    )
    cur.connection.commit()


def query_delete_profile(cur, index):
    cur.execute(f"DELETE FROM profiles WHERE profile_index_sap='{index}'")
    cur.connection.commit()


__name__ = "__main__"
pass
