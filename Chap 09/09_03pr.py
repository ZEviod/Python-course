for i in range (2,21):
    with open (f"tables(09_03pr k liye)/multiplication_table_of_{i}", 'w') as f:
        for j in range (1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write("\n")
