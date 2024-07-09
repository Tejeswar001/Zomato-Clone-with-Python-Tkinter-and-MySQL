CREATE DATABASE IF NOT EXISTS zomato_clone;
USE zomato_clone;

-- Create Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    other_profile_info TEXT
);

INSERT INTO Users (username, password, email, other_profile_info) VALUES
('Sri', 'password123', 'sri@gmail.com', 'Loves Italian food'),
('Teju', 'password456', 'teju@gmail.com', 'Vegetarian'),
('Manohari', 'password789', 'manuu@gamil.com', 'Enjoys spicy food'),
('Ramanii', 'password901', 'ramanii@gmail.com', 'Non- veg lover'),
('Akshitha', 'password321', 'akshitha@gmail.com' , 'Non- spicy food only'),
('Vikram', 'password234', 'vikram@gmail.com', 'Prefers vegan food'),
('Suman', 'password567', 'suman@yahoo.com', 'Loves street food'),
('Nithya', 'password890', 'nithya@hotmail.com', 'Enjoys gourmet cuisine'),
('Karthik', 'password112', 'karthik@gmail.com', 'Gluten-free diet'),
('Anjali', 'password334', 'anjali@gmail.com', 'Prefers organic food'),
('Rajesh', 'password556', 'rajesh@gmail.com', 'Loves fast food'),
('Pooja', 'password778', 'pooja@gmail.com', 'Sugar-free diet'),
('Arjun', 'password990', 'arjun@gmail.com', 'Enjoys Mediterranean food'),
('Sneha', 'password1234', 'sneha@gmail.com', 'Prefers raw food diet'),
('Ravi', 'password5678', 'ravi@gmail.com', 'Loves seafood');



CREATE TABLE Restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    cuisine VARCHAR(50),
    rating DECIMAL(3, 2),
    other_info TEXT
);

INSERT INTO Restaurants (name, location, cuisine, rating, other_info) VALUES

('Paradise', 'Hyderabad', 'Non-veg', 4.6, 'Renowned for biryani'),
('Rasoi Ghar', 'Mumbai', 'Vegetarian', 4.7, 'Authentic Gujarati thali'),
('Coastal Spice', 'Chennai', 'Indian', 4.3, 'Specializes in coastal cuisine'),
('Spice Symphony', 'Delhi', 'Non-veg', 4.8, 'Known for butter chicken'),
('Urban Tadka', 'Pune', 'veg and non-veg', 4.5, 'Fusion cuisine with a modern twist'),
('Saffron', 'Kolkata', 'Indian', 4.4, 'Bengali delicacies'),
('Tandoori Flames', 'Ahmedabad', 'Non-veg', 4.6, 'Delicious kebabs and tikkas'),
('Green Leaf', 'Coimbatore', 'Vegetarian', 4.7, 'Organic and farm-fresh dishes'),
('Royal Feast', 'Jaipur', 'Indian', 4.5, 'Rajasthani royal cuisine'),
('Blue Bay', 'Goa', 'veg and non-veg', 4.8, 'Seafood and beachside dining');



CREATE TABLE IF NOT EXISTS Menus (
    menu_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id) ON DELETE CASCADE
);

INSERT INTO Menus (restaurant_id, item_name, price, description) VALUES

