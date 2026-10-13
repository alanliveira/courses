import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:myapp/model/restaurant.dart';

class RestaurantData extends ChangeNotifier {
  List<Restaurant> listRestaurants = [];

  Future<void> getRestaurants() async {
    String jsonString = await rootBundle.loadString('assets/data.json');
    Map<String, dynamic> data = json.decode(jsonString);
    List<dynamic> dataRestaurants = data['restaurants'];

    for (var dataRestaurant in dataRestaurants) {
      Restaurant restaurant = Restaurant.fromMap(dataRestaurant);
      listRestaurants.add(restaurant);
    }
  }
}
