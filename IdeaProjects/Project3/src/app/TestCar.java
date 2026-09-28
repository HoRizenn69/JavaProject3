package app;

import vehicles.Car;
import vehicles.ElectricCar;

public class TestCar {
    public static void main(String[] args) {
        Car car = new Car("Toyota Camry", "A123BC77", "Черный", 2018, "Иван Иванов", "INS-10001");
        ElectricCar electricCar = new ElectricCar("Tesla Model 3", "E777EE77", "Белый", 2021, "Петр Петров", "INS-20002", 75);

        System.out.println("Исходные данные ТС");
        System.out.println(car.toString());
        System.out.println(electricCar.toString());

        car.setYear(2020);
        car.setOwnerName("Алексей Смирнов");

        electricCar.setYear(2023);
        electricCar.setOwnerName("Ольга Сидорова");

        car.setInsuranceNumber("INS-99999");
        electricCar.setInsuranceNumber("INS-88888");

        System.out.println("\nЕмкость батареи электромобиля: " + electricCar.getBatteryCapacity() + " kWh");

        System.out.println("\nОбновленные данные ТС");
        System.out.println(car.toString());
        System.out.println(electricCar.toString());
    }
}