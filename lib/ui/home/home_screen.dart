import 'package:flutter/material.dart';
import 'package:myapp/data/catecories_data.dart';
import 'package:myapp/data/restaurants_data.dart';
import 'package:myapp/model/restaurant.dart';
import 'package:myapp/ui/_core/widgets/app_bar.dart';
import 'package:myapp/ui/home/widgets/category_widget.dart';
import 'package:myapp/ui/home/widgets/restaurant_widget.dart';
import 'package:provider/provider.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    RestaurantData restaurantData = Provider.of<RestaurantData>(context);

    return Scaffold(
      drawer: Drawer(),
      appBar: getAppBar(context: context),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            spacing: 32,
            children: [
              Center(child: Image.asset('assets/logo.png', width: 147)),
              Text('Boas Vindas!'),
              TextFormField(),
              Text('Escolha por categoria'),
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  spacing: 10,
                  children: List.generate(
                    CatecoriesData.listCategories.length,
                    (categoryIndex) {
                      return CategoryWidget(
                        category: CatecoriesData.listCategories[categoryIndex],
                      );
                    },
                  ),
                ),
              ),
              Image.asset('assets/banners/banner_promo.png'),
              Text(
                'Bem Avaliados',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  decoration: TextDecoration.underline,
                  fontSize: 24,
                ),
              ),
              Column(
                spacing: 10,
                children: List.generate(restaurantData.listRestaurants.length, (
                  index,
                ) {
                  Restaurant restaurant = restaurantData.listRestaurants[index];
                  return RestaurantWidget(restaurant: restaurant);
                }),
              ),
              SizedBox(width: 64),
            ],
          ),
        ),
      ),
    );
  }
}
