public class Dog {

    // Atributes
    private String size;
    private String color;
    private int age;

    // Accesor methods
    // Size of the dog
    private void setSize(String size){
        this.size = size;
    }
    public String getSize(){
        return size;
    }
    // Color of the dog
    private void setColor(String color){
        this.color = color;
    }
    public String getColor(){
        return color;
    }
    // Age of the dog
    private void setAge(int age){
        this.age = age;
    }
    public int age(){
        return age;
    }

    // Constructor
    public Dog(){
        size = "Medium";
        color = "Brown";
        age = 7;
    }
    // Custom constructor
    public Dog(String size, String color, int age){
        this.size = size;
        this.color = color;
        this.age = age;
    }

    // Behaviors
    public void bark(){
        System.out.println("The dog is barking.");
    }
    public void poop(){
        System.out.println("The dog is pooping.");
    }
    public void destroy(){
        System.out.println("The dog is destroying the shoe.");
    }
}
