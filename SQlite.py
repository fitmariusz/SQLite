def query_add_profile(cur, index, name, width, height, colors):
    cur.execute(
        f"INSERT INTO profiles VALUES('{index}', '{name}', {width}, {height}, '{colors}')"
    )
    cur.connection.commit()


__name__ = "__main__"
pass
