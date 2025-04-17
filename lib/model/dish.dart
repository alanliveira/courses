class Dish {
  final String id;
  final String name;
  final String imagePath;
  final int price;

  Dish({
    required this.id,
    required this.name,
    required this.imagePath,
    required this.price,
  });

  factory Dish.fromMap(Map<String, dynamic> map) {
    return Dish(
      id: map['id'] ?? '',
      name: map['name'] ?? '',
      imagePath: map['imagePath'] ?? '',
      price: map['price']?.toInt() ?? 0,
    );
  }

  Map<String, dynamic> toMap() {
    return {'id': id, 'name': name, 'imagePath': imagePath, 'price': price};
  }

  @override
  String toString() {
    return 'Dish(id: $id, name: $name, imagePath: $imagePath, price: $price)';
  }
}
