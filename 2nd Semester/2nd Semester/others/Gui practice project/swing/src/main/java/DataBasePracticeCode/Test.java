package DataBasePracticeCode;
import  DataBaseConnection.*;

import java.sql.PreparedStatement;
import java.sql.ResultSet;

import java.sql.PreparedStatement;

import java.sql.ResultSet;
public class Test{ 
     public static void main(String[] args) {
         
     
        int id=1;
        String name=null;
        String email=null;
        DataBaseConnection con = new DataBaseConnection();
        try{
            String query="insert into student(name,email) values(?,?)";
            PreparedStatement preparedStatement=con.connection.prepareStatement(query);
          //  preparedStatement.setInt(1, id);
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, email);
            preparedStatement.executeUpdate();
        }
        catch(Exception e){
            System.out.println(e);
        }
        //for printing my sql data
        int i;
        String s,s1;
        try{
            String query1="select * from student ";
            PreparedStatement preparedStatement=con.connection.prepareStatement(query1);
            ResultSet resultSet=preparedStatement.executeQuery();
            while(resultSet.next()){
                i=resultSet.getInt("id");
                s=resultSet.getString("name");
                s1=resultSet.getString("email");
                System.out.println(i+" "+s+" "+s1);
            }
            System.out.println("success");
        }
        catch(Exception e){
            System.out.println(e);
        }
 }}