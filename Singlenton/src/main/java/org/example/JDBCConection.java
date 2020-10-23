package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCConection {
    //Step-1
    private static JDBCConection jdbc;
    ///Step-2: Construct PRIVATE - prevents the instantiation from any other class.
    private JDBCConection() {  }
    //Step-3: Now we are providing global point of access.
    public static JDBCConection getInstance() {
        if (jdbc==null)
        { jdbc=new  JDBCConection();
        }
        return jdbc;
    }
    public static Connection getConnection()throws ClassNotFoundException, SQLException
    {   Connection con=null;
        try{
            //Class.forName("com.mysql.jdbc.Driver");
            Class.forName("com.mysql.cj.jdbc.Driver");
            con= DriverManager.getConnection("jdbc:mysql://localhost:3306/library", "root", "");
        }catch(Exception e){
            System.out.println("Error: "+e.getMessage());
        }
        return con;
    }
}//end class
