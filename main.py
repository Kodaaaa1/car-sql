from database import connect, create_tables

def add_vehicle():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    placa = input("Placa: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO vehicles (marca, modelo, ano, placa)
        VALUES (?, ?, ?, ?)
    """, (marca, modelo, ano, placa))

    conn.commit()
    conn.close()
    print("✅ Veículo cadastrado!")

def list_vehicles():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()

    for v in vehicles:
        print(v)

    conn.close()

def add_maintenance():
    vehicle_id = input("ID do veículo: ")
    tipo = input("Tipo (óleo, freio...): ")
    descricao = input("Descrição: ")
    data = input("Data: ")
    km = input("KM: ")
    custo = input("Custo: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO maintenance (vehicle_id, tipo, descricao, data, km, custo)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (vehicle_id, tipo, descricao, data, km, custo))

    conn.commit()
    conn.close()
    print("🔧 Manutenção registrada!")

def list_maintenance():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT v.modelo, m.tipo, m.data, m.custo
        FROM maintenance m
        JOIN vehicles v ON m.vehicle_id = v.id
    """)

    data = cursor.fetchall()

    for d in data:
        print(d)

    conn.close()

def menu():
    create_tables()

    while True:
        print("\n=== SISTEMA DE MANUTENÇÃO ===")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Registrar manutenção")
        print("4 - Listar manutenções")
        print("0 - Sair")

        option = input("Escolha: ")

        if option == "1":
            add_vehicle()
        elif option == "2":
            list_vehicles()
        elif option == "3":
            add_maintenance()
        elif option == "4":
            list_maintenance()
        elif option == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
