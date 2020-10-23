package org.uab.solid;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCConnection {
    private static JDBCConnection jdbc;
    private JDBCConnection() {  }
    //Now we are providing global point of access.
    public static JDBCConnection getInstance() {
        if (jdbc==null)
        {   jdbc=new  JDBCConnection(); }
        return jdbc;
    }

    public static Connection getConnection()throws ClassNotFoundException, SQLException
    {   Connection con = null;
        try{
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/library", "root", "");
        }catch(Exception e){
            System.out.println("Error en la conexion a BD:......."+e.getMessage());
        }
        return con;
    }//end function

}// end class
