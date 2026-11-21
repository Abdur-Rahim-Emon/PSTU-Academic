
package W3;


public class Test {
    public static void main(String[] args) {
        Employee e1=new Employee();
        e1.getValue("Abdur ", 25,"02343434","Patuakhali ", 333333,"Salse");
        e1.show();
        System.out.println("manager details ");
        Manager m1=new Manager();
        m1.getValue1("Emon", 30,"93434934","Nilphamari ", 44444444, "Manager");
        m1.show1();
    }
}