(1, 'Mutton Rogan Josh', 180, 'Tender mutton cooked in aromatic spices.'),
(1, 'Haleem', 220, 'A rich and savory meat and lentil stew.'),
(1, 'Tandoori Chicken', 180, 'Juicy chicken marinated in yogurt and spices.'),
(1, 'Chicken 65', 160, 'Spicy, deep-fried chicken bites.'),
(1, 'Vegetable Samosa', 50, 'Crispy pastry filled with spiced potatoes and peas.'),
(1, 'Chicken Kebab', 140, 'Grilled chicken skewers with spices.'),
(1, 'Chicken Manchurian', 180, 'Chicken in a tangy and spicy Manchurian sauce.'),
(1, 'Malai Kofta', 180, 'Fried dumplings in a creamy sauce.'),
(1, 'Butter Chicken', 200, 'Creamy and rich butter chicken.'),
(1, 'Mutton Biryani', 300, 'Flavorful and aromatic mutton biryani.'),
(2, 'Mixed Vegetable Curry', 130, 'A delightful medley of seasonal vegetables.'),
(2, 'Aloo Gobi', 90, 'Classic potato and cauliflower curry.'),
(2, 'Palak Paneer', 150, 'Creamy spinach with cubes of paneer.'),
(2, 'Rajma Chawal', 120, 'Kidney beans curry with rice.'),
(2, 'Bhindi Masala', 130, 'Stir-fried okra with onions and tomatoes.'),
(2, 'Jeera Rice', 90, 'Basmati rice flavored with cumin seeds.'),
(2, 'Gobi Manchurian', 120, 'Crispy cauliflower in Manchurian sauce.'),
(2, 'Paneer Bhurji', 140, 'Scrambled paneer with spices.'),
(2, 'Dal Makhani', 110, 'Creamy black lentils cooked with butter.'),
(2, 'Vegetable Korma', 160, 'Mixed vegetables in a creamy coconut sauce.'),
(3, 'Fish Fry', 150, 'Crispy fried fish with a tangy dip.'),
(3, 'Dal Makhani', 110, 'Creamy black lentils cooked with butter.'),
(3, 'Hyderabadi Biryani', 220, 'Spicy and flavorful Hyderabadi biryani.'),
(3, 'Lamb Vindaloo', 180, 'Spicy and tangy lamb curry.'),
(3, 'Prawn Biryani', 250, 'Biryani with succulent prawns and aromatic spices.'),
(3, 'Paneer Butter Masala', 170, 'Paneer in a rich tomato and butter sauce.'),
(3, 'Mutton Biryani', 270, 'Aromatic biryani with tender mutton pieces.'),
(3, 'Chicken Chettinad', 210, 'Spicy chicken curry from Chettinad.'),
(3, 'Fish Amritsari', 180, 'Crispy fried fish with spices.'),
(3, 'Fish Curry', 220, 'Fish cooked in a coconut milk-based curry.'),
(4, 'Butter Chicken', 200, 'Creamy and rich butter chicken.'),
(4, 'Keema Naan', 130, 'Naan stuffed with minced meat.'),
(4, 'Mutton Biryani', 300, 'Flavorful and aromatic mutton biryani.'),
(4, 'Chicken Tikka Masala', 200, 'Grilled chicken in a rich tomato sauce.'),
(4, 'Fish Curry', 220, 'Fish cooked in a coconut milk-based curry.'),
(4, 'Vegetable Hakka Noodles', 150, 'Stir-fried noodles with mixed vegetables.'),
(4, 'Chicken Shawarma', 160, 'Grilled chicken wrapped in pita bread.'),
(4, 'Kadhai Paneer', 160, 'Paneer cooked with bell peppers and tomatoes.'),
(4, 'Dal Tadka', 110, 'Yellow lentils tempered with spices.'),
(4, 'Chicken Chettinad', 210, 'Spicy chicken curry from Chettinad.'),
(5, 'Egg Biryani', 140, 'Delicious biryani with boiled eggs.'),
(5, 'Prawn Curry', 250, 'Succulent prawns in a spicy coconut curry.'),
(5, 'Chicken Tikka Masala', 200, 'Grilled chicken in a rich tomato sauce.'),
(5, 'Chole Bhature', 140, 'Spicy chickpeas with fried bread.'),
(5, 'Mutton Korma', 300, 'Tender mutton in a rich, creamy sauce.'),
(5, 'Vegetable Pulao', 130, 'Rice cooked with mixed vegetables and spices.'),
(5, 'Chicken Shawarma', 160, 'Grilled chicken wrapped in pita bread.'),
(5, 'Fish Curry', 220, 'Fish cooked in a coconut milk-based curry.'),
(5, 'Chicken Chettinad', 210, 'Spicy chicken curry from Chettinad.'),
(5, 'Vegetable Hakka Noodles', 150, 'Stir-fried noodles with mixed vegetables.'),
(6, 'Haleem', 220, 'A rich and savory meat and lentil stew.'),
(6, 'Mutton Biryani', 300, 'Flavorful and aromatic mutton biryani.'),
(6, 'Chicken Tikka Masala', 200, 'Grilled chicken in a rich tomato sauce.'),
(6, 'Mutton Korma', 300, 'Tender mutton in a rich, creamy sauce.'),
(6, 'Vegetable Korma', 160, 'Mixed vegetables in a creamy coconut sauce.'),
(6, 'Dal Tadka', 110, 'Yellow lentils tempered with spices.'),
(6, 'Vegetable Pulao', 130, 'Rice cooked with mixed vegetables and spices.'),
(6, 'Chicken Shawarma', 160, 'Grilled chicken wrapped in pita bread.'),
(6, 'Fish Curry', 220, 'Fish cooked in a coconut milk-based curry.'),
(6, 'Chicken Chettinad', 210, 'Spicy chicken curry from Chettinad.'),
(7, 'Aloo Gobi', 90, 'Classic potato and cauliflower curry.'),
(7, 'Bhindi Masala', 130, 'Stir-fried okra with onions and tomatoes.'),
(7, 'Jeera Rice', 90, 'Basmati rice flavored with cumin seeds.'),
(7, 'Paneer Butter Masala', 170, 'Paneer in a rich tomato and butter sauce.'),
(7, 'Dal Tadka', 110, 'Yellow lentils tempered with spices.'),
(7, 'Vegetable Pulao', 130, 'Rice cooked with mixed vegetables and spices.'),
(7, 'Vegetable Korma', 160, 'Mixed vegetables in a creamy coconut sauce.'),
(7, 'Paneer Bhurji', 140, 'Scrambled paneer with spices.'),
(7, 'Vegetable Hakka Noodles', 150, 'Stir-fried noodles with mixed vegetables.'),
(7, 'Malai Kofta', 180, 'Fried dumplings in a creamy sauce.'),
(8, 'Mixed Vegetable Curry', 130, 'A delightful medley of seasonal vegetables.'),
(8, 'Palak Paneer', 150, 'Creamy spinach with cubes of paneer.'),
(8, 'Rajma Chawal', 120, 'Kidney beans curry with rice.'),
(8, 'Bhindi Masala', 130, 'Stir-fried okra with onions and tomatoes.'),
(8, 'Jeera Rice', 90, 'Basmati rice flavored with cumin seeds.'),
(8, 'Paneer Bhurji', 140, 'Scrambled paneer with spices.'),
(8, 'Gobi Manchurian', 120, 'Crispy cauliflower in Manchurian sauce.'),
(8, 'Dal Makhani', 110, 'Creamy black lentils cooked with butter.'),
(8, 'Vegetable Korma', 160, 'Mixed vegetables in a creamy coconut sauce.'),
(8, 'Aloo Gobi', 90, 'Classic potato and cauliflower curry.'),
(9, 'Royal Biryani', 280, 'Special Rajasthani biryani with a blend of spices.'),
(9, 'Laal Maas', 320, 'Spicy Rajasthani mutton curry.'),
(9, 'Gatte Ki Sabzi', 180, 'Gram flour dumplings in a tangy yogurt sauce.'),
(9, 'Ker Sangri', 150, 'Traditional Rajasthani desert beans and berries curry.'),
(9, 'Pyaaz Kachori', 70, 'Flaky pastry filled with spicy onion mixture.'),
(9, 'Dal Baati Churma', 220, 'Traditional Rajasthani dish with lentils and baked wheat balls.'),
(9, 'Rajasthani Thali', 350, 'Assorted Rajasthani dishes served in a thali.'),
(9, 'Mawa Kachori', 60, 'Sweet pastry filled with mawa and dry fruits.'),
(9, 'Bajra Roti', 30, 'Traditional millet flatbread.'),
(9, 'Papad Ki Sabzi', 140, 'Spicy curry made with papad.'),
(10, 'Seafood Platter', 450, 'Assorted seafood served with dips.'),
(10, 'Goan Fish Curry', 280, 'Traditional Goan fish curry with coconut milk.'),
(10, 'Prawn Balchao', 300, 'Spicy prawn pickle from Goa.'),
(10, 'Chicken Xacuti', 250, 'Goan chicken curry with roasted spices.'),
(10, 'Bebinca', 180, 'Traditional Goan layered dessert.'),
(10, 'Sorpotel', 320, 'Goan pork curry.'),
(10, 'Goan Prawn Curry', 290, 'Prawns cooked in a coconut milk-based curry.'),
(10, 'Goan Sausage Pulao', 260, 'Rice cooked with Goan sausages.'),
(10, 'Kingfish Fry', 300, 'Crispy fried kingfish with Goan spices.'),
(10, 'Pork Vindaloo', 340, 'Spicy and tangy pork curry from Goa.');



CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    restaurant_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id) ON DELETE CASCADE
);

INSERT INTO Orders (user_id, restaurant_id, total_amount) VALUES
(1, 1, 270),
(2, 2, 270),
(3, 3, 260),
(4, 4, 150),
(5, 5, 300);


CREATE TABLE IF NOT EXISTS OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    menu_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (menu_id) REFERENCES Menus(menu_id) ON DELETE CASCADE
);

INSERT INTO OrderDetails (order_id, menu_id, quantity, price) VALUES
(1, 1, 1, 170),
(1, 2, 1, 360),
(2, 3, 1, 250),
(2, 4, 1, 400),
(3, 5, 1, 150),
(3, 6, 1, 170),
(4, 4, 1, 200),
(5, 3, 1, 150);

ALTER TABLE Menus
ADD COLUMN average_rating DECIMAL(3, 2) DEFAULT NULL;

-- Alter OrderDetails table to include item_name column
ALTER TABLE OrderDetails
ADD COLUMN item_name VARCHAR(100) NOT NULL;

ALTER TABLE Menus
DROP COLUMN average_rating;

ALTER TABLE Menus
DROP COLUMN total_rating;

ALTER TABLE Menus
ADD COLUMN average_rating int default 0;

ALTER TABLE Menus
ADD COLUMN total_rating int default 0;
