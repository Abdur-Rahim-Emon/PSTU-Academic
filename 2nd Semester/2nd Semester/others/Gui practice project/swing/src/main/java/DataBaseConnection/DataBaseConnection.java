package DataBaseConnection;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class DataBaseConnection {
    public java.sql.Connection connection;
    public Statement statement;
    public static final String url="jdbc:mysql://localhost:3306/sms";
    final String userName = "root";
    final String password = "588342";
    public DataBaseConnection() {
        try{
            connection = DriverManager.getConnection(url,userName,password);
            statement=connection.createStatement();
         //   System.out.println("suceess full ");
        }
        catch(SQLException e){
            System.out.println(e);
        }
    }
}
