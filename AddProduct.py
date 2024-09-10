'''
    <a href="product.html?product=1" class="card">
        <img src="1/1.jpg" alt="Laptop 1">
        <div class="card-content">
            <h2>LAPTOP MICROSOFT SURFACE 3 15pouces</h2>
            <p class="price">87000DA</p>
            <p class="condition">Condition: New</p>
        </div>
    </a>
'''

'''
    ,
    '5': {
        name: 'HP Elitebook 840 G8',
        price: '------DA',
        condition: 'Condition: New',
        description: '➡INTEL CORE I5 1135G7 11ÈME GÉNÉRATION JUSQU’À 4.2GHz BOOST\n➡8GB DE RAM LPDDR4X 4266MHZ\n➡256GB SSD DE STOCKAGE M.2 PCIe 3.0\n➡ECRAN 15.6 POUCES FULL HD AMOLED ANTIREFLET NANOEDGE ROTATIF 360°\n➡CLAVIER LUMINEUX + FACE ID\n➡TRÈS BONNE AUTONOMIE DE BATTERIE\n➡FOURNIE AVEC CHARGEUR ORIGINAL\n➡PRIX : 99 500 DA\n➡LIVRAISON DISPONIBLE POUR TOUTES LES WILAYAS\n➡GARENTIE DE 3 MOIS',
        images: ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg'],
        link: "https://www.instagram.com/p/C-WBTbuoe1s/"
    }
'''

current_pid = input("Current Laptop ID: ")
laptop_name = input("New Laptop's Name: ")
laptop_cost = input("New Laptop's Cost: ")
laptop_cond = input("New Laptop's Cond: ")
laptop_desc = input("New Laptop's Cond: ")
laptop_imag = int(input("New Laptop's IMGs: "))
laptop_Link = input("New Laptop's Link: ")

#Images String System
i=1
images_set = "['1.jpg'"

while i<laptop_imag:
    images_set += f", '{i+1}.jpg'"
    i += 1 
images_set += "]"

print(images_set)

#Needed Strings
add_product_syntax = f"<a href='product.html?product={current_pid}' class='card'>\n  <img src='{current_pid}/1.jpg' alt='Laptop {current_pid}'>\n    <div class='card-content'>\n        <h2>{laptop_name}</h2>\n        <p class='price'>{laptop_cost}DA</p>\n        <p class='condition'>Condition: {laptop_cond}</p>\n    </div>\n</a>"
add_product_display = f",\n'{current_pid}': " + "{" + f"\n    name: '{laptop_name}',\n    price: '{laptop_cost}DA',\n    condition:'{laptop_cond}',\n    description: '{laptop_desc}',\n    images:'{images_set}',\n    link:'{laptop_Link}'\n" + "}"

#Coolest Output
print(add_product_syntax)
print("\n\n",add_product_display)