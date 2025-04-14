import 'package:flutter/material.dart';
import 'package:myapp/ui/_core/app_colors.dart';

abstract class AppTheme {
  static ThemeData appTheme = ThemeData.dark().copyWith(
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ButtonStyle(
        backgroundColor: WidgetStateColor.resolveWith((states) {
          if (states.contains(WidgetState.disabled)) {
            return Colors.grey;
          } else if (states.contains(WidgetState.pressed)) {
            return Color.fromARGB(171, 255, 164, 89);
          }
          return AppColors.mainColor;
        }),
        foregroundColor: WidgetStatePropertyAll(Colors.black)
      ),
    ),
  );
}
