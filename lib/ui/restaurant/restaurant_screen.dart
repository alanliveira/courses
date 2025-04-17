import 'package:flutter/material.dart';

import 'package:myapp/model/restaurant.dart';
import 'package:myapp/ui/_core/bag_provider.dart';
import 'package:myapp/ui/_core/widgets/app_bar.dart';
import 'package:provider/provider.dart';

class RestaurantScreen extends StatelessWidget {
  final Restaurant restaurant;

  const RestaurantScreen({super.key, required this.restaurant});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: getAppBar(context: context, title: restaurant.name),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          spacing: 12,
          children: [
            Image.asset("assets/${restaurant.imagePath}", width: 128),
            Text(
              'Mais pedidos',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
            ),
            Column(
              children: List.generate(restaurant.dishes.length, (dishIndex) {
                final dish = restaurant.dishes[dishIndex];
                return ListTile(
                  leading: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      image: DecorationImage(
                        image: AssetImage('dishes/default.png'),
                        fit: BoxFit.cover,
                      ),
                      borderRadius: BorderRadius.all(Radius.circular(75.0)),
                      boxShadow: [
                        BoxShadow(blurRadius: 7.0, color: Colors.black),
                      ],
                    ),
                  ),
                  trailing: IconButton(
                    onPressed: () {
                      context.read<BagProvider>().addDish(dish);
                    },
                    icon: Icon(Icons.add),
                  ),
                  title: Text(dish.name),
                  subtitle: Text("R\$ ${dish.price.toStringAsFixed(2)}"),
                );
              }),
            ),
          ],
        ),
      ),
    );
  }
}
