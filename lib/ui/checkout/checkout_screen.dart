import 'package:flutter/material.dart';
import 'package:myapp/model/dish.dart';
import 'package:myapp/ui/_core/app_theme.dart';
import 'package:myapp/ui/_core/bag_provider.dart';
import 'package:provider/provider.dart';

class CheckoutScreen extends StatelessWidget {
  const CheckoutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final BagProvider bagProvider = Provider.of<BagProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Sacola'),
        centerTitle: true,
        actions: [
          TextButton(
            onPressed: () {
              bagProvider.clearBag();
            },
            child: Text('Limpar'),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(
                'Pedidos',
                textAlign: TextAlign.start,
                style: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
              ),
              Column(children: _generateBagItems(bagProvider)),
            ],
          ),
        ),
      ),
    );
  }

  List<Widget> _generateBagItems(BagProvider bagProvider) {
    if (bagProvider.getMapByDish().isEmpty) {
      return [
        Text('Sua sacola está vazia', style: TextStyle(color: Colors.grey)),
      ];
    }

    return List.generate(bagProvider.getMapByDish().keys.length, (dishIndex) {
      Dish dish = bagProvider.getMapByDish().keys.toList()[dishIndex];

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
            boxShadow: [BoxShadow(blurRadius: 7.0, color: Colors.black)],
          ),
        ),
        title: Text(dish.name),
        subtitle: Text("R\$ ${dish.price.toStringAsFixed(2)}"),
        trailing: Row(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          spacing: 5,
          children: [
            IconButton(
              onPressed: () {
                bagProvider.removeDish(dish);
              },
              icon: Icon(Icons.remove, size: 10),
              style: AppTheme.appTheme.elevatedButtonTheme.style?.copyWith(
                padding: WidgetStateProperty.all<EdgeInsets>(
                  EdgeInsets.symmetric(horizontal: 1.0, vertical: 1.0),
                ),
              ),
            ),
            Text(
              bagProvider.getMapByDish()[dish].toString(),
              style: TextStyle(fontSize: 24),
            ),
            IconButton(
              onPressed: () {
                bagProvider.addDish(dish);
              },
              icon: Icon(Icons.add),
              style: AppTheme.appTheme.elevatedButtonTheme.style,
            ),
          ],
        ),
      );
    });
  }
}
