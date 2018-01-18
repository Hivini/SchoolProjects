public class Human {

    // Atributes
    private String race;
    private float height;
    private float weight;

    // Access Methods
    // Race of the human
    private void setRace(String race){
        this.race = race;
    }
    public String getRace(){
        return race;
    }
    // Height of the human
    private void setHeight(float height){
        this.height = height;
    }
    public float getHeight(){
        return height;
    }
    // Weight of the human
    private void setWeight(float weight){
        this.weight = weight;
    }
    public float getWeight(){
        return weight;
    }

    // Constructor
    public Human(){
        race = "Caucasian";
        height = 1.70f;
        weight = 65f;
    }
    // Custom Constructor
    public Human(String race, float height, float weight){
        this.race = race;
        this.height = height;
        this.weight = weight;
    }

    // Behaviors
    public void talk(){
        System.out.println("The human is talking.");
    }
    public void stupid(){
        System.out.println("The human is being stupid.");
    }
    public void walking(){
        System.out.println("The human is walking.");
    }
}
