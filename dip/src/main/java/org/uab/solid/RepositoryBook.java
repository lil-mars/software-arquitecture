package org.uab.solid;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class RepositoryBook {
    public RepositoryBook(){ }

    public List<Book> viewListBooks(){
        List<Book> listBook = new ArrayList();

        try{
            Connection con = JDBCConnection.getConnection();
            Statement stmt=con.createStatement();
            ResultSet rs=stmt.executeQuery("SELECT * FROM book;");
            while(rs.next()) {
                Book book = new Book();
                System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getString(3));
                book.setIdBook(rs.getInt(1));
                book.setTitle(rs.getString(2));
                book.setSample(rs.getString(3));
                listBook.add(book);
            }
        }catch(Exception e){
            System.out.println("Error: "+e);
        }
        return listBook;
    }//end function

}//end class
