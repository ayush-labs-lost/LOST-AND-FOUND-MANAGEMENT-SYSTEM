loim = {
    101: {
        "name": "Earbuds",
        "category": "Electronics",
        "location": "Library",
        "date": "22092026",
        "person": "Rahul"
    },
    102: {
        "name": "phone charger",
        "category": "Electronic parts",
        "location": "Block A",
        "date": "21092026",
        "person": "Aman"
    }
}
fodim = {
    201: {
        "name": "phone charger",
        "category": "Electronic parts",
        "location": "Block B",
        "date": "22092026",
        "person": "Rohit"
    }
}
cldim = {}
def load_data():
    global loim
    global fodim
    global cldim
    try:
        with open("data.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if data[0] == "LOST":
                    id = int(data[1])
                    loim[id] = {
                        "name": data[2],
                        "category": data[3],
                        "location": data[4],
                        "date": data[5],
                        "person": data[6]
                    }
                elif data[0] == "FOUND":
                    id = int(data[1])
                    fodim[id] = {
                        "name": data[2],
                        "category": data[3],
                        "location": data[4],
                        "date": data[5],
                        "person": data[6]
                    }
                elif data[0] == "CLAIMED":
                    id = int(data[1])
                    cldim[id] = {
                        "name": data[2],
                        "category": data[3],
                        "location": data[4],
                        "date": data[5],
                        "person": data[6],
                        "claimed_by": data[7]
                    }
        print("\nData loaded successfully")
    except FileNotFoundError:
        print("\nNo saved data found. Starting with default data.")
def replosm():
    print("\n" + "=" * 45)
    print("           REPORT LOST ITEM")
    print("=" * 45)
    itemname = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location where it was lost: ")
    date = input("Enter date (DDMMYYYY): ")
    person = input("Enter your name: ")
    if loim:
        itemid = max(loim.keys()) + 1
    else:
        itemid = 101
    loim[itemid] = {
        "name": itemname,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\nLost item reported successfully")
    print("Your Item ID is:", itemid)
def reportfounditem():
    print("\n" + "=" * 45)
    print("           REPORT FOUND ITEM")
    print("=" * 45)
    itemname = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter the location where it was found: ")
    date = input("Enter date (DD-MM-YYYY): ")
    person = input("Enter your name: ")
    if fodim:
        itemid = max(fodim.keys()) + 1
    else:
        itemid = 201
    fodim[itemid] = {
        "name": itemname,
        "category": category,
        "location": location,
        "date": date,
        "person": person
    }
    print("\nFound item reported successfully")
    print("Your Item ID is:", itemid)
def searchitem():
    print("\n" + "=" * 45)
    print("              SEARCH ITEM")
    print("=" * 45)
    keyword = input("Enter item name to search: ").lower()
    found = False
    for item_id, item in loim.items():
        if keyword in item["name"].lower():
            print("\n--- LOST ITEM FOUND ---")
            print("Item ID    :", item_id)
            print("Item Name  :", item["name"])
            print("Category   :", item["category"])
            print("Location   :", item["location"])
            print("Date       :", item["date"])
            print("Reported By:", item["person"])
            found = True
    for item_id, item in fodim.items():
        if keyword in item["name"].lower():
            print("\n--- FOUND ITEM ---")
            print("Item ID   :", item_id)
            print("Item Name :", item["name"])
            print("Category  :", item["category"])
            print("Location  :", item["location"])
            print("Date      :", item["date"])
            print("Found By  :", item["person"])
            found = True
    if not found:
        print("\nNo matching item found.")
def vwltit():
    print("\n" + "=" * 80)
    print("                         LOST ITEMS")
    print("=" * 80)
    if not loim:
        print("No lost items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in loim.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def vwfdit():
    print("\n" + "=" * 80)
    print("                         FOUND ITEMS")
    print("=" * 80)
    if not fodim:
        print("No found items reported.")
        return
    print(f"{'ID':<8}{'ITEM':<25}{'CATEGORY':<18}{'LOCATION':<20}")
    print("-" * 80)
    for item_id, item in fodim.items():
        print(
            f"{item_id:<8}"
            f"{item['name']:<25}"
            f"{item['category']:<18}"
            f"{item['location']:<20}"
        )
def clmitm():
    print("\n" + "=" * 45)
    print("           CLAIM / RECOVER ITEM")
    print("=" * 45)
    try:
        i_id = int(input("Enter found item ID: "))
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return
    if i_id not in fodim:
        print("\nNo found item with this ID.")
        return
    item = fodim[i_id]
    print("\nItem Details")
    print("-" * 30)
    print("Item Name :", item["name"])
    print("Category  :", item["category"])
    print("Location  :", item["location"])
    print("Date      :", item["date"])
    print("Found By  :", item["person"])
    clmnt = input("\nEnter claimant name: ")
    item["claimed_by"] = clmnt
    cldim[i_id] = item
    del fodim[i_id]
    print("\nItem claimed successfully")
    print("Claimed By:", clmnt)
def remits():
    print("\n" + "=" * 45)
    print("              REMOVE ITEM")
    print("=" * 45)
    try:
        it_id = int(input("Enter Item ID to remove: "))
    except ValueError:
        print("\nInvalid ID. Please enter a number.")
        return
    if it_id in loim:
        del loim[it_id]
        print("\nLost item removed successfully")
    elif it_id in fodim:
        del fodim[it_id]
        print("\nFound item removed successfully")
    elif it_id in cldim:
        del cldim[it_id]
        print("\nClaimed item removed successfully")
    else:
        print("\nNo item found with this ID.")
def stats():
    print("\n" + "=" * 45)
    print("              STATISTICS")
    print("=" * 45)
    lt_c = len(loim)
    fd_c = len(fodim)
    cd_c = len(cldim)
    ttl_i = lt_c + fd_c + cd_c
    print("\nLost Items    :", lt_c)
    print("Found Items   :", fd_c)
    print("Claimed Items :", cd_c)
    print("-" * 45)
    print("Total Items   :", ttl_i)
def savda():
    with open("data.txt", "w") as file:

        for i_id, dtls in loim.items():
            file.write(
                "LOST|" +
                str(i_id) + "|" +
                dtls["name"] + "|" +
                dtls["category"] + "|" +
                dtls["location"] + "|" +
                dtls["date"] + "|" +
                dtls["person"] + "\n"
            )
        for i_id, dtls in fodim.items():
            file.write(
                "FOUND|" +
                str(i_id) + "|" +
                dtls["name"] + "|" +
                dtls["category"] + "|" +
                dtls["location"] + "|" +
                dtls["date"] + "|" +
                dtls["person"] + "\n"
            )
        for i_id, dtls in cldim.items():
            file.write(
                "CLAIMED|" +
                str(i_id) + "|" +
                dtls["name"] + "|" +
                dtls["category"] + "|" +
                dtls["location"] + "|" +
                dtls["date"] + "|" +
                dtls["person"] + "|" +
                dtls["claimed_by"] + "\n"
            )
    print("\nData saved successfully")
load_data()
while True:
    print("\n" + "=" * 55)
    print("        LOST & FOUND MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Report Lost Item")
    print("2. Report Found Item")
    print("3. Search Item")
    print("4. View Lost Items")
    print("5. View Found Items")
    print("6. Claim / Recover Item")
    print("7. Remove Item")
    print("8. Statistics")
    print("9. Exit")
    print("-" * 55)
    choice = input("Enter your choice: ")
    if choice == "1":
        replosm()
    elif choice == "2":
        reportfounditem()
    elif choice == "3":
        searchitem()
    elif choice == "4":
        vwltit()
    elif choice == "5":
        vwfdit()
    elif choice == "6":
        clmitm()
    elif choice == "7":
        remits()
    elif choice == "8":
        stats()
    elif choice == "9":
        savda()
        print("\nThank you!")
        break
    else:
        print("\nInvalid choice! Please enter a number from 1 to 9.")


