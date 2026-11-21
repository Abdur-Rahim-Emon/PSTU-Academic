
package W;
class Car {
    private String color;
    private String engine;
    private boolean sunroof;

    public Car setColor(String color) {
        this.color = color;
        return this; // Returns the current object (this) to allow method chaining
    }

    public Car setEngine(String engine) {
        this.engine = engine;
        return this;
    }

    public Car setSunroof(boolean sunroof) {
        this.sunroof = sunroof;
        return this;
    }

    public void showDetails() {
        System.out.println("Color: " + color + ", Engine: " + engine + ", Sunroof: " + sunroof);
    }
}
public class TEst {
    public static void main(String[] args) {
        Car car = new Car().setColor("Red").setEngine("V8").setSunroof(true);
        car.showDetails();

    }
            

    
}
