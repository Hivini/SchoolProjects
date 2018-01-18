public class Main {
    public static void main(String[] args) {
        // Initialization of all the objects.
        Bicycle mountainBike = new Bicycle();
        Bicycle bmx = new Bicycle();
        Dog corgi = new Dog();
        Dog shibaInu = new Dog();
        Human steve = new Human();
        Human alice = new Human();
        
        System.out.println(bmx.getColor());
        bmx.breaks();
    }
}
