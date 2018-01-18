public class Bicycle {
    // Atributes
    private String color;
    private float avSpeed;
    private String trainingWheels;

    // Accesor methods
    // Color of the bicycle
    private void setColor(String color){
        this.color = color;
    }
    public String getColor(){
        return color;
    }
    // Average speed of the bicycle
    private void setAvSpeed(float avSpeed){
        this.avSpeed = avSpeed;
    }
    public float getAvSpeed(){
        return avSpeed;
    }
    // Does it have training wheels?
    private void setTrainingWheels(String trainingWheels){
        this.trainingWheels = trainingWheels;
    }
    public String getTrainingWheels(){
        return trainingWheels;
    }

    // Constructor
    public Bicycle(){
        color = "Gray";
        avSpeed = 15.5f;
        trainingWheels = "No";
    }
    // Custom Constructor
    public Bicycle(String color, float avSpeed, String trainingWheels){
        this.color = color;
        this.avSpeed = avSpeed;
        this.trainingWheels = trainingWheels;
    }

    // Behaviors
    public void breaks(){
        System.out.println("The bicycle is braking.");
    }
    public void turnLeft(){
        System.out.println("The bicycle is turning left.");
    }
    public void turnRight(){
        System.out.println("The bicycle is turning right.");
    }
}
