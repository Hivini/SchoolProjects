public class Main {
    public static void main(String[] args) {
        // Initialization of all the objects.
        Bicycle mountainBike = new Bicycle();
        Bicycle bmx = new Bicycle("Red", 20.3f, "Yes");
        Dog corgi = new Dog();
        Dog shibaInu = new Dog("Medium", "Read Coat", 3);
        Human steve = new Human();
        Human alice = new Human("Negroid", 1.60f, 55.4f);

        // Sorry for the thousands of println
        // Printing bicycles attributes
        System.out.println("-------Bicycle-------");
        System.out.println("- Mountain Bike");
        System.out.println("Color: " + mountainBike.getColor());
        System.out.println("Average Speed: " + Float.toString(mountainBike.getAvSpeed()));
        System.out.println("Training Wheels: " + mountainBike.getTrainingWheels());
        System.out.println("\n- BMX");
        System.out.println("Color: " + bmx.getColor());
        System.out.println("Average Speed: " + Float.toString(bmx.getAvSpeed()));
        System.out.println("Training Wheels: " + bmx.getTrainingWheels() + "\n");
        // Printing bicycles behaviors
        bmx.breaks();
        bmx.turnLeft();
        bmx.turnRight();

        // Printing dogs attributes
        System.out.println("\n-------Dog-------");
        System.out.println("- Corgi");
        System.out.println("Size: " + corgi.getSize());
        System.out.println("Color: " + corgi.getColor());
        System.out.println("Age " + Integer.toString(corgi.getAge()));
        System.out.println("\n- Shiba Inu");
        System.out.println("Size: " + shibaInu.getSize());
        System.out.println("Color: " + shibaInu.getColor());
        System.out.println("Age " + Integer.toString(shibaInu.getAge()) + "\n");
        // Printing dogs behaviors
        corgi.bark();
        corgi.poop();
        corgi.destroy();

        // Printing humans attributes
        System.out.println("\n-------Human-------");
        System.out.println("- Steve");
        System.out.println("Race: " + steve.getRace());
        System.out.println("Height: " + Float.toString(steve.getHeight()) + "m");
        System.out.println("Weight: " + Float.toString(steve.getWeight()) + "kg");
        System.out.println("\n- Alice");
        System.out.println("Race: " + alice.getRace());
        System.out.println("Height: " + Float.toString(alice.getHeight()) + "m");
        System.out.println("Weight: " + Float.toString(alice.getWeight()) + "kg\n");
        // Printing human behaviors
        alice.talk();
        alice.stupid();
        alice.walking();




    }
}
